from datetime import datetime,timedelta

class Data:
    def __init__(self):
        self.momento = datetime.today()

    def __str__(self):
        return self.formata()

    def mes(self):
        meses_ano=["Janeiro", "Fevereiro", "Março", "Abril", "Maio","Junho","Julho","Agosto","Setembro","Outubro", "Novembro","Dezembro"]
        mes_cadastro = self.momento.month
        return meses_ano[mes_cadastro - 1]

    def dia_semana(self):
        dias_semana=["Domingo", "Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira","Sexta-Feira","Sábado"]
        dia_semana = self.momento.weekday() + 1
        return dias_semana[dia_semana]

    def formata(self):
        formatado = self.momento.strftime(f"%d/%m/%Y %H:%M")
        return formatado

    def tempo(self):
        tempo_cadastro = (datetime.today() - timedelta(days=30)) - self.momento
        return tempo_cadastro