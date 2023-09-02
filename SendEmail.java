import java.util.*;
import javax.mail.*;
import javax.mail.internet.*;

public class SendEmail {
    public static void main(String[] args) {
        // Set up the email properties
        Properties props = new Properties();
        props.put("mail.smtp.host", "smtp.gmail.com");
        props.put("mail.smtp.port", "587");
        props.put("mail.smtp.auth", "true");
        props.put("mail.smtp.starttls.enable", "true");

        // Set up the credentials for the email account you will be using to send the email
        String username = "testtest6235@gmail.com";
        String password = "tykvbelgoxpjesew";

        // Set up the session and message
        Session session = Session.getInstance(props, new Authenticator() {
            @Override
            protected PasswordAuthentication getPasswordAuthentication() {
                return new PasswordAuthentication(username, password);
            }
        });
        Message message = new MimeMessage(session);

        try {
            // Set the recipients of the email
            message.setFrom(new InternetAddress(username));
            message.setRecipients(Message.RecipientType.TO, InternetAddress.parse("customer_email@example.com"));

            // Set the subject and body of the email
            message.setSubject("Grocery Bill");
            message.setText("Here is your grocery bill as requested. Thank you for shopping with us!");

            // Attach the bill to the email
            MimeBodyPart billAttachment = new MimeBodyPart();
            billAttachment.attachFile("path/to/grocery_bill.pdf");
            MimeMultipart multipart = new MimeMultipart();
            multipart.addBodyPart(billAttachment);
            message.setContent(multipart);

            // Send the email
            Transport.send(message);
            System.out.println("Email sent successfully!");
        } catch (MessagingException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
