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
@app.route('/main')
def root():
    holder = init.get_session_holder()
    return render_template('initiative.html', init=holder)


@app.route('/main/init')
def initiative():
    holder = init.get_session_holder()
    holder.clear()
    holder.add_actor("Wu kong", 12)
    holder.add_actor("Lee Sin", 10)
    holder.add_actor("Vi", 8)
    return render_template('initiative.html', init=holder)


@app.route('/init')
def initiative():
    holder = init.get_session_holder()
    holder.clear()
    holder.add_actor("Wu kong", 12)
    holder.add_actor("Lee Sin", 10)
    holder.add_actor("Vi", 8)
    return render_template('initiative.html', init=holder)


@app.route('/actors/end_of_turn')
def initiative_next():
    holder = init.get_session_holder()
    holder.step()
    return render_template('actors.html', init=holder)


@app.route('/actors/new')
def initiative_add():
    name = request.args.get('name')
    value = request.args.get('value')
    holder = init.get_session_holder()
    holder.add_actor(name, int(value))
    return render_template('actors.html', init=holder)


@app.route('/actors/delay')
def initiative_delay():
    name = request.args.get('name')
    value = request.args.get('value')
    holder = init.get_session_holder()
    holder.delay_actor(name, int(value))
    return render_template('initiative.html', init=holder)


if __name__ == '__main__':
    print('INITIATIVE_PARSER_HOST =', env.str('INITIATIVE_PARSER_HOST'))
    print('INITIATIVE_PARSER_PORT =', env.int('INITIATIVE_PARSER_PORT'))
    app.run(host=env.str('INITIATIVE_PARSER_HOST'), port=env.int('INITIATIVE_PARSER_PORT'))
