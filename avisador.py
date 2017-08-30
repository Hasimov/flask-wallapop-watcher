#!/usr/bin/env python3
from flask import render_template
from flask_script import Manager
from app import app, get_resultados
from flask_mail import Mail, Message
from models import db, Programado

app.config.update(
    MAIL_SERVER='smtp.mailgun.org',
    MAIL_PORT=587,
    MAIL_USERNAME='postmaster@sandboxcbf540cc1c514f818bce4f566e6a1477.mailgun.org',
    MAIL_PASSWORD='9176ea5fc4c32da768f334c33f6c8b20'
)
mail = Mail(app)

manager = Manager(app)

@manager.command
def send_email():
    programados = Programado.query.all()
    for item in programados:
        # Get last id
        results = get_resultados(item.title)
        itemId = results[0]['itemId']
        # Update last item in database
        if int(itemId) != item.last_item:
            programado_update = Programado.query.filter_by(id=item.id).first()
            programado_update.last_item = itemId
            db.session.add(programado_update)
            try:
                db.session.commit()
            except:
                db.session.rollback()
            # Send email
            msg = Message(
                "Nuevo aviso",
                sender="no-reply@pycon17.es",
                recipients=["andros@fenollosa.email"]
            )
            msg.body = render_template('emails/notificacion.txt', title=results[0]['title'], id=itemId)
            msg.html = render_template('emails/notificacion.html', title=results[0]['title'], id=itemId)
            mail.send(msg)

if __name__ == "__main__":
    manager.run()

