CONFIRM_EMAIL = """
	<html>

	<body style="background-color:#e2e1e0;font-family: Open Sans, sans-serif;font-size:100%;font-weight:400;line-height:1.4;color:#000;">
	  <table style="max-width:670px;margin:50px auto 10px;background-color:#fff;padding:50px;-webkit-border-radius:3px;-moz-border-radius:3px;border-radius:3px;-webkit-box-shadow:0 1px 3px rgba(0,0,0,.12),0 1px 2px rgba(0,0,0,.24);-moz-box-shadow:0 1px 3px rgba(0,0,0,.12),0 1px 2px rgba(0,0,0,.24);box-shadow:0 1px 3px rgba(0,0,0,.12),0 1px 2px rgba(0,0,0,.24); border-top: solid 10px blue;">
	    <thead>
	    	<tr>
	    		<td colspan="2" style="font-size:19px;padding:0px 15px 10px 25%;">Activación de cuenta</td>
	    	</tr>
	    <tbody>
	      <tr>
	        <td style="height:35px;"></td>
	      </tr>
	      <tr>
	        <td colspan="2" style="padding:10px 20px;">
	          <p style="font-size:14px;margin:0 0 6px 0;">
	            <span style="font-weight:bold;display:inline-block;min-width:150px">
	              Hola $(username), Gracias por confiar en nosotros. Te damos la bienvenida a nuestra plataforma. <br>Has click en este <a href="$(url)">ENLACE</a> para activar tu cuenta.
	            </span>
	          </p>
	        </td>
	      </tr>
	      <tr>
	        <td style="width:50%;padding:20px;vertical-align:top">
	        </td>
	      </tr>
	    </tbody>
	    <tfooter>
	      <tr>
	        <td colspan="2" style="font-size:14px;padding:50px 15px 0 15px;">
	          <strong style="display:block;margin:0 0 10px 0;">SELAH COMFORT</strong><br> Medellín - Colombia<br><br>
	          <!-- <b>Phone:</b> 03552-222011<br> -->
	          <b>Email:</b> support@selahcomfort.com
	        </td>
	      </tr>
	    </tfooter>
	  </table>
	</body>

	</html>
"""