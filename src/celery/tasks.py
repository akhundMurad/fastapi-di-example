from src.services.mails import MailsService


def send_mail(service: MailsService) -> None:
    service.send_mail()
