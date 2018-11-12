from flask import Flask, render_template
from flask import request
from service.InitiativeService import InitiativeService
app = Flask(__name__)

init = InitiativeService()


@app.route('/')
@app.route('/main')
def root():
    return render_template('index.html')


@app.route('/init')
def initiative():
    holder = init.get_session_holder()
    holder.clear()
    holder.add_actor("Wu kong", 12)
    holder.add_actor("Lee Sin", 10)
    holder.add_actor("Vi", 8)
    return render_template('initiative.html', init=holder)


@app.route('/init/next')
def initiative_next():
    holder = init.get_session_holder()
    holder.step()
    return render_template('initiative.html', init=holder)


@app.route('/init/delay')
def initiative_delay():
    name = request.args.get('name')
    value = request.args.get('value')
    holder = init.get_session_holder()
    holder.delay_actor(name, int(value))
    return render_template('initiative.html', init=holder)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
