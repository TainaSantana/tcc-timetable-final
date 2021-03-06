import random as rnd
import prettytable
from professores.models import Professor
from disciplinas.models import Disciplina
from salas.models import Sala


class Professor:
    def __init__(self, id, nome):
        self._id = id
        self._nome = nome

    def get_id(self):
        return self._id

    def get_nome(self):
        return self._nome

    def __str__(self):
        return self._nome


class Disciplina:
    def __init__(self, sigla, nome, professores, sem):
        self._sigla = sigla
        self._nome = nome
        self._professores = professores
        self._sem = sem

    def get_sigla(self):
        return self._sigla

    def get_nome(self):
        return self._nome

    def get_professores(self):
        return self._professores

    def get_sem(self):
        return self._sem

    def __str__(self): return self._nome


class DiasAula:
    def __init__(self, dias):
        self._dias = dias

    def get_dias(self):
        return self._dias

    def __str__(self):
        return self._dias


class HorarioAula:
    def __init__(self, id, horario):
        self._id = id
        self._horario = horario

    def get_id(self):
        return self._id

    def get_horario(self):
        return self._horario


class Sala:
    def __init__(self, nome, capacidade):
        self._nome = nome
        self._capacidade = capacidade

    def get_nome(self):
        return self._nome

    def get_capacidade(self):
        return self._capacidade


# classe que representa o curso a ser otimizado
class Curso:

    def __init__(self, nome, disciplinas, n_alunos):
        self._nome = nome
        self._disciplinas = disciplinas
        self._n_alunos = n_alunos

    def get_nome(self): return self._nome

    def get_disciplinas(self): return self._disciplinas

    def get_n_alunos(self): return self._n_alunos


class Classe:
    def __init__(self, id, curso, disciplina, horario_aula, dias_aula):
        self._horario_aula = horario_aula
        self._id = id
        self._curso = curso
        self._disciplina = disciplina
        self._dias_aula = dias_aula
        self._professor = None
        self._horarioAula = None
        self._sala = None


    def get_id(self):
        return self._id

    def get_curso(self):
        return self._curso

    def get_disciplina(self):
        return self._disciplina

    def get_dias_aula(self):
        return self._dias_aula

    def get_professor(self):
        return self._professor

    def get_horario_aula(self):
        return self._horario_aula

    def get_sala(self):
        return self._sala

    def set_professor(self, professor):
        self._professor = professor

    def set_sala(self, sala):
        self._sala = sala


    def __str__(self):
        return str(self._curso.get_nome()) + "," + str(self._disciplina.get_sigla()) + "," \
               + str(self._sala.get_nome()) + "," \
               + str(self._professor.get_nome()) + "," \
               + str(self._horario_aula.get_id()) + "," \
               + str(self._disciplina.get_sem()) + "," \
               + str(self._dias_aula.get_dias()) + "," \



class Dados:
    def __init__(self):
        salas = Sala.objects.all().values('nome', 'capacidade')
        horarios_aulas = [
            ["1 Hor??rio", "19:00 ??? 19:50"],
            ["2 Hor??rio", "19:50 ??? 20:40"],
            ["3 Hor??rio", "21:00 ??? 21:50"],
            ["4 Hor??rio", "21:50 ??? 22:35"]
        ]
        professores = Professor.objects.all().values('nome')

        dias_aula = ["SEG", "TER", "QUA", "QUI", "SEX"]

        self._salas = []
        self._horarios_aulas = []
        self._professores = []
        self._dias_aula = []

        self.fill_objects(salas, horarios_aulas, professores, dias_aula)

        self._disciplinas = Disciplina.objects.all().values('nome', 'professor', 'semestre')

        self._cursos = Disciplina.objects.all().values('nome', 'categoria')

    def get_professores(self):
        return self._professores

    def get_salas(self):
        return self._salas

    def get_disciplinas(self):
        return self._disciplinas

    def get_cursos(self):
        return self._cursos

    def get_horarios_aulas(self):
        return self._horarios_aulas

    def get_dias_aula(self):
        return self._dias_aula

    def fill_objects(self, salas, horarios_aulas, professores, dias_aula):
        for i in range(0, len(salas)):
            self._salas.append(Sala(salas[i][0], salas[i][1]))
        for i in range(0, len(horarios_aulas)):
            self._horarios_aulas.append(HorarioAula(horarios_aulas[i][0], horarios_aulas[i][1]))
        for i in range(0, len(professores)):
            self._professores.append(Professor(professores[i][0], professores[i][1]))
        for i in range(0, len(dias_aula)):
            self._dias_aula.append(DiasAula(dias_aula[i][0]))

    def get_professor(self, nome):
        return next((professor for professor in self._professores if professor.get_id() == nome), None)


