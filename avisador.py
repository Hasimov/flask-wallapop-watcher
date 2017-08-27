from flask_script import Manager
from flask_mail import Mail, Message
from models import db, Programado

from app import app

app.config.update(
    MAIL_SERVER='smtp.mailgun.org',
    MAIL_PORT=587,
    MAIL_USERNAME='postmaster@sandboxcbf540cc1c514f818bce4f566e6a1477.mailgun.org',
    MAIL_PASSWORD='9176ea5fc4c32da768f334c33f6c8b20'
)
mail = Mail(app)

manager = Manager(app)

@manager.command
def buscar_y_notificar():
    msg = Message(
        "Nuevo aviso",
        sender="no-reply@pycon17.es",
        recipients=["andros@fenollosa.email"]
        )
    msg.body = "testing"
    msg.html = "<b>testing</b>"
    mail.send(msg)


@manager.command
def test():
    programado_all = Programado.query.all()
    app.get_resultados()

if __name__ == "__main__":
    manager.run()