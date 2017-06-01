import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '345083071:AAHtSaRQT0jcOx5OCPOQnWWvpCtJ25z7TOA'
WEBHOOK_URL = 'https://57e5066d.ngrok.io/hook'

global first
first = 1
app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'init',
        'MC_main',
        'KFC_main',
        'SUB_main',
        'MC_choose',
        'MC_dessert',
        'MC_snack',
        'KFC_snack',
        'KFC_count',
        'SUB_salad',
        'drink',
        'final',
        'result'               
    ],
    transitions=[    	
    	{
            'trigger': 'advance',
            'source': 'init',
            'dest': 'MC_main',
            'conditions': 'is_going_to_MC_main'
        },
        {
            'trigger': 'advance',
            'source': 'MC_main',
            'dest': 'MC_choose',
            'conditions': 'is_going_to_MC_m_1'
        },
        {
            'trigger': 'advance',
            'source': 'MC_main',
            'dest': 'MC_choose',
            'conditions': 'is_going_to_MC_m_2'
        },
        {
            'trigger': 'advance',
            'source': 'MC_main',
            'dest': 'MC_choose',
            'conditions': 'is_going_to_MC_m_3'
        },
        {
            'trigger': 'advance',
            'source': 'MC_choose',
            'dest': 'MC_dessert',
            'conditions': 'is_going_to_MC_c_1'
        },
        {
            'trigger': 'advance',
            'source': 'MC_choose',
            'dest': 'MC_snack',
            'conditions': 'is_going_to_MC_c_2'
        },
        {
            'trigger': 'advance',
            'source': 'MC_dessert',
            'dest': 'drink',
            'conditions': 'is_going_to_MC_d_1'
        },
        {
            'trigger': 'advance',
            'source': 'MC_dessert',
            'dest': 'drink',
            'conditions': 'is_going_to_MC_d_2'
        },
        {
            'trigger': 'advance',
            'source': 'MC_dessert',
            'dest': 'drink',
            'conditions': 'is_going_to_MC_d_3'
        },
        {
            'trigger': 'advance',
            'source': 'MC_snack',
            'dest': 'drink',
            'conditions': 'is_going_to_MC_s_1'
        },
        {
            'trigger': 'advance',
            'source': 'MC_snack',
            'dest': 'drink',
            'conditions': 'is_going_to_MC_s_2'
        },
        {
            'trigger': 'advance',
            'source': 'init',
            'dest': 'KFC_main',
            'conditions': 'is_going_to_KFC_main'
        },
        {
            'trigger': 'advance',
            'source': 'KFC_main',
            'dest': 'KFC_count',
            'conditions': 'is_going_to_KFC_m_1'
        },
        {
            'trigger': 'advance',
            'source': 'KFC_count',
            'dest': 'KFC_snack',
            'conditions': 'is_going_to_KFC_c'
        },
        {
            'trigger': 'advance',
            'source': 'KFC_main',
            'dest': 'KFC_snack',
            'conditions': 'is_going_to_KFC_m_2'
        },
        {
            'trigger': 'advance',
            'source': 'KFC_main',
            'dest': 'KFC_snack',
            'conditions': 'is_going_to_KFC_m_3'
        },
        {
            'trigger': 'advance',
            'source': 'KFC_snack',
            'dest': 'drink',
            'conditions': 'is_going_to_KFC_s_1'
        },
        {
            'trigger': 'advance',
            'source': 'KFC_snack',
            'dest': 'drink',
            'conditions': 'is_going_to_KFC_s_2'
        },
        {
            'trigger': 'advance',
            'source': 'KFC_snack',
            'dest': 'drink',
            'conditions': 'is_going_to_KFC_s_3'
        },
        {
            'trigger': 'advance',
            'source': 'init',
            'dest': 'SUB_main',
            'conditions': 'is_going_to_SUB_main'
        },
        {
            'trigger': 'advance',
            'source': 'SUB_main',
            'dest': 'SUB_salad',
            'conditions': 'is_going_to_SUB_m_1'
        },
        {
            'trigger': 'advance',
            'source': 'SUB_main',
            'dest': 'SUB_salad',
            'conditions': 'is_going_to_SUB_m_2'
        },
        {
            'trigger': 'advance',
            'source': 'SUB_main',
            'dest': 'SUB_salad',
            'conditions': 'is_going_to_SUB_m_3'
        },
        {
            'trigger': 'advance',
            'source': 'SUB_salad',
            'dest': 'drink',
            'conditions': 'is_going_to_SUB_s_1'
        },
        {
            'trigger': 'advance',
            'source': 'SUB_salad',
            'dest': 'drink',
            'conditions': 'is_going_to_SUB_s_2'
        },
        {
            'trigger': 'advance',
            'source': 'SUB_salad',
            'dest': 'drink',
            'conditions': 'is_going_to_SUB_s_3'
        },
        {
            'trigger': 'advance',
            'source': 'drink',
            'dest': 'final',
            'conditions': 'is_going_to_drink_1'
        },
        {
            'trigger': 'advance',
            'source': 'drink',
            'dest': 'final',
            'conditions': 'is_going_to_drink_2'
        },
        {
            'trigger': 'advance',
            'source': 'drink',
            'dest': 'final',
            'conditions': 'is_going_to_drink_3'
        },
        {
            'trigger': 'advance',
            'source': 'drink',
            'dest': 'final',
            'conditions': 'is_going_to_drink_4'
        },
        {
            'trigger': 'advance',
            'source': 'final',
            'dest': 'result',
            'conditions': 'is_going_to_result'
        },
        {
            'trigger': 'advance',
            'source': 'final',
            'dest': 'init',
            'conditions': 'is_going_to_init'
        },        

    ],
    initial='init',
    auto_transitions=False,
    show_conditions=True,

)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    if(first == 1):
    	update.message.reply_text("What do you want to eat ?")    	
    	update.message.reply_text("1)McDonald's")
    	update.message.reply_text("2)KFC")
    	update.message.reply_text("3)SUBWAY")
    	global first
    	first = 0
    else:
    	machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)    
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()    
    app.run()
