from django.core.mail import send_mail

def send_confirmation_email(user, confirmation_link):
    subject = "Подтверждение регистрации"
    message = """
    **Приветствуем, {{ user.username }}!**

    **Вы успешно зарегистрировались на нашем сайте.**

    **Для активации вашего аккаунта, пожалуйста, перейдите по ссылке:**

    {{ confirmation_link }}

    **Если вы не перейдете по ссылке в течение 24 часов, ваша регистрация будет аннулирована.**

    **С уважением,**

    **Команда [myproject1]**
    """.format(user=user, confirmation_link=confirmation_link)
    send_mail(subject, message, "[zhumausupbek@gmail.com]", [user.email], fail_silently=False)


def send_reset_password_email(user, reset_link):
    subject = "Сброс пароля"
    message = """
    **Приветствуем, {{ user.username }}!**

    **Мы получили запрос на сброс пароля для вашего аккаунта на [название вашего сайта].**

    **Чтобы сбросить пароль, пожалуйста, перейдите по ссылке:**

    {{ reset_link }}

    **Если вы не перейдете по ссылке в течение 24 часов, ваш запрос на сброс пароля будет аннулирован.**

    **С уважением,**

    **Команда [myproject1]**
    """.format(user=user, reset_link=reset_link)
    send_mail(subject, message, "[zhumausupbek@gmail.com]", [user.email], fail_silently=False)

