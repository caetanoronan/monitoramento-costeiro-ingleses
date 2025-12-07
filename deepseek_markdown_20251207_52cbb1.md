# PROJETO DE PESQUISA E EXTENSÃO
## Monitoramento Aerofotogramétrico da Dinâmica Costeira:
### Alargamento Artificial da Orla e Avanço das Dunas Urbanas - Praia dos Ingleses, Florianópolis/SC

**Instituição Proponente:** Instituto Federal de Santa Catarina - Campus Florianópolis  
**Área Temática:** Geotecnologias Aplicadas ao Meio Ambiente e Ordenamento Territorial  
**Vigência:** 12 meses  
**Data:** [DATA DE SUBMISSÃO]

---

### 1. RESUMO EXECUTIVO

Este projeto propõe a execução de um levantamento aerofotogramétrico sistemático para monitorar a dinâmica costeira na Praia dos Ingleses, Florianópolis/SC. Com base institucional no IFSC-Campus Florianópolis, o estudo tem como objetivos principais: (1) avaliar a estabilidade morfológica e a eficácia do alargamento artificial da faixa de areia executado recentemente; e (2) monitorar a taxa de avanço do campo dunar frontal sobre a área urbana consolidada.

A metodologia empregará Veículos Aéreos Não Tripulados (VANTs/Drones) para aquisição de imagens de ultra-alta resolução, processadas através de técnicas de Fotogrametria e Visão Computacional (Structure from Motion - SfM). Serão gerados produtos geoespaciais quantitativos, como Modelos Digitais de Superfície (MDS), ortomosaicos georreferenciados e mapas de diferença de volume (DoD), que permitirão uma análise precisa das mudanças sazonais e anuais.

Além do caráter técnico-científico, o projeto possui forte componente de extensão e capacitação, integrando alunos de graduação e pós-graduação em todas as etapas. Os resultados fornecerão subsídios técnicos fundamentais para a gestão municipal, defesa civil e planejamento urbano, servindo como um estudo de caso paradigmático para o monitoramento costeiro com tecnologias acessíveis.

**Palavras-chave:** Fotogrametria com Drone; Monitoramento Costeiro; Dinâmica de Dunas; Gestão de Zona Costeira; Geotecnologias; IFSC.

---

### 2. INTRODUÇÃO E JUSTIFICATIVA

A Praia dos Ingleses, localizada no nordeste da Ilha de Santa Catarina, representa um dos principais polos turísticos e de ocupação urbana do município de Florianópolis. Nas últimas décadas, a região tem enfrentado desafios complexos relacionados à erosão costeira e à mobilidade de dunas, agravados por eventos climáticos extremos e pela pressão antrópica.

Recentemente, foi executada uma obra de engordamento (alargamento artificial) da faixa de areia, uma intervenção destinada a proteger a orla e o patrimônio urbano. Paralelamente, o campo dunar natural, cuja mobilidade é parte essencial da dinâmica do ecossistema, apresenta avanços sobre a infraestrutura urbana, gerando riscos e conflitos.

Diante deste cenário, faz-se imperativo um monitoramento técnico, preciso e contínuo para:
1.  **Avaliar o Retorno do Investimento Público:** Quantificar a permanência e a redistribuição do sedimento depositado na obra de alargamento.
2.  **Gerir Riscos:** Entender os padrões de avanço dunar para subsidiar ações de defesa civil e planejamento.
3.  **Produzir Conhecimento:** Gerar dados científicos de base para futuras intervenções e políticas públicas.
4.  **Capacitar Profissionais:** Oferecer aos alunos do IFSC experiência prática em um projeto real de Geotecnologia aplicada ao Meio Ambiente.

O uso de VANTs se apresenta como a ferramenta mais viável técnica e economicamente para este fim, permitindo aquisições frequentes de dados de alta resolução com relativo baixo custo e flexibilidade operacional.

---

### 3. OBJETIVOS

#### 3.1. Objetivo Geral
Realizar o monitoramento aerofotogramétrico da orla da Praia dos Ingleses para quantificar e analisar a evolução morfológica da faixa de areia artificialmente alargada e a dinâmica de avanço do campo dunar frontal sobre a zona urbana adjacente.