class Schedule:
    def __init__(self, data):
        self._data = data
        self._classes = []
        self._num_de_conflitos = 0
        self._fitness = 0  # inicializa a nota da avaliacao com valor 0
        self._classNumb = 0  # realiza o controle do n??mero de classes/turmas

    def get_classes(self):

        return self._classes

    # ira obter o numero de conflitos a cada gera????o
    def get_num_de_conflitos(self):
        return self._num_de_conflitos

    # funcao de calculo de aptid??o
    def get_fitness(self):

        self._fitness = self.calculate_fitness()

        return self._fitness

    # incializa a popula????o com as informa????es das disciplinas, salas e professores e gerar novas turmas
    def initialize(self):
        cursos = self._data.get_cursos()
        diasaula = self._data.get_dias_aula()
        for i in range(0, len(cursos)):
            disciplinas = cursos[i].get_disciplinas()
            dias = diasaula[i].get_dias()
            for j in range(0, len(disciplinas)):
                for k in range(0, len(dias)):
                    novo_horario_aula = self._data.get_horarios_aulas()[
                        rnd.randrange(0, len(self._data.get_horarios_aulas()))]
                    dias_aula = self._data.get_dias_aula()[rnd.randrange(0, len(self._data.get_dias_aula()))]
                    # dias_aula = self._data.get_restricoes()[rnd.randrange(0, len(self._data.get_restricoes()))]
                    nova_classe = Classe(self._classNumb, cursos[i], disciplinas[j], novo_horario_aula, dias_aula)

                self._classNumb += 1

                nova_classe.set_sala(self._data.get_salas()[rnd.randrange(0, len(self._data.get_salas()))])

                nova_classe.set_professor(
                    disciplinas[j].get_professores()[rnd.randrange(0, len(disciplinas[j].get_professores()))])

                self._classes.append(nova_classe)
        return self

    # calcula aptidao dos individuos
    def calculate_fitness(self):
        self._num_de_conflitos = 0
        classes = self.get_classes()
        for i in range(0, len(classes)):
            capacidade = classes[i].get_sala().get_capacidade()
            n_alunos = classes[i].get_curso().get_n_alunos()
            # sem = classes[i].get_disciplinas().get_sem()
            # valida se a capacidade da sala ?? menor do que a quantidade de alunos
            if capacidade < n_alunos:
                self._num_de_conflitos += 1
            for j in range(0, len(classes)):
                if j >= i:
                    if (classes[i].get_horario_aula() == classes[j].get_horario_aula() and
                            classes[i].get_id() != classes[j].get_id()):
                        if classes[i].get_sala() == classes[
                            j].get_sala():  # valida a sala ter?? 2 classes simultaneamente
                            self._num_de_conflitos += 1
                        if classes[i].get_professor() == classes[
                            j].get_professor():  # valida se o professor tem aula com duas classes no mesmo hor??rio
                            self._num_de_conflitos += 1
                        if classes[i].get_professor() == classes[i].get_sala() and classes[j].get_professor() == \
                                classes[j].get_sala():
                            self._num_de_conflitos += 1
                        if classes[i].get_disciplina() == classes[j].get_disciplina() and classes[i].get_dias_aula() == \
                                classes[
                                    j].get_dias_aula():  # valida se disciplinas de diferentes semestres ser??o ministradas no mesmo hor??rio
                            self._num_de_conflitos += 1


        return 1 / (1.0 * self._num_de_conflitos + 1)

    def __str__(self):
        return_value = ""
        for i in range(0, len(self._classes) - 1):
            return_value += str(self._classes[i]) + " | "
        return_value += str(self._classes[len(self._classes) - 1])
        return return_value


NUMBER_OF_ELITE = 1  # individuo com melhor aptidao
TOURNAMENT_SELECTION_SIZE = 3
MUTATION_RATE = 0.2  # taxa de mutacao
POPULATION_SIZE = 3  # tamanho da populacao


