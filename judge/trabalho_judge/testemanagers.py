from django.db import models
from django.db.models import Q, F, Count, Avg, Min, Max
from django.utils import timezone
from datetime import timedelta


class PerfilManager(models.Manager):

    # 01 → perfis premium de um país nos últimos N dias
    def premium_recentes_do_pais(self, pais, dias):
        limite = timezone.now() - timedelta(days=dias)
        return self.filter(premium=True, pais=pais, criado__gte=limite)

    # 02 → perfis que falam pt-BR e estão no top 100
    def ptbr_top100(self):
        return self.filter(linguagem="pt-BR", ranking__lte=100)

    # 03 → treinadores OU premium com muitos resolvidos
    def treinadores_ou_premium_com_muitos_resolvidos(self, x):
        return self.filter(
            Q(treinador=True) | Q(premium=True),
            resolvidos__gte=x
        )

    # 04 → submetidos maior que resolvidos
    def com_submetidos_maior_que_resolvidos(self):
        return self.filter(submetidos__gt=F('resolvidos'))

    # 05 → usernames de uma instituição com prefixo específico
    def usernames_da_instituicao_com_prefixo(self, inst, prefixo):
        return list(
            self.filter(instituicao=inst, username__startswith=prefixo)
            .values_list('username', flat=True)
        )

    # 07 → perfis sem submissões recentes
    def sem_submissoes_recentes(self, dias):
        limite = timezone.now() - timedelta(days=dias)
        return self.exclude(submissao__data__gte=limite)

    # 08 → quantidade de perfis premium por país
    def paises_com_mais_premium(self):
        return self.filter(premium=True).values('pais').annotate(total=Count('id'))

    # 09 → resumo: melhor, pior ranking e média de resolvidos
    def resumo_ranking_dos_premium(self):
        return self.filter(premium=True).aggregate(
            melhor=Min('ranking'),
            pior=Max('ranking'),
            media=Avg('resolvidos')
        )

    # 10 → perfis oficiais em competições ativas
    def oficiais_em_competicoes_ativas(self):
        agora = timezone.now()
        return self.filter(
            participacao__oficial=True,
            participacao__competicao__inicio__lte=agora,
            participacao__competicao__fim__gte=agora
        ).distinct()


class ProblemaManager(models.Manager):

    # 11 → problemas públicos em pt-BR com dificuldade mínima
    def publicos_ptbr_a_partir_de_dificuldade(self, nivel):
        return self.filter(publico=True, linguagem="pt-BR", dificuldade__gte=nivel)

    # 12 → problemas dentro de intervalo de tempo e memória
    def por_intervalo_de_tempo_e_memoria(self, t_min, t_max, m_min, m_max):
        return self.filter(
            tempo__range=(t_min, t_max),
            memoria__range=(m_min, m_max)
        )

    # 13 → busca por título OU categoria
    def por_titulo_ou_categoria(self, termo, categorias):
        return self.filter(
            Q(titulo__icontains=termo) | Q(categoria__in=categorias)
        )

    # 14 → problemas com linguagens ativas específicas
    def com_linguagens_ativas(self, slugs):
        return self.filter(linguagens__slug__in=slugs, linguagens__ativa=True).distinct()

    # 15 → problemas com mínimo de submissões
    def com_minimo_de_aceites(self, x):
        return self.annotate(total=Count('submissao')).filter(total__gte=x)

    # 16 → mais AC do que WA
    def com_mais_aceites_que_wrong_answer(self):
        return self.annotate(
            ac=Count('submissao', filter=Q(submissao__status='AC')),
            wa=Count('submissao', filter=Q(submissao__status='WA'))
        ).filter(ac__gt=F('wa'))

    # 17 → problemas sem exemplos
    def sem_exemplos(self):
        return self.filter(exemplo__isnull=True)

    # 20 → lista de códigos por categoria pública
    def codigos_por_categoria_publica(self, categoria):
        return list(
            self.filter(publico=True, categoria=categoria)
            .values_list('codigo', flat=True)
        )

    # 21 → distribuição de problemas por dificuldade
    def distribuicao_publicos_por_dificuldade(self):
        return self.filter(publico=True).values('dificuldade').annotate(total=Count('id'))

    # 22 → resumo de notas (média, max, min)
    def resumo_de_notas_publicas_ptbr(self):
        return self.filter(publico=True, linguagem="pt-BR").aggregate(
            media=Avg('nota'),
            max=Max('nota'),
            min=Min('nota')
        )


class SubmissaoManager(models.Manager):

    # 26 → submissões recentes em fila ou execução
    def em_fila_ou_execucao_recentes(self):
        limite = timezone.now() - timedelta(hours=1)
        return self.filter(
            Q(status='QUEUE') | Q(status='RUNNING'),
            data__gte=limite
        )

    # 27 → submissões aceitas em linguagem e ano
    def aceitas_na_linguagem_no_ano(self, linguagem, ano):
        return self.filter(
            status='AC',
            linguagem=linguagem,
            data__year=ano
        )

    # 28 → wrong answer em problemas difíceis e públicos
    def wrong_answer_em_problemas_dificeis_publicos(self):
        return self.filter(
            status='WA',
            problema__dificuldade='DIFICIL',
            problema__publico=True
        )

    # 32 → submissões com erro e log preenchido
    def com_log_e_status_problematico(self):
        return self.filter(
            log__isnull=False
        ).exclude(status='AC')

    # 33 → distribuição de status por problema
    def distribuicao_por_status_do_problema(self, problema):
        return self.filter(problema=problema).values('status').annotate(total=Count('id'))

    # 34 → média de tempo por linguagem
    def media_tempo_por_linguagem_em_problema(self, problema):
        return self.filter(
            problema=problema,
            status='AC'
        ).values('linguagem').annotate(media=Avg('tempo'))


class CompeticaoManager(models.Manager):

    # 41 → competições ativas agora
    def ativas_agora(self):
        agora = timezone.now()
        return self.filter(inicio__lte=agora, fim__gte=agora, publico=True)

    # 42 → competições futuras públicas com freeze
    def futuras_publicas_com_freeze(self):
        agora = timezone.now()
        return self.filter(inicio__gt=agora, publico=True, freeze__isnull=False)

    # 43 → competições com freeze antes do fim
    def freeze_antes_do_termino(self):
        return self.filter(freeze__lt=F('fim'))

    # 44 → competições com mínimo de participantes
    def com_minimo_participantes_oficiais(self, n):
        return self.annotate(total=Count('participacao')).filter(total__gte=n)