#### 3.2. Objetivos Específicos
1.  Executar três campanhas aerofotogramétricas sistemáticas (linha de base, pós-inverno, pós-verão) cobrindo toda a área de interesse.
2.  Gerar ortomosaicos georreferenciados com resolução espacial igual ou superior a 3 cm/pixel.
3.  Elaborar Modelos Digitais de Superfície (MDS) texturizados e de alta precisão para cada campanha.
4.  Quantificar, através de mapas de diferença (DoD), os volumes de sedimento erosionados e depositados tanto na praia quanto nas dunas.
5.  Mapear a posição da linha de costa e da frente dunar em cada campanha, criando uma série temporal.
6.  Analisar a correlação entre os eventos meteorológicos/marégrafos (dados secundários) e as mudanças morfológicas observadas.
7.  Produzir um relatório técnico-científico final e artigos para divulgação dos resultados.
8.  Capacitar alunos do IFSC nas etapas de planejamento de voo, coleta de campo, processamento de dados e análise geoespacial.

---

### 4. METODOLOGIA

#### 4.1. Área de Estudo
A área de estudo compreende um trecho de aproximadamente 3 km da orla da Praia dos Ingleses, estendendo-se desde a linha de preamar até a área urbana consolidada imediatamente atrás do campo dunar frontal.

#### 4.2. Planejamento e Aquisição dos Dados
*   **Plataforma:** Drone de asa rotativa DJI Phantom 4 RTK (disponível no IFSC), garantindo precisão georreferenciada com correção cinemática pós-processada (PPK).
*   **Parâmetros de Voo:** Altura de voo ajustada para atingir GSD (Ground Sample Distance) ≤ 3 cm. Recobrimento longitudinal e lateral mínimo de 80% e 70%, respectivamente.
*   **Pontos de Controle no Solo (GCPs):** Serão implantados 15-20 alvos fixos ou semipermanentes distribuídos pela área. Suas coordenadas serão coletadas com receptor GNSS geodésico de dupla frequência (Topcon/Trimble).
*   **Cronograma de Campanhas:**
    *   **Campanha 1 (Mês 2):** Linha de base, imediatamente após a liberação do projeto.
    *   **Campanha 2 (Mês 7):** Pós-período de inverno (maior atividade de ondas).
    *   **Campanha 3 (Mês 10):** Pós-período de verão (maior intensidade de uso antrópico).

#### 4.3. Processamento e Análise
*   **Fotogrametria:** As imagens serão processadas no *software* Agisoft Metashape (licença educacional). O fluxo inclui alinhamento, georreferenciamento via GCPs, construção da nuvem de pontos densa, geração do MDS e do ortomosaico.
*   **Análise de Mudanças:** Os MDSs de campanhas diferentes serão comparados no módulo "Calcular Diferencial" do Metashape ou no QGIS, gerando um Modelo Digital de Diferença (DoD - *Difference of DSM*). Este mapa permitirá o cálculo volumétrico de perdas e ganhos de sedimentos.
*   **Análise Espacial em SIG:** No QGIS, serão digitalizadas as linhas de costa e frentes dunares para análise de deslocamento. Todos os dados serão integrados em um banco de dados geoespacial único.

---

### 5. EQUIPE EXECUTORA

| **Função** | **Nome/Cargo** | **Instituição** | **Atribuições** |
| :--- | :--- | :--- | :--- |
| **Coordenador** | Prof. Dr. [Nome] | IFSC - Florianópolis | Coordenação geral, responsabilidade técnica, relações institucionais, revisão final. |
| **Pesquisador Responsável** | [Nome - Mestrando/Doutorando] | IFSC/PGMAC | Execução do processamento avançado, análise de dados, redação de relatórios e artigos. |
| **Piloto/Técnico de Campo** | Técn. [Nome] | IFSC - Florianópolis | Operação do drone, manutenção de equipamentos, coleta de GCPs. |
| **Bolsista de Extensão I** | [Nome do Aluno] | IFSC - Curso [X] | Apoio em campo, organização de logística, processamento inicial de dados. |
| **Bolsista de Extensão II** | [Nome do Aluno] | IFSC - Curso [Y] | Suporte em SIG, geração de mapas temáticos, criação de visualizações. |

---

### 6. CRONOGRAMA DE EXECUÇÃO

*(Ver Planilha Anexa - Cronograma Detalhado)*

A execução do projeto está planejada para 12 meses, conforme síntese abaixo:

| **Atividade** | **Mês 1-2** | **Mês 3-4** | **Mês 5-6** | **Mês 7-8** | **Mês 9-10** | **Mês 11-12** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Planejamento e Licenças** | ● | | | | | |
| **Campanha 1 (Base)** | ● | | | | | |
| **Processamento Camp. 1** | | ● | ● | | | |
| **Análise Preliminar** | | | ● | | | |
| **Campanha 2 (Pós-Inverno)** | | | | ● | | |
| **Processamento/Análise Comp.** | | | | | ● | |
| **Campanha 3 (Pós-Verão)** | | | | | ● | |
| **Análise Final Integrada** | | | | | | ● |
| **Redação do Relatório Final** | | | | | | ● |
| **Divulgação dos Resultados** | | | | | | ● |

Legenda: ● = Período de execução principal.

---

### 7. PRODUTOS ESPERADOS E ENTREGAS

1.  **Produtos de Dados (Geoespaciais):**
    *   Banco de dados contendo 3 Ortomosaicos Georreferenciados (GeoTIFF).
    *   Banco de dados contendo 3 Modelos Digitais de Superfície (MDS) em formato LAZ e OBJ.
    *   2 Mapas de Diferença de Volume (DoD) entre campanhas (GeoTIFF + Relatório Volumétrico).
    *   Série temporal vetorial da linha de costa e da frente dunar (Shapefile).

2.  **Produtos de Conhecimento (Relatórios e Publicações):**
    *   **Relatório Técnico-Científico Final:** Documento abrangente (70-100 páginas) com toda a metodologia, resultados, discussão, conclusões e recomendações aos gestores.
    *   **Artigo Científico:** Preparado para submissão em periódico nacional da área de Geografia Física ou Geotecnologias.
    *   **Technical Paper/Resumo Expandido:** Para apresentação em evento científico (ex: Simpósio Brasileiro de Geomática).

3.  **Produtos de Extensão e Divulgação:**
    *   **Seminário de Resultados:** Apresentação aberta à comunidade acadêmica e representantes da Prefeitura de Florianópolis.
    *   **Pôster Científico:** Resumindo a metodologia e principais achados.
    *   **Visualizador 3D Online:** Link público para visualização interativa de um dos modelos gerados.

---

### 8. ORÇAMENTO (RESUMIDO)

*(Ver Planilha Anexa - Orçamento Detalhado)*

O projeto foi orçado considerando o uso máximo da infraestrutura e equipamentos do IFSC, focando os recursos em bolsas, consumíveis e logística.

| **Rubrica** | **Justificativa** | **Valor Total (R$)** |
| :--- | :--- | :--- |
| **1. Pessoal/Bolsas** | 1 Bolsa Nível Superior (12x R$ 2.000) + 2 Bolsas Nível Técnico (12x R$ 600) | 38.400,00 |
| **2. Equipamentos (Consumo)** | Baterias extras, cartões de memória, manutenção preventiva do drone. | 2.000,00 |
| **3. Material de Consumo** | Confecção de alvos (GCPs), cabos, mídia para backup, material gráfico. | 1.000,00 |
| **4. Serviços de Terceiros** | Transporte para campo (combustível), pequenos reparos. | 1.200,00 |
| **5. Reserva Técnica** | 10% para contingências (imprevistos de campo, necessidade de software extra). | 4.260,00 |
| **TOTAL GERAL DO PROJETO** | | **46.860,00** |

**Possíveis Fontes de Financiamento:** Edital de Pesquisa Aplicada (FAPESC), Edital de Extensão (IFSC/PROEX), Projeto de Cooperação Técnica com a Prefeitura Municipal de Florianópolis.

---

### 9. REFERÊNCIAS BIBLIOGRÁFICAS

[Inserir referências no formato ABNT. Exemplos:]
GONÇALVES, J. A.; HENRIQUES, R. UAV photogrammetry for topographic monitoring of coastal areas. ISPRS Journal of Photogrammetry and Remote Sensing, v. 104, p. 101-111, 2015.
IBGE. Manual Técnico de Geomorfologia. 2. ed. Rio de Janeiro: IBGE, 2009.
MUEHE, D. (Org.). Erosão e progradação no litoral brasileiro. Brasília: MMA, 2006.

---

**ANEXOS:**
A. Planilha de Cronograma Detalhado
B. Planilha de Orçamento Detalhado
C. Currículos Resumidos da Equipe
D. Carta de Anuência/Apoio Institucional (em busca)

---
**Elaborado por:** [Nome do Coordenador]
**E-mail:** [email@ifsc.edu.br]
**Telefone:** [(48) XXXX-XXXX]
**IFSC - Campus Florianópolis**