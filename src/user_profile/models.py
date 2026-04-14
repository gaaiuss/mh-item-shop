from typing import TYPE_CHECKING

from django.contrib.auth.models import User
from django.db import models
from django.forms import ValidationError

from utils.validate import validate_cep, validate_cpf

if TYPE_CHECKING:
    from django.core.exceptions import ValidationErrorMessageArg


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField()
    cpf = models.CharField(max_length=11, verbose_name="CPF")
    address = models.CharField()
    number = models.CharField()
    complement = models.CharField()
    neighborhood = models.CharField()
    cep = models.CharField(verbose_name="CEP")
    city = models.CharField()
    state = models.CharField(
        max_length=2,
        default="SP",
        choices=(
            ("AC", "Acre"),
            ("AL", "Alagoas"),
            ("AP", "Amapá"),
            ("AM", "Amazonas"),
            ("BA", "Bahia"),
            ("CE", "Ceará"),
            ("DF", "Distrito Federal"),
            ("ES", "Espírito Santo"),
            ("GO", "Goiás"),
            ("MA", "Maranhão"),
            ("MT", "Mato Grosso"),
            ("MS", "Mato Grosso do Sul"),
            ("MG", "Minas Gerais"),
            ("PA", "Pará"),
            ("PB", "Paraíba"),
            ("PR", "Paraná"),
            ("PE", "Pernambuco"),
            ("PI", "Piauí"),
            ("RJ", "Rio de Janeiro"),
            ("RN", "Rio Grande do Norte"),
            ("RS", "Rio Grande do Sul"),
            ("RO", "Rondônia"),
            ("RR", "Roraima"),
            ("SC", "Santa Catarina"),
            ("SP", "São Paulo"),
            ("SE", "Sergipe"),
            ("TO", "Tocantins"),
        ),
    )

    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"

    def clean(self) -> None:
        error_messages: ValidationErrorMessageArg = {}

        if not validate_cpf(self.cpf):
            error_messages["cpf"] = "Type a valid CPF"

        if not validate_cep(self.cep):
            error_messages["cep"] = "Type a valid CEP"

        if error_messages:
            raise ValidationError(error_messages)