# populacao de individuos (representado pelos poss??veis horarios (schedules))
class Population:
    def __init__(self, population_size, data):
        self._population_size = population_size  # tamanho da populacao
        self._data = data  # dados do curso
        self._schedules = []  # lista de individulos (horarios) da populacao
        # dado o tamanho da populacao, instanciamos os horarios e chamamos o metodo de inicializacao da populacao
        for i in range(0, population_size):
            self._schedules.append(Schedule(data).initialize())

    def get_schedules(self): return self._schedules


class GeneticAlgorithm:
    def __init__(self, data):
        self._data = data

    # metodo publico que chama a mutacao de populacao e o cruzamento de populacao
    def evolve(self, population):
        return self._mutate_population(self._crossover_population(population))

    # faz o cruzamento de todos os indiv??duos (hor??rios) da popula????o
    def _crossover_population(self, population):
        crossover_population = Population(0, self._data)
        for i in range(NUMBER_OF_ELITE):
            crossover_population.get_schedules().append(population.get_schedules()[i])
        i = NUMBER_OF_ELITE
        while i < POPULATION_SIZE:
            schedule1 = self._select_tournament_population(population).get_schedules()[0]
            schedule2 = self._select_tournament_population(population).get_schedules()[0]
            crossover_population.get_schedules().append(self._crossover_schedule(schedule1, schedule2))
            i += 1
        return crossover_population

    # m??otodo de sele????o por torneio dos individuos (horarios) para fazer cruzamento
    def _select_tournament_population(self, pop):
        tournament_population = Population(0, self._data)
        # pega 3 individuos (horarios) e fazemos a classificacao, retornamos a populacao de 3 individuos ordenados
        for i in range(TOURNAMENT_SELECTION_SIZE):
            tournament_population.get_schedules().append(pop.get_schedules()[rnd.randrange(0, POPULATION_SIZE)])
        tournament_population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        return tournament_population

    # metodo que faz o cruzamento dos dois individuos (horarios)
    def _crossover_schedule(self, schedule1, schedule2):
        crossover_schedule = Schedule(self._data).initialize()
        for i in range(0, len(crossover_schedule.get_classes())):
            if rnd.random() > 0.5:  # a depender do valor aleat??rio escolhemos a classe 1 ou 2
                crossover_schedule.get_classes()[i] = schedule1.get_classes()[i]
            else:
                crossover_schedule.get_classes()[i] = schedule2.get_classes()[i]
        return crossover_schedule

    # faz a mutacao em todos os individuos da populacao
    def _mutate_population(self, population):
        for i in range(NUMBER_OF_ELITE, POPULATION_SIZE):
            self._mutate_schedule(population.get_schedules()[i])
        return population

    # m??todo faz a mutacao do horario antes, ent??o se o n??mero aleat??rio for menor ou igual ?? taxa de muta????o
    # ent??o fazemos a muta????o e pegamos as classes desta programa????o rec??m-criada
    def _mutate_schedule(self, mutate_schedule):
        schedule = Schedule(self._data).initialize()
        for i in range(0, len(mutate_schedule.get_classes())):
            if MUTATION_RATE > rnd.random():  # taxa de mutacao
                mutate_schedule.get_classes()[i] = schedule.get_classes()[i]
        return mutate_schedule


def exibe_disciplinas(cursos):
    tabela_disciplinas = prettytable.PrettyTable(['Disciplina', 'Professor(a)'])
    for i in range(0, len(cursos)):
        professores = cursos[i].get_professores()
        temp_str = ""
        for j in range(0, len(professores) - 1):
            temp_str += str(professores[j]) + " | "
        temp_str += str(professores[len(professores) - 1])
        tabela_disciplinas.add_row(
            [cursos[i].get_nome(), temp_str])
    print(tabela_disciplinas)


def exibe_professores(professores):
    tabela_professores = prettytable.PrettyTable(['C??digo', 'Nome do(a) Professor(a)'])
    for i in range(0, len(professores)):
        tabela_professores.add_row([professores[i].get_id(), professores[i].get_nome()])
    print(tabela_professores)


def exibe_horarios_aulas(horarios_aulas):
    tabela_horarios_aulas = prettytable.PrettyTable(['Per??odo', 'Hor??rio'])
    for i in range(0, len(horarios_aulas)):
        tabela_horarios_aulas.add_row([horarios_aulas[i].get_id(), horarios_aulas[i].get_horario()])
    print(tabela_horarios_aulas)


def exibe_geracao(schedules):
    tabela_geracao = prettytable.PrettyTable(
        ['#', 'Fitness', 'Quantidade de Conflitos', 'Classe [Curso, Disciplina, Sala, Professor(a), Per??odo]'])

    for i in range(0, len(schedules)):
        tabela_geracao.add_row([str(i), round(schedules[i].get_fitness(), 3), schedules[i].get_num_de_conflitos(),
                                schedules[i]])
    print(tabela_geracao)


def exibe_sala(salas):
    tabela_salas = prettytable.PrettyTable(['Sala', 'Capacidade'])
    for i in range(0, len(salas)):
        tabela_salas.add_row([str(salas[i].get_nome()), str(salas[i].get_capacidade())])
    print(tabela_salas)

def exibe_horario(schedule):  # print_schedule_as_table
    classes = schedule.get_classes()
    tabela_horario = prettytable.PrettyTable(
        ['Dia Semana', 'Turma (N. alunos)', 'Curso (Sigla)', 'Semestre', 'Sala (Capacidade)', 'Professor (C??digo)',
         'Hor??rio'])
    for i in range(0, len(classes)):
        tabela_horario.add_row([
            str(classes[i].get_dias_aula().get_dias()),
            classes[i].get_curso().get_nome() + " (" +
            str(classes[i].get_curso().get_n_alunos()) + ")",

            classes[i].get_disciplina().get_nome(),

            classes[i].get_disciplina().get_sem(),

            classes[i].get_sala().get_nome() + " (" + str(
                classes[i].get_sala().get_capacidade()) + ")",

            classes[i].get_professor().get_nome(),

            classes[i].get_horario_aula().get_horario() + " (" + str(
                classes[i].get_horario_aula().get_id()) + ")"
        ])
    print(tabela_horario)


def exibe_populacao_atual(population, generation_number):
    print("\n> Gera????o # " + str(generation_number))
    exibe_geracao(population.get_schedules())
    exibe_horario(population.get_schedules()[0])


def exibe_estatisticas(generation_number, data):
    print("\n")
    print("Quantidade de gera????es: " + str(generation_number))
    print("-----------------------------------------------")
    print("INFORMA????ES GERAIS")
    print("Quantidade de professores: " + str(len(data.get_professores())))
    print("Categoria de disciplinas (quantidade): " + str(len(data.get_cursos())))
    print("Quantidade de disciplinas: " + str(len(data.get_disciplinas())))
    print("-----------------------------------------------")
    print("PAR??METROS DO ALGORITMO GEN??TICO")
    print("NUMBER_OF_ELITE: " + str(NUMBER_OF_ELITE))
    print("TOURNAMENT_SELECTION_SIZE: " + str(TOURNAMENT_SELECTION_SIZE))
    print("Taxa de muta????o: " + str(MUTATION_RATE))
    print("Tamanho da Popula????o: " + str(POPULATION_SIZE))
    print("--")


def exibe_dados_disponiveis(data):
    print("> Informa????es: ")
    # exibe_cursos(data.get_cursos())
    exibe_disciplinas(data.get_disciplinas())
    exibe_professores(data.get_professores())
    exibe_sala(data.get_salas())
    exibe_horarios_aulas(data.get_horarios_aulas())


def main():
    data = Dados()  # instancia a classe de dados
    exibe_dados_disponiveis(data)  # instancia o metodo que contem todos os dados do curso e das grades geradas

    generation_number = 0  # inicializa o numero de geracoes
    conflitos = []

    population = Population(POPULATION_SIZE, data)  # instancia a classe de populacao

    geneticAlgorithm = GeneticAlgorithm(data)

    # la??o onde exibimos a popula????o onde o horario mais adequado tem zero conflitos
    while population.get_schedules()[0].get_fitness() != 1.0:
        generation_number += 1  # incrementa o numero da geracao
        population = geneticAlgorithm.evolve(
            population)  # chama o metodo publico do algoritmo genetico que retorna a mutacao e o cruzamento
        population.get_schedules().sort(key=lambda x: x.get_fitness(),
                                        reverse=True)  # ordena em ordem inversa o resultado das avalia????es

        exibe_populacao_atual(population, generation_number)  # exibe a populacao atual
        conflitos.append(population.get_schedules()[0].get_num_de_conflitos())
    exibe_estatisticas(generation_number, data)


if __name__ == '__main__':
    main()
