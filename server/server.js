const http = require("http");
const bodyParser = require("body-parser");
const express = require("express");
const nodemailer = require("nodemailer");

// Generate test SMTP service account from ethereal.email
// Only needed if you don't"nodemailer" mail account for testing

const app = express();
const port = 3000;

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.get("/content/:content", (req, res, next) => { // eslint-disable-line
  console.log(req.params.content); // eslint-disable-line
  nodemailer.createTestAccount(() => {
    // create reusable transporter object using the default SMTP transport
    const transporter = nodemailer.createTransport({
      host: "smtp.gmail.com",
      port: 587,
      secure: false, // true for 465, false for other ports
      auth: {
        user: "acristhebestman@gmail.com",
        pass: "?ThisIsMyPass18"
      }
    });

    // setup email data with unicode symbols
    const mailOptions = {
      from: "acristhebestman@gmail.com", // sender address
      to: "pmnet@free.fr", // list of receivers
      subject: "Hello", // Subject line
      text: "heyhey", // plain text body
      html: "<b>Hello world?</b>" // html body
    };

    // send mail with defined transport object
    transporter.sendMail(mailOptions, (error, info) => {
      if (error) {
        return console.log(error); // eslint-disable-line
      }
      console.log("Message sent: %s", info.messageId); // eslint-disable-line
      // Preview only available when sending through an Ethereal account
      console.log("Preview URL: %s", nodemailer.getTestMessageUrl(info)); // eslint-disable-line

      // Message sent: <b658f8ca-6296-ccf4-8306-87d57a0b4321@example.com>
      // Preview URL: https://ethereal.email/message/WaQKMgKddxQDoou...
      return null;
    });
  });

  return res.status(200);
});

app.get("/", (req, res, next) => { // eslint-disable-line
  nodemailer.createTestAccount(() => {
    // create reusable transporter object using the default SMTP transport
    const transporter = nodemailer.createTransport({
      host: "smtp.gmail.com",
      port: 587,
      secure: false, // true for 465, false for other ports
      auth: {
        user: "acristhebestman@gmail.com",
        pass: "?ThisIsMyPass18"
      }
    });

    // setup email data with unicode symbols
    const mailOptions = {
      from: "acristhebestman@gmail.com", // sender address
      to: "bobsender87@gmail.com", // list of receivers
      subject: "Hello", // Subject line
      text: "", // plain text body
      html: { path: "./public/fake.html" } // html body
    };

    // send mail with defined transport object
    transporter.sendMail(mailOptions, (error, info) => {
      if (error) {
        return console.log(error); // eslint-disable-line
      }
      console.log("Message sent: %s", info.messageId); // eslint-disable-line
      // Preview only available when sending through an Ethereal account
      console.log("Preview URL: %s", nodemailer.getTestMessageUrl(info)); // eslint-disable-line

      // Message sent: <b658f8ca-6296-ccf4-8306-87d57a0b4321@example.com>
      // Preview URL: https://ethereal.email/message/WaQKMgKddxQDoou...
      return null;
    });
  });

  return res.status(200).json({ key: "hey" });
});

const server = http.createServer(app);

server.listen(port, () => {
  console.log(`server listening on port ${port}`); // eslint-disable-line
});
