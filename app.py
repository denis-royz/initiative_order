from flask import Flask, render_template
from flask import request
from service.InitiativeService import InitiativeService
from envparse import Env

app = Flask(__name__)
init = InitiativeService()
env = Env(
    INITIATIVE_PARSER_HOST=dict(cast=str,  default='0.0.0.0'),
    INITIATIVE_PARSER_PORT=dict(cast=int,  default='5000')
)
env.read_envfile()


@app.route('/')
def root():
    holder = init.get_session_holder()
    return render_template('initiative.html', init=holder)


@app.route('/slave')
def slave():
    holder = init.get_session_holder()
    return render_template('initiative_slave.html', init=holder)


@app.route('/api/v1/reset')
def reset():
    init.reset()
    holder = init.get_session_holder()
    return render_template('actors.html', init=holder)


@app.route('/api/v1/actors/end_of_turn')
def initiative_next():
    holder = init.get_session_holder()
    holder.step()
    return render_template('actors.html', init=holder)


@app.route('/api/v1/actors/new')
def initiative_add():
    name = request.args.get('name')
    value = request.args.get('value')
    holder = init.get_session_holder()
    holder.add_actor(name, int(value))
    return render_template('actors.html', init=holder)


@app.route('/api/v1/set_init')
def initiative_delay():
    actor_id = request.args.get('actor_id')
    value = request.args.get('value')
    holder = init.get_session_holder()
    holder.set_init_to_actor(actor_id, int(value))
    return render_template('actors.html', init=holder)


@app.route('/api/v1/delete')
def delete_actor():
    actor_id = request.args.get('actor_id')
    holder = init.get_session_holder()
    holder.delete_actor(actor_id)
    return render_template('actors.html', init=holder)


if __name__ == '__main__':
    print('INITIATIVE_PARSER_HOST =', env.str('INITIATIVE_PARSER_HOST'))
    print('INITIATIVE_PARSER_PORT =', env.int('INITIATIVE_PARSER_PORT'))
    app.run(host=env.str('INITIATIVE_PARSER_HOST'), port=env.int('INITIATIVE_PARSER_PORT'))
а