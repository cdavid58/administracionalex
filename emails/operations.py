from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .template_email import *
import smtplib,requests
from .template_email import *

class Send_Emails:

	def Confirm_Email(self,email,name_user,pk):
		result = False
		try:
			remitente = 'notificacionesoftware@gmail.com'
			destinatarios = ["notificacionesoftware@gmail.com",str(email)]
			asunto = 'Activación de cuenta'
			html = CONFIRM_EMAIL
			html = html.replace("$(username)",str(name_user))
			html = html.replace("$(pk)",str(pk))
			html = html.replace("$(url)",f"http://localhost:8000/Activate_Account/{pk}")
			mensaje = MIMEMultipart()
			mensaje['From'] = remitente
			mensaje['To'] = ", ".join(destinatarios)
			mensaje['Subject'] = asunto
			mensaje.attach(MIMEText(html,'html'))
			sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
			sesion_smtp.starttls()
			texto = mensaje.as_string()
			usuario = "notificacionesoftware@gmail.com"
			clave = "zwtalrafuyidxxms"
			sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
			sesion_smtp.starttls()
			texto = mensaje.as_string()
			remitente = usuario
			sesion_smtp.login(usuario,clave)
			sesion_smtp.sendmail(remitente, destinatarios, texto)
			sesion_smtp.quit()
			result = True
		except Exception as e:
			print(e)		
		return result

