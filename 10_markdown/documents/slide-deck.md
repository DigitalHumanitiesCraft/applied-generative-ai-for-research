---
type: representation
source-type: document
source: "[[00_sources/slide-deck.md]]"
converter: "none (Markdown original); block IDs stamped deterministically per line"
channel: handover
metadata:
  title: "Knowledge, Context and Agentic Engineering for Knowledge Work. Full Slide Deck, slide-text export"
  creator: "Digital Humanities Craft"
  date: "2026-08-20"
  format: md
  identifier: "https://github.com/DigitalHumanitiesCraft/knowledge-context-agentic-engineering/blob/5c0e9d66bc9a169a0c184742bfe247fc232c7439/slides/full-slide-deck.md"
  license: "CC-BY-4.0 for the slide text; deck images carry third-party rights checked per deck"
  confidential: false
created: 2026-08-22
updated: 2026-08-22
---

# Full Slide Deck

Slide-text export of the Google deck of the teaching line, state of 2026-08-20. Everything below this header is the export as produced and carries no editorial changes. ^p0001

Knowledge, Context and Agentic Engineering for Knowledge Work ^p0002

Full Slidedeck. September 2026. ^p0003


Dr. Christopher Pollin MA MA ^p0004
Digital Humanities Craft OG ^p0005
www.dhcraft.org | office@dhcraft.org ^p0006
Slides were generated AI-assisted. Images are partly AI-generated. ^p0007
Knowledge Engineering, Context Engineering und Agentic Engineering bezeichnen drei miteinander verbundene Ebenen der Arbeit mit LLM-basierten AI Agents. ^p0008

Knowledge Engineering betrifft den Aufbau und die Pflege expliziten, revidierbaren Projektwissens. Dazu gehören Forschungsdaten, Dokumentationen, Anforderungen, Designentscheidungen und Prozesswissen ebenso wie Wissen, das zunächst nur implizit bei einzelnen Expert:innen oder innerhalb einer Organisation vorhanden ist. Dieses Wissen wird in einer Form festgehalten, in der es gelesen, überprüft, ergänzt und korrigiert werden kann. Im Promptotyping bildet eine fortschreibbare und versionierte Wissensbasis aus Markdown-Dokumenten die zentrale Struktur, die Forschungsdaten, Domänenwissen, Anforderungen, Implementierung und Verifikation miteinander verbindet. ^p0009

Context Engineering betrifft nicht den gesamten Wissensbestand, sondern den Informationszustand einer konkreten Aufgabe. Es bestimmt, welche Informationen, Anweisungen, Werkzeuge und Beispiele zu einem bestimmten Zeitpunkt im Kontextfenster eines Modells verfügbar sind, in welcher Reihenfolge sie bereitgestellt werden und was bewusst nicht geladen wird. Prompt Engineering konzentriert sich demgegenüber enger auf die Gestaltung einer einzelnen Eingabesequenz. Context Engineering organisiert den aufgabenrelevanten Ausschnitt aus einem größeren Wissensbestand über einen längeren Arbeitsverlauf. ^p0010

Agentic Engineering betrifft die Organisation und Kontrolle mehrschrittiger Arbeit, in der LLM-basierte Agents nicht nur Text erzeugen, sondern innerhalb einer Projektumgebung auf Wissens- und Softwareartefakte einwirken. Sie können Dateien lesen und bearbeiten, Datenbeschreibungen und Anforderungen auswerten, Code erzeugen, Programme ausführen, Ergebnisse prüfen und ihre Arbeit auf Grundlage von Rückmeldungen überarbeiten. Der Begriff ist deshalb weiter als agentische Softwareentwicklung: Die Arbeit richtet sich nicht nur auf Code, sondern auch auf Datenbeschreibungen, Spezifikationen, Mappings, Designentscheidungen, Prozessdokumente und Verifikationskonzepte. ^p0011

Die drei Ebenen erfüllen unterschiedliche Funktionen. Knowledge Engineering organisiert den verfügbaren Wissensbestand. Context Engineering stellt daraus den für eine Aufgabe relevanten Ausschnitt bereit. Agentic Engineering organisiert, wie ein Agent mit diesem Kontext innerhalb einer technischen Umgebung handelt. Ein AI Harness stellt dafür den Zugriff auf Dateien, Werkzeuge und Ausführungsumgebungen sowie die Verwaltung von Zustand, Zugriffsrechten und Rückmeldungen bereit. Das Harness entscheidet jedoch nicht selbst, welches Projektwissen relevant oder wissenschaftlich angemessen ist. ^p0012

Im Promptotyping werden diese Ebenen in einem iterativen Arbeitsprozess verbunden. Der Agent arbeitet aus einer gepflegten Projektwissensbasis, erzeugt oder verändert digitale Forschungsartefakte und schreibt Erkenntnisse aus Exploration, Implementierung und Prüfung in den Wissensbestand zurück. Dadurch entwickeln sich das dokumentierte Projektverständnis und das daraus erzeugte Artefakt gemeinsam weiter. ^p0013

Diese Struktur automatisiert keine neutrale Übersetzung von Forschungsdaten in Software. Sie macht vielmehr jenen Teil der Übersetzung explizit, der formuliert, dokumentiert und geprüft werden kann. Die Verantwortung für die Interpretation der Daten, die fachliche Angemessenheit der Modellierung und die Akzeptanz eines digitalen Forschungsartefakts verbleibt bei den für die Forschung verantwortlichen Personen. ^p0014


Prompt Engineering ^p0015
Prompt Engineering is the iterative design and evaluation of instructions for a specific model and task. ^p0016

Shift in focus: ^p0017
Prompt → Context Engineering ^p0018

Prompting Strategies: ^p0019
There Is No Prompt to Rule Them All ^p0020

What prompting really is !? ^p0021
Finding Coordinates in a ^p0022
Latent Program Space ^p0023
Schulhoff et al. The Prompt Report: A Systematic Survey of Prompting Techniques. 2024. ^p0024
https://doi.org/10.48550/arXiv.2406.06608 ^p0025

Knowledge ^p0026
& ^p0027
Context Engineering ^p0028
A defintion knowledge ^p0029

A definition context engineer ^p0030

 → ^p0031

→ ^p0032
literatur ^p0033


https://www.youtube.com/watch?v=FgaBdwSvOGM ^p0034

Skriptum:  https://docs.google.com/document/d/1yYEGgC2R8CDnkqqh8z6ApKfQYSETsYyez2vxwPHK8_k/edit?usp=sharing ^p0035

Computer- und datenbasierte Forschungsarbeit wird durch Frontier-LLMs asymmetrisch amplifiziert ^p0036
“The big goal that we are working towards is automating research” ^p0037
	- Jakub Pachocki (OpenAI’s chief scientist) ^p0038
“Geniuses in a data center” ^p0039
	- Dario Amodei (CEO Anthropic) ^p0040
Benchmarks ^p0041
https://simple-bench.com ^p0042
https://arcprize.org/leaderboard ^p0043
https://lastexam.ai ^p0044
https://epoch.ai/frontiermath ^p0045
… ^p0046
https://metr.org/time-horizons ^p0047

Lernziele ^p0048
Die Grundlagen und Möglichkeiten des Context- und Agentic Engineering verstehen und nutzen. ^p0049

Wissen für die Arbeit mit LLMs und AI Agents aufbereiten und nutzbar machen. ^p0050

Agentenunterstützte Workflows gestalten, umsetzen und evaluieren. ^p0051
Ablauf ^p0052
todo ^p0053

Zentrale Begriffe für die Arbeit mit AI Agents ^p0054
AI Agent ^p0055
LLM-basiertes System für mehrschrittige, werkzeuggestützte Aufgabenausführung ^p0056

Agentic Engineering ^p0057
Organisation und Kontrolle mehrschrittiger agentischer Arbeit ^p0058

AI Harness ^p0059
Technische Umgebung, in der AI Agents Kontext erhalten, Werkzeuge nutzen, Aufgaben ausführen und Rückmeldung verarbeiten ^p0060

Knowledge Engineering ^p0061
Aufbau und Pflege expliziten, revidierbaren Projektwissens ^p0062

Prompt Engineering ^p0063
Iterative Gestaltung und Optimierung von Prompts ^p0064

Context Engineering ^p0065
Auswahl, Organisation und Bereitstellung aufgabenrelevanter Informationen im Kontextfenster eines LLMs ^p0066

Schulhoff, Sander, Michael Ilie, Nishant Balepur, Konstantine Kahadze, Amanda Liu, Chenglei Si, Yinheng Li et al. 2024. “The Prompt Report: A Systematic Survey of Prompting Techniques.” ^p0067
https://doi.org/10.48550/arXiv.2406.06608 ^p0068
Mei, Lingrui et al. 2025. “A Survey of Context Engineering for Large Language Models.” ^p0069
https://doi.org/10.48550/arXiv.2507.13334 ^p0070
Sapkota, Ranjan, Konstantinos I. Roumeliotis, and Manoj Karkee. 2026. “AI Agents vs. Agentic AI: A Conceptual Taxonomy, Applications, and Challenges.” Information Fusion 126: 103599. ^p0071
https://doi.org/10.1016/j.inffus.2025.103599 ^p0072
Zhong, Hailin, and Shengxin Zhu. 2026. “AI Harness Engineering: A Runtime Substrate for Foundation-Model Software Agents.” ^p0073
https://doi.org/10.48550/arXiv.2605.13357 ^p0074
Russell, Stuart J., and Peter Norvig. Artificial Intelligence: A Modern Approach. 4th edn. Pearson Series in Artificial Intelligence. Pearson, 2020. https://aima.cs.berkeley.edu. ^p0075

AI Harness ^p0076
Technische Software-Schicht, über die ein LLM-basierter AI Agent Kontext erhält, Werkzeuge aufruft, Aktionen in einer Arbeitsumgebung ausführt und Rückmeldung verarbeitet. Das Harness verwaltet dabei Zustand, Zugriffsrechte und Kontrollfluss. ^p0077
Beispiele sind Claude Code, Codex, Cursor oder Pi) ^p0078
Zhong, Hailin, and Shengxin Zhu. 2026. “AI Harness Engineering: A Runtime Substrate for Foundation-Model Software Agents.” ^p0079
https://doi.org/10.48550/arXiv.2605.13357 ^p0080
Schematische Darstellung eines AI Harness. Erzeugt mit ChatGPT Images 2.0. ^p0081

Claude Code ^p0082

RQ4: Are measured intelligence, self-estimated intelligence, and implicit theories of intelligence able to predict statistically significant variance in the acceptance of “active” or “passive” enhancement methods in addition to personality traits (Big Five, Dark Triad, vulnerable narcissism)? ^p0083
Kontext ^p0084
Daten ^p0085
LLM-gestützte Exploration und Analyse von Forschungsdaten ^p0086
Grinschgl, S., Berdnik, A. L., Stehling, E., Hofer, G., & Neubauer, A. C. (2023). Who Wants to Enhance Their Cognitive Abilities? Potential Predictors of the Acceptance of Cognitive Enhancement. Journal of Intelligence, 11(6), 109. https://doi.org/10.3390/jintelligence11060109 ^p0087

Aggregated test data and the codebook: https://osf.io/2s3ze ^p0088

Pre-registration at https://osf.io/urwxt ^p0089
Codebook ^p0090
Paper ^p0091
Forschungsfrage und Auftrag ^p0092


Projekt vorbereiten: Quellen, Files und AI-Agent Loops ^p0093
Erstelle im aktuellen Verzeichnis ein Projekt mit dieser Struktur: ^p0094

hands-on-01-forschungsdatenanalyse/ ^p0095
├── data/ ^p0096
├── context/ ^p0097
├── task/ ^p0098
├── scripts/ ^p0099
├── outputs/ ^p0100
└── report/ ^p0101

Recherchiere anschließend die folgenden Ressourcen: ^p0102

 * Aggregated test data and the codebook: https://osf.io/2s3ze ^p0103
 * Pre-registration: https://osf.io/urwxt ^p0104

Lade die relevanten Dateien herunter und lege sie passend unter `data/` beziehungsweise `context/` ab. ^p0105

Erstelle außerdem `task/quellen.md` mit: ^p0106
 * Titel und Funktion jeder Datei, ^p0107
 * ursprünglicher URL, ^p0108
 * Dateiformat, ^p0109
 * kurzer Begründung der Zuordnung. ^p0110

Verändere die heruntergeladenen Quelldateien nicht. ^p0111
Zeige abschließend die angelegte Projektstruktur. ^p0112
Tool Use ^p0113
Loop ^p0114
Files ^p0115
└─────────── AI HARNESS ────────┘ ^p0116
1. Preparation ^p0117
Diese erste Phase ist die Preparation. Bevor der Agent etwas analysiert oder implementiert, wird zunächst ein belastbarer Projektbestand hergestellt. ^p0118
Im Prompt geben wir nicht jede einzelne Handlung vor. Wir formulieren ein Ziel: Der Agent soll eine Projektstruktur anlegen, die relevanten Quellen recherchieren, die Dateien herunterladen und sie sinnvoll einordnen. Dabei arbeitet er nicht nur im Chat, sondern innerhalb eines AI Harness – also einer technischen Umgebung, die ihm Zugriff auf Dateien, Webzugriff, Terminal und weitere Werkzeuge gibt. ^p0119
Auf der rechten Seite sehen wir mehrere zentrale Elemente agentischer Arbeit. Über Files nimmt der Agent den bestehenden Projektzustand wahr und verändert ihn. Durch Tool Use greift er auf Webressourcen und die lokale Projektumgebung zu. Diese Schritte laufen nicht einmalig ab, sondern in einem AI-Agent Loop: Der Agent prüft den aktuellen Zustand, wählt eine Handlung, führt ein Werkzeug aus, verarbeitet das Ergebnis und entscheidet über den nächsten Schritt. ^p0120
Das Ergebnis dieser Phase ist daher nicht bloß eine Antwort im Chat. Es entsteht ein persistenter und nachvollziehbarer Projektbestand: Forschungsdaten, Codebook und Präregistrierung liegen strukturiert vor, ihre Herkunft wird dokumentiert, und die Quelldateien bleiben unverändert. ^p0121
Methodisch ist das wichtig, weil die spätere Arbeit nicht bei null beginnt. Alle weiteren Schritte bauen auf diesem vorbereiteten Bestand auf. Preparation bedeutet hier also: Quellen und Arbeitsumgebung so einzurichten, dass der Agent kontrolliert, nachvollziehbar und wiederholbar weiterarbeiten kann. ^p0122


Vorgehen planen: Daten verstehen und Möglichkeiten abwägen ^p0123
2. Planning ^p0124
Untersuche die Forschungsdaten und die zugehörigen Kontextquellen. ^p0125

Entwickle zunächst ein konzeptionelles Vorgehen für ein lokales, statisches Webtool zur sicheren Exploration der ursprünglichen Daten. ^p0126

Erstelle das Tool, führe es lokal im Browser aus und prüfe die zentralen Funktionen. Verändere die Quelldateien nicht. ^p0127

Erstelle einen sehr kompakten Plan. Erkläre alles in einfacher Sprache, ohne Komplexität zu verlieren. ^p0128

hands-on-01-forschungsdatenanalyse/ ^p0129
├── context/ ^p0130
│   ├── Enhancement_Analyses_Syntax_shareable.sps   (13.374 Bytes) ^p0131
│   ├── Enhancement_Codebook.pdf                    (261.011 Bytes) ^p0132
│   └── Preregistration_urwxt_OSF-API.json          (33.385 Bytes) ^p0133
├── data/ ^p0134
│   ├── Enhancement_Data_SPSS_shareable.sav         (58.316 Bytes) ^p0135
│   └── Enhancement_Data_SPSS_shareable.xlsx        (72.063 Bytes) ^p0136
├── outputs/                                        (leer) ^p0137
├── report/                                         (leer) ^p0138
├── scripts/                                        (leer) ^p0139
└── task/ ^p0140
    └── quellen.md ^p0141
Konzeption vor Implementierung ^p0142

Lokales, statisches Webtool im Browser ^p0143

Kompakter Plan in einfacher Sprache ^p0144

Zielbild präzisieren: Rückfragen, Feedback und iterative Überarbeitung ^p0145
Lies den Projektbestand und deinen bisherigen Plan. ^p0146

Stelle mir gezielte Rückfragen, damit du das gewünschte Endergebnis, die Nutzungssituation und die fachlichen Anforderungen möglichst genau verstehst. ^p0147

Frage nach allem, was sich nicht zuverlässig aus den vorhandenen Dateien ableiten lässt. **Triff keine stillen Annahmen.** ^p0148

Nutze mein Feedback, um die Anforderungen und den Plan schrittweise zu überarbeiten. ^p0149

Fasse nach jeder Runde kurz zusammen, was du verstanden und geändert hast. ^p0150
3. Feedback & Self Revision ^p0151

Webtool umsetzen: Plan ausführen und ein funktionierendes Artefakt erzeugen ^p0152
Setze den überarbeiteten Plan um. ^p0153

Erstelle ein lokales, statisches Webtool zur Exploration der Forschungsdaten. ^p0154

Nutze die vorhandenen Daten und Kontextquellen, verändere die Quelldateien nicht und dokumentiere wichtige technische Entscheidungen. ^p0155

Öffne das Tool im Browser und behebe auftretende Fehler. ^p0156
4. Implementation ^p0157

Ergebnis prüfen: Funktionen, Datenverarbeitung und Übereinstimmung mit den Anforderungen ^p0158
Prüfe das erzeugte Webtool systematisch. ^p0159

Kontrolliere: ^p0160
- ob es lokal im Browser funktioniert, ^p0161
- ob die Daten korrekt eingelesen und dargestellt werden, ^p0162
- ob die vereinbarten Anforderungen umgesetzt sind, ^p0163
- ob die Quelldateien unverändert geblieben sind. ^p0164

Dokumentiere gefundene Fehler, behebe technische Probleme und fasse die Prüfergebnisse kompakt zusammen. ^p0165
5. Verification ^p0166

Context Engineering ^p0167
Context Engineering umfasst die systematische Auswahl, Organisation, Pflege und Bereitstellung der Informationen, die ein LLM-basiertes System für seine Arbeit benötigt. ^p0168

Context Engineering ^p0169

Model Context Window = 8K ^p0170
A context window, in the context of large language models (LLMs), refers to the portion of text that the model can consider at once when generating or analyzing language. ^p0171
[...] ^p0172
Model Context Window = 8K ^p0173
A context window, in the context of large language models (LLMs), refers to the portion of text that the model can consider at once when generating or analyzing language. It is essentially the window through which the model "sees" and processes text, helping it understand the current context to make predictions, generate coherent sentences, or provide relevant responses. ^p0174
[...] ^p0175
6000 Token ^p0176
Input Token ^p0177
Output Token ^p0178
Lorem ipsum … ^p0179
Lorem ipsum … ^p0180
1500 Token ^p0181
Context Window = 6000 + 1500 < 8000 ^p0182
Context Window = 10000 + 1500 > 8000 ^p0183
3500 tokens are not in the context window! ^p0184
What is a Context Window? Unlocking LLM Secrets. https://youtu.be/-QVoIxEpFkM ^p0185
Attention Is All You Need (2017). https://arxiv.org/abs/1706.03762 ^p0186
Hong, Kelly, Anton Troynikov, and Jeff Huber. Context Rot: How Increasing Input Tokens Impacts LLM Performance. Chroma, 2025. https://research.trychroma.com/context-rot. ^p0187
The Context Window is the model’s finite working space, containing the input and previously generated tokens available at each generation step. Through self-attention, the model uses these tokens to predict the next token. ^p0188
Context Rot describes how the model’s ability to retrieve and use relevant information can decline as the number of tokens in the context window grows. ^p0189
Context engineering begins with the information available to the model at each generation step. A large language model generates one token at a time. Its current context consists of the input and all tokens generated so far, while self-attention relates the tokens within this bounded sequence to predict the next token. Both examples show an 8,000-token context window. In the first example, 6,000 input tokens leave room for 2,000 output tokens. After 1,500 tokens have been generated, the complete sequence contains 7,500 tokens, all of which remain formally available to the model. In the second example, 10,000 input tokens combined with 1,500 output tokens would produce a sequence of 11,500 tokens, exceeding the limit by 3,500. The system must shorten the sequence through truncation or compaction, or reject the request. The red tokens represent information excluded from the resulting context and therefore unable to influence the next prediction. The formal context limit determines which tokens can be available. Context rot concerns how reliably the model uses them. As the sequence grows, relevant information can become harder to retrieve and apply, causing task performance to decline even before the formal limit is reached. The chart reports results from a controlled repeated-words task and should be understood as task-specific evidence. The pattern varies across models and tasks. Context engineering curates the active sequence so that relevant information retains priority within the finite context budget. ^p0190

Wissen auswählen, strukturieren und verdichten ^p0191
Context Compression kann zunächst allgemein als Verringerung der Informationsmenge verstanden werden, die in einen Arbeitskontext aufgenommen werden soll. Dazu gehören etwa: ^p0192
Auswahl relevanter Abschnitte, ^p0193
Zusammenfassung, ^p0194
Entfernung von Wiederholungen, ^p0195
Aggregation von Daten, ^p0196
Reduktion auf relevante Beispiele. ^p0197
Der Begriff bezeichnet jedoch zunächst nur die Verringerung des Umfangs. Für Context Engineering genügt das nicht. ^p0198
Distillation ^p0199
Das Paper verwendet deshalb den stärkeren Begriff Distillation. Distillation reduziert nicht nur die Tokenmenge, sondern überführt ein vorhandenes Verständnis in eine selektive, strukturierte und prüfbare Repräsentation. ^p0200
Erhalten bleiben sollen insbesondere: ^p0201
relevante Begriffe und Unterscheidungen, ^p0202
Beziehungen und Abhängigkeiten, ^p0203
Bedingungen und Einschränkungen, ^p0204
Unsicherheiten und offene Fragen, ^p0205
Begründungen und Entscheidungszusammenhänge. ^p0206
Das gleiche Ausgangsmaterial kann unterschiedlich destilliert werden, wenn sich Zweck oder Aufgabe verändern. Eine Zusammenfassung für eine allgemeine Einführung unterscheidet sich von einer Darstellung, die einen Agenten bei der Implementierung oder Verifikation anleiten soll. ^p0207
Das Paper grenzt Distillation daher ausdrücklich von blosser Zusammenfassung und Context Compression ab. Sie erzeugt eine inspizierbare Repräsentation, die für weitere Arbeit hinreichend sein soll. ^p0208

Wissensdokumente und ihre Serialisierung in Markdown ^p0209
Wissensdokumente ^p0210
Hier würde die verbesserte Definition stehen: ^p0211
Ein Wissensdokument ist eine begrenzte, strukturierte und revidierbare Repräsentation relevanten Wissens, die aus umfangreicherem Material destilliert und von Menschen geprüft sowie von LLM-basierten Systemen als Kontext genutzt werden kann. ^p0212
Danach die zentralen Eigenschaften: ^p0213
Begrenztheit ^p0214
 Ein Wissensdokument bildet nicht den gesamten Wissensbestand ab, sondern einen abgegrenzten Gegenstand oder Zweck. ^p0215
Strukturierung ^p0216
 Begriffe, Zusammenhänge, Regeln, Bedingungen und Unsicherheiten werden explizit organisiert. ^p0217
Revidierbarkeit ^p0218
 Das Dokument bleibt lesbar, kritisierbar, ergänzbar und korrigierbar. ^p0219
Duale Nutzbarkeit ^p0220
 Menschen können es prüfen und bearbeiten; LLM-basierte Systeme können es als Kontext verwenden. ^p0221
Zweckmässige Verdichtung ^p0222
 Das Dokument ist kompakt, ohne die für seinen Zweck erforderlichen Differenzierungen zu verlieren. ^p0223
Das Paper beschreibt solche Dokumente als begrenzte Repräsentationen, die aus umfangreicherem Material destilliert, für menschliche Prüfung gepflegt und für die Aufnahme in aufgabenspezifische Working Contexts verfügbar gemacht werden. ^p0224
Markdown als Serialisierung ^p0225
Das Wissensdokument ist das konzeptionelle Artefakt. Markdown ist eine mögliche technische Repräsentation dieses Artefakts. ^p0226
Markdown eignet sich dafür, weil es: ^p0227
als Plain Text offen und langfristig lesbar ist, ^p0228
einfache Strukturen wie Überschriften, Listen, Links, Tabellen und Codeblöcke unterstützt, ^p0229
mit unterschiedlichen Editoren bearbeitet werden kann, ^p0230
leicht versioniert und verglichen werden kann, ^p0231
durch Menschen direkt lesbar ist, ^p0232
durch LLMs ohne aufwendige Konvertierung verarbeitet werden kann. ^p0233

Wissensbasis und Working Context ^p0234
Dieser Abschnitt schliesst das Kapitel ab und verbindet die Einzelkonzepte. ^p0235
Wissensdokumente liegen persistent in einer Wissensbasis oder Projektumgebung. Sie müssen nicht bei jeder Aufgabe vollständig in das Context Window geladen werden. ^p0236
Das Paper unterscheidet deshalb: ^p0237
Project Knowledge Base ^p0238
 Der persistente, inspizierbare und revidierbare Bestand des dokumentierten Projektwissens. ^p0239
Working Context ^p0240
 Die für eine konkrete Aufgabe bereitgestellten Informationen, Dokumente, Datenzugriffe, Instruktionen und Werkzeuge. ^p0241
Der Working Context kann enthalten: ^p0242
die Aufgabenstellung, ^p0243
relevante Wissensdokumente oder einzelne Abschnitte, ^p0244
ausgewählte Daten und Beispiele, ^p0245
Agenteninstruktionen, ^p0246
Werkzeugbeschreibungen und Zugriffsrechte, ^p0247
aktuelle Ergebnisse und Rückmeldungen. ^p0248
Nicht jedes relevante Objekt muss vollständig im Context Window liegen. Ein Agent kann über Werkzeuge auf vollständige Datenbestände zugreifen, während nur Beschreibungen, Abfrageergebnisse oder ausgewählte Beispiele als Tokens in den Kontext aufgenommen werden. ^p0249
Die zentrale Unterscheidung lautet: ^p0250
Die Wissensbasis bewahrt verfügbares Wissen. Context Engineering stellt daraus den für eine konkrete Aufgabe geeigneten Working Context zusammen. ^p0251
Diese Trennung ist für das Paper zentral: Die persistente Wissensbasis und der aufgabenspezifische Working Context erfüllen unterschiedliche Funktionen und dürfen nicht gleichgesetzt werden. ^p0252

Agentic ^p0253
Engineering ^p0254
Agentic Engineering umfasst die systematische Organisation mehrschrittiger agentischer Arbeit, insbesondere die Zerlegung und Koordination von Aufgaben, den Einsatz von Werkzeugen, die Reaktion auf Zwischenergebnisse, die erforderlichen menschlichen Eingriffe sowie die Prüfung und Fortführung der Arbeit. ^p0255

Warum mehrschrittige Arbeit organisiert werden muss ^p0256
Agentische Arbeit ^p0257
Ein AI Agent verfolgt ein Ziel über mehrere Modell- und Werkzeugaufrufe. ^p0258
Er liest und verändert Dateien, führt Programme aus und verarbeitet Zwischenergebnisse. ^p0259
Seine nächsten Schritte hängen von Ergebnissen, Fehlern und Rückmeldungen aus der Arbeitsumgebung ab. ^p0260
Organisation und Kontrolle ^p0261
Aufgaben müssen begrenzt, zerlegt und koordiniert werden. ^p0262
Werkzeuge, Zugriffsrechte und Abbruchbedingungen müssen festgelegt werden. ^p0263
Zwischenergebnisse müssen geprüft und bei Bedarf an Menschen eskaliert werden. ^p0264
Der Projektzustand muss über mehrere Schritte hinweg nachvollziehbar bleiben. ^p0265
Kernaussage: ^p0266
Agentic Engineering organisiert, wie ein AI Agent über mehrere Schritte handelt, auf Ergebnisse reagiert und seine Arbeit prüfbar fortführt. ^p0267

Knowledge Engineering ^p0268
Knowledge Engineering umfasst den Aufbau und die Pflege expliziten, revidierbaren Projektwissens, das die aktuelle Auffassung eines Projekts von seinen Daten, seinem Zweck und den für die Umsetzung relevanten Entscheidungen festhält. ^p0269

“I know things” ^p0270
https://media.tenor.com/39mLNuMFLCsAAAAe/thats-what-i-do-i-drink-and-i-know-things.png ^p0271
Wissen kann vorhanden sein, ohne explizit dokumentiert, geteilt oder für einen Agenten nutzbar zu sein. ^p0272

Warum Wissen explizit festgehalten werden muss ^p0273
Implizites und fragmentiertes Wissen ^p0274
Wissen liegt verteilt in Dokumenten, Daten, Notizen, Arbeitspraktiken und bei einzelnen Personen. ^p0275
Vorhandene lokale Ordnung ergibt noch keine gemeinsame, systemweit nutzbare Wissensbasis. ^p0276
Informationen können widersprüchlich, unvollständig, veraltet oder nur aus ihrem Entstehungskontext verständlich sein. ^p0277
Persistentes und revidierbares Projektwissen ^p0278
Relevantes Wissen wird explizit repräsentiert und strukturiert. ^p0279
Menschen und LLM-basierte Systeme können denselben dokumentierten Stand lesen und verwenden. ^p0280
Aussagen, Entscheidungen und Unsicherheiten bleiben prüfbar, ergänzbar und korrigierbar. ^p0281
Kernaussage: ^p0282
Knowledge Engineering macht relevantes Wissen explizit, inspizierbar und revidierbar. ^p0283

Wissensmodellierung ^p0284
Konstruktion einer Wissensbasis: Konzepte einer Domäne identifizieren, formal repräsentieren, abfragbar machen. ^p0285
Personal Information Management ^p0286
Umgang mit eigener Information über Formate und Orte hinweg, im Dienst von Zielen und Rollen. ^p0287
Projektmanagement ^p0288
Systematische Planung, Steuerung und Kontrolle von Vorhaben innerhalb definierter Rahmenbedingungen. ^p0289
Fragen identifizieren ^p0290
Wissen erwerben ^p0291
Vokabular festlegen ^p0292
Wissen kodieren ^p0293
Instanzen beschreiben ^p0294
Abfragen und Inferenz ^p0295
Evaluieren ^p0296
Erwerben und erstellen ^p0297
Speichern und organisieren ^p0298
Pflegen und wiederfinden ^p0299
Nutzen und verteilen ^p0300
Kernproblem: Fragmentierung ^p0301
Kernkonzept: Personal Information Collection ^p0302
Initiierung ^p0303
Planung ^p0304
Durchführung ^p0305
Überwachung und Steuerung ^p0306
Abschluss ^p0307
Russell, Stuart J., and Peter Norvig. Artificial Intelligence: A Modern Approach. 4th edn. Pearson Series in Artificial Intelligence. Pearson, 2020. https://aima.cs.berkeley.edu. ^p0308
Jones, William, Jesse David Dinneen, Robert Capra, Anne R. Diekema, and Manuel A. Pérez-Quiñones. Personal Information Management. 2017. https://doi.org/10.1081/E-ELIS4-120053695. ^p0309
„Handbuch Projektmanagement von Jürg Kuster | ISBN 978-3-662-65472-9 | Fachbuch online kaufen - Lehmanns.de“. o. J. Zugegriffen 15. September 2024. https://www.lehmanns.de/shop/wirtschaft/59031377-9783662654729-handbuch-projektmanagement. ^p0310

Wissensdokumente ^p0311
Definition ^p0312
Ein Wissensdokument ist eine begrenzte, strukturierte und revidierbare Repräsentation relevanten Wissens, die aus einem umfangreicheren Bestand destilliert und von Menschen geprüft sowie von LLM-basierten Systemen als Kontext genutzt werden kann. ^p0313
Eigenschaften ^p0314
Begrenzt ^p0315
 Behandelt einen klar umrissenen Gegenstand oder erfüllt eine bestimmte Funktion. ^p0316
Strukturiert ^p0317
 Organisiert relevante Begriffe, Zusammenhänge, Regeln, Bedingungen und Unsicherheiten. ^p0318
Revidierbar ^p0319
 Kann gelesen, geprüft, ergänzt und korrigiert werden. ^p0320
Dual nutzbar ^p0321
 Für Menschen verständlich und prüfbar; für LLMs als Kontext verwendbar. ^p0322
Kompakt, aber hinreichend ^p0323
 Reduziert Umfang und Redundanz, ohne notwendige Differenzierungen zu verlieren. ^p0324
Technische Form ^p0325
Im Workshop werden Wissensdokumente als Markdown-Dateien gespeichert. ^p0326
Markdown eignet sich dafür, weil es: ^p0327
offener Plain Text ist, ^p0328
einfache Strukturen unterstützt, ^p0329
versionierbar und verlinkbar ist, ^p0330
von Menschen und LLMs direkt gelesen werden kann. ^p0331
Die begriffliche Pointe lautet: ^p0332
Das Wissensdokument ist das Konzept; Markdown ist seine technische Repräsentation. ^p0333

Persona Engineering: “You are a …” ^p0334
Du repräsentierst eine typische Teilnehmerin meines Workshops. ^p0335
Hintergrund: ^p0336
- 48 Jahre alt ^p0337
- Literaturwissenschaftlerin ^p0338
- arbeitet regelmäßig mit Word, Excel und digitalen Editionen ^p0339
- keine Erfahrung mit Terminal, Git oder VS Code ^p0340
- nutzt ChatGPT gelegentlich ^p0341
- ist motiviert, aber vorsichtig bei technischen Installationen ^p0342
- verwendet Windows ^p0343

Aufgabe: ^p0344
Lies die folgende Workshop-Anleitung aus dieser Perspektive. ^p0345

Identifiziere: ^p0346
1. Stellen, die du nicht sicher verstehen würdest, ^p0347
2. Begriffe, die nicht erklärt sind, ^p0348
3. Schritte, bei denen du wahrscheinlich Unterstützung benötigst, ^p0349
4. Fragen, die du während des Workshops stellen würdest. ^p0350

Erfinde keine technischen Fehler. Beurteile nur, was sich aus der Anleitung ergibt. ^p0351
Persona Engineering: A Field Guide to AI Synthetic Personas — Ishan Anand, InsightSciences.ai. https://youtu.be/YnNF55QV0zs?si=GfKc9ZmXyD_UtqYs ^p0352

Mapping Mobile Musicians ^p0353
Mobilität und Musiktheaterwissen im Graz der Nachkriegszeit ^p0354
am Beispiel der Sängerin Ira Malaniuk ^p0355
Erfassen ^p0356

Kuratieren ^p0357

Verstehen ^p0358

 Explorieren ^p0359
(lokal zeigen) ^p0360

AI Agents gibt es schon länger als LLMs ^p0361
Titelblatt von Wieners 1948 erschienenem Werk Cybernetics or Control and Communication in the Animal and the Machine. https://de.wikipedia.org/wiki/Norbert_Wiener ^p0362
Autonomie: handelt ohne ständige äußere Steuerung ^p0363

Reaktivität: antwortet auf Veränderungen seiner Umgebung ^p0364

Proaktivität: verfolgt von sich aus Ziele ^p0365

“soziale” Fähigkeit: interagiert mit anderen Agenten ^p0366
Ernst Peter Fischer: Norbert Wieners Kybernetik in 90 Sekunden. https://youtu.be/PKTgbBPMzeg ^p0367
Wooldridge, Michael, and Nicholas R. Jennings. ‘Intelligent Agents: Theory and Practice’. The Knowledge Engineering Review 10, no. 2 (1995): 115–52. https://doi.org/10.1017/S0269888900008122. ^p0368
Multi-Agent Hide and Seek. OpenAI 2017. https://www.youtube.com/watch?v=kopoLzvh5jY ^p0369
AlphaGo - The Movie | Full award-winning documentary. 2016. https://youtu.be/WXuK6gekU1Y ^p0370
Wang, Guanzhi, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, und Anima Anandkumar. “Voyager: An Open-Ended Embodied Agent with Large Language Models“, 25. Mai 2023. https://arxiv.org/abs/2305.16291v2. ^p0371

LLMs als Jagged Alien ‘Intelligences’ ^p0372
Eigenschaften des Modells ^p0373
Probabilistisch / Konfabulationen / Bias / Black-Box ^p0374
“Memorieren” Arithmetik, Buchstabieren ^p0375
Sycophancy als Tendenz von LLMs Nutzer:innen zuzustimmen ^p0376
Andersartiges Weltmodell ^p0377
“Every cat is smarter than an LLM”  (LeCun) ^p0378
Interaktionen ^p0379
Tool-Use (Websuche, Coding, … ) ^p0380
Context Window als “Aufmerksamkeitsspanne” ^p0381
Knowledge Cut-Off und kein Continual Learning ^p0382
“Reasoning” als “Thinking” Token ^p0383
Lindsey, Authors Jack, Wes Gurnee*, Emmanuel Ameisen*, u. a. „On the Biology of a Large Language Model“. Transformer Circuits, o. J. Zugegriffen 25. Mai 2025. https://transformer-circuits.pub/2025/attribution-graphs/biology.html. ^p0384
Fabrizio Dell’Acqua et al., ‘Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality’, Organization Science 37, no. 2 (2026): 403–23, https://doi.org/10.1287/orsc.2025.21838. ^p0385

Summerfield, Christopher. These Strange New Minds: How AI Learned to Talk and What It Means. Viking, 2025. ^p0386

Joshua Gans, ‘A Model of Artificial Jagged Intelligence’, arXiv:2601.07573, preprint, arXiv, 12 January 2026, https://doi.org/10.48550/arXiv.2601.07573. ^p0387


Fable 5 beauftragt 3 Opus Subagents um die TEI XML zu verifizieren und validieren ^p0388
Die Opus Subagents bedienen sich der “epistemischen Infrastruktur” aus Wissensdokumenten (pipeline.md) und Tools (Schema, Python Scripts, etc.) ^p0389

https://www.youtube.com/watch?v=OWPRU_Pc4Ng ^p0390


MCP vs Skills: Which Is Right for Your AI Agent and LLMs?. https://www.youtube.com/watch?v=goU9VIXA8II ^p0391

Modelling Routing ^p0392
Planning vs. Execution (writing code) ^p0393
Planning (best possible model) mit Fable oder Opus ^p0394
Execution mit Opus oder Sonnet ^p0395
Research → write spec → write code → PR → review → edit ^p0396
Spec = Specification = User Stories ^p0397
Specification ist kontextualisiert im knowledge ordner (daten, research, design etc.) ^p0398
Review pr wieder bei Fable ^p0399
Matthew Berman. https://youtu.be/1KKB_UiW6ls?si=QRBVjLB9C24DOzhC ^p0400


Knowledge und Context Engineering ^p0401
Knowledge Engineering organisiert den Bestand. Vorhandene Dokumente und Daten aufbereiten und nach Konventionen strukturieren; implizites Wissen von Expert:innen und Organisationen erheben und in dieselbe Form bringen. ^p0402
Context Engineering stellt daraus den für eine Aufgabe relevanten Ausschnitt im Kontextfenster des Agenten bereit. ^p0403
Die zweite Tätigkeit setzt die erste voraus. Das Wissenssystem ist kein Archiv, sondern ein Produktionssystem für Zielartefakte. ^p0404

Knowledge Engineering hat zwei Quellen. Die erste sind vorhandene Dokumente und Daten, die aufbereitet werden, PDF-Bestände in maschinenlesbare Formate überführt (etwa mit Docling), tabellarische Daten in Snapshot-Dokumente, Texte in destillierte Wissensdokumente. Die zweite Quelle ist Wissen, das noch in keinem Dokument steht, sondern implizit bei Expert:innen, in einer Institution oder einem Projekt liegt; es wird über Interviews, Deep Dives und Anforderungserhebung gehoben und in dieselbe strukturierte Form gebracht. Der Begriff stammt aus der Expertensystem-Tradition; die Verschiebung gegenüber der klassischen Fassung liegt im Formalisierungsziel, nicht mehr Logik und Ontologie, sondern strukturierte natürliche Sprache mit leichtem Metadaten-Anteil, weil das Sprachmodell das Sprachverstehen beisteuert. ^p0405
Context Engineering ist die Gestaltung dessen, was zu jedem Zeitpunkt eines Laufs im Kontextfenster liegt, Auswahl, Reihenfolge und Zeitpunkt des Ladens von Information, Werkzeugen und Anweisungen, einschließlich der Entscheidung, was bewusst nicht geladen wird. Die Abgrenzung gegen Prompting liegt im Gegenstand; Prompting optimiert eine einzelne Anweisung, Context Engineering verwaltet den Informationszustand einer ganzen Arbeitstrajektorie. Es setzt Knowledge Engineering voraus, weil nur ein strukturierter Bestand selektives Laden erlaubt; darin liegt die Abgrenzung gegen den Kurzschluss, Context Engineering sei besseres Prompting. ^p0406
Der Zweck des Ganzen ist die Produktion. Das Wissenssystem dient nicht der Ablage, sondern der Ableitung von Zielartefakten, eines Konzepts, eines Antrags, einer Spezifikation, eines Datenmodells. Kuratierte, verdichtete Wissensdokumente dienen als Eingabe eines LLM-Schritts, der das Artefakt erzeugt. Die User Story bildet die Brücke zwischen beiden Tätigkeiten, sie fasst eine fachliche Anforderung in eine Form, die für Menschen verständlich und für den Agenten als Kontext verwertbar ist. ^p0407


Vorbereitung ^p0408

Obsidian und der Vault als Arbeitsumgebung ^p0409
Obsidian ist ein Wissensmanagementsystem, das Notizen als Markdown-Dateien in einem lokalen Ordner speichert. Dieser Ordner heißt Vault. ^p0410
Die Daten bleiben auf dem eigenen Computer, das Dateiformat ist offen, kein Cloud-Konto ist erforderlich. ^p0411
Der Vault ist ein Second Brain, ein externes Gedächtnis, das ^p0412
individuelles oder institutionelles Wissen organisiert ^p0413
operative Arbeit und Projekte steuert ^p0414
Wissensstrukturen und Domänen modelliert und repräsentiert ^p0415
https://obsidian.md ^p0416
Obsidian ist ein Wissensmanagementsystem, das Notizen als Markdown-Dateien in einem gewöhnlichen lokalen Ordner speichert, und dieser Ordner heißt Vault. Es gibt keinen Server, keine Datenbank im Hintergrund, kein Cloud-Konto. Die Daten liegen auf dem eigenen Rechner, das Format ist offener Plain Text, und auf dieser Eigenschaft baut alles Weitere in diesem Workshop auf. ^p0417
Links sehen Sie meinen eigenen Vault, den Ordnerbaum und daneben die Graphansicht, in der jede Notiz ein Punkt ist und jeder Link eine Kante. Er ist über Jahre gewachsen, Projekte, Lehrmaterial, Begriffe, Literatur. Ein solcher Vault ist ein Second Brain, ein externes Gedächtnis. Er organisiert Wissen, individuelles wie institutionelles, also Ablage und Wiederauffinden. Er steuert operative Arbeit und Projekte, was ansteht, was geplant ist, in welchem Zustand ein Vorhaben ist. Und er modelliert und repräsentiert Wissensstrukturen, von informellen Links und Tags bis zu Dokumenttypen und Relationen. Auf dieser dritten Ebene arbeiten wir in diesem Workshop hauptsächlich, die zweite nehmen wir mit. ^p0418
Ein externes Gedächtnis ist genau das, was ein AI Agent braucht. Sein Kontextfenster ist ein begrenztes, flüchtiges Arbeitsgedächtnis, der Vault der Langzeitspeicher dazu. Weil der Vault ein Ordner mit offenen Textdateien ist, liest und schreibt der Agent dieselben Dateien wie ich. Obsidian ist eine Sicht auf diesen Ordner, das Terminal eine andere, der Agent eine dritte. Dieses geteilte Gedächtnis ist die Arbeitsgrundlage des Workshops, und deshalb richten wir es jetzt gemeinsam ein. ^p0419

Claude Code als AI Harness ^p0420

Obsidian installieren ^p0421

Claude Code einrichten ^p0422

Demo: Obsidian und Claude Code ^p0423

AI Agents ^p0424

Latent Programm Space ^p0425

AI Agent Begriffe ^p0426
Tools Use ^p0427
AI Harness ^p0428
AGENTS.md | CLAUDE.md ^p0429
Agent Skill ^p0430
Model Context Protocol (MCP) ^p0431
Agent2Agent (A2A) ^p0432
Subagents ^p0433
5 AI Agent Terms You Need to Know. https://youtu.be/k5jYwyhDMxA ^p0434

Tools Use ^p0435

AGENTS.md | CLAUDE.md ^p0436
Eine Markdown-Datei im Wurzelverzeichnis eines Projekts, die der Agent zu Beginn jeder Sitzung automatisch in seinen Kontext lädt. Sie beschreibt, wie dieses konkrete Projekt funktioniert, also Build- und Testbefehle, Code-Konventionen, Commit-Format und relevante Pfade. Mehrere solcher Dateien sind verschachtelbar, wobei eine Datei näher am Arbeitsverzeichnis die Regeln übergeordneter Dateien überschreibt. Enthält die Datei etwa die Vorgabe, vor jedem Commit pnpm test auszuführen, dann tut der Agent genau das bei jedem Commit in diesem Projekt, ohne dass du es erneut anweist. (Von OpenAI eingeführt.) ^p0437

Agent Skill ^p0438
Ein Ordner mit einer SKILL.md und optional Skripten und Ressourcen für eine bestimmte Aufgabe ^p0439

Name und Beschreibung jedes eingerichteten Skills lädt der Agent bei Sitzungsbeginn, die ganze Skill erst bei passender Anfrage ^p0440

Dauerhaft präsent bleibt allein die Beschreibung, das hält das Context Window bei themenfremden Aufgaben frei ^p0441

Beispiel: PowerPoint oder Word erzeugen ^p0442
Agent Skills. https://agentskills.io ^p0443
5 AI Agent Terms You Need to Know. https://youtu.be/k5jYwyhDMxA ^p0444
Skill-Aufruf bei claude.ai ^p0445

MCP ^p0446
Ein offenes Protokoll, das LLM-Anwendungen über eine einheitliche Schnittstelle mit externen Tools, Datenquellen und Workflows verbindet. Ein Tool oder eine Datenquelle wird in einen MCP-Server verpackt, und jeder Agent, der MCP spricht, kann diesen Server nutzen, ohne einen eigenen Konnektor dafür zu bauen. Das löst das M-mal-N-Problem, da sonst M Agenten und N Tools M×N maßgeschneiderte Verbindungen bräuchten. Braucht ein Agent etwa Daten aus Notion, spricht er MCP mit einem Notion-MCP-Server, und dieser Server kümmert sich um die eigentliche Notion-API; einen Stripe-Server spricht derselbe Agent auf dieselbe Weise an. (Von Anthropic.) ^p0447

A2A (Agent to Agent) ^p0448
A2A (Agent2Agent) ist ein offener Standard für die Kommunikation zwischen autonomen KI-Agenten. Er definiert eine gemeinsame Sprache, mit der Agenten aus unterschiedlichen Frameworks und von verschiedenen Anbietern zusammenarbeiten, ohne interne Logik, Tools oder Speicher preiszugeben. ^p0449
Opakheit: Interaktion ohne Offenlegung von Speicher, Tools oder proprietärer Logik. ^p0450
Erweiterbarkeit: formale Extensions mit gestuftem Promotionsverfahren, das den Kern stabil hält. ^p0451
Verhältnis zu MCP: komplementär, MCP regelt Agent-zu-Tool, A2A Agent-zu-Agent. ^p0452
Abgrenzung: kein Development-Kit, kein Tool-Call-Protokoll, kein MCP-Ersatz, keine Messaging-App. ^p0453


https://a2a-protocol.org/latest/topics/a2a-and-mcp/#why-different-protocols ^p0454

https://github.com/a2aproject/A2A ^p0455

Subagents ^p0456
Ein Subagent ist ein Kindagent, den der Hauptagent für eine abgegrenzte Teilaufgabe erzeugt. Jeder läuft in seinem eigenen frischen Kontextfenster, erledigt seine Arbeit und gibt nur ein Ergebnis zurück, was das Kontextfenster des Elternagenten sauber hält und Parallelität ermöglicht. Anders als die vier anderen Begriffe gibt es dafür keinen formalen Standard, sondern ein Muster, das in praktisch allen Agentensystemen nahezu identisch auftaucht. Im ersten typischen Fall ist eine Aufgabe zu groß für ein einzelnes Kontextfenster, etwa das Sichten von 500 Dateien; der Hauptagent erzeugt einen Subagenten, der die Dateien liest und eine Zusammenfassung zurückgibt, sodass er selbst nie alle 500 laden muss. Im zweiten Fall ist die Arbeit parallelisierbar, etwa zwanzig unabhängige Prüfungen, die zwanzig Subagenten gleichzeitig statt nacheinander erledigen. Dein Forschungsleitstellen-Muster mit parallel orchestrierten Claude-Instanzen ist eine konkrete Ausprägung davon. ^p0457

Knowledge und Context Engineering ^p0458

Warum AI Agents Context brauchen ^p0459
Mit wachsender Autonomie verschiebt sich der Engpass vom Modell zum Kontext. ^p0460
Das Kontextfenster ist begrenzt; die Leistung fällt deutlich unterhalb der Fenstergrenze ab (Context Rot). ^p0461
Lange autonome Läufe akkumulieren Rauschen; Reasoning-Budget fließt in Navigation statt in die Aufgabe. ^p0462
Zielgröße ist nicht kurz, sondern dicht und hinreichend. ^p0463

Der Befund lässt sich reproduzieren. Erhält ein Agent einen unstrukturierten Bestand und den Auftrag, daraus ein Zieldokument zu erzeugen, fällt das Ergebnis schwach aus oder der Kontext läuft über. Drei Mechanismen erklären das. Erstens degradiert die Modellleistung mit wachsender Kontextlänge deutlich unterhalb der nominellen Fenstergrenze; die Chroma-Untersuchung von 2025 zeigt das über 18 Modelle hinweg (Angaben auf der Verifikationsliste). Zweitens akkumuliert ein langer autonomer Lauf Rauschen, jedes gelesene irrelevante Dokument, jede Fehlausgabe bleibt im Fenster und verwässert die relevante Information. Drittens ist das Reasoning-Budget endlich; was das Modell auf die Navigation durch ungeordnetes Material verwendet, fehlt am eigentlichen Problem. ^p0464
Die Gegenposition gehört dazu. Für kurze Einzelabfragen sind starke Modelle robust gegen unordentlichen Kontext; das Problem kippt beim langhorizontigen Delegieren, wenn der Agent über viele Schritte selbständig mit dem Material arbeitet. Daraus folgt die Kernthese, mit wachsender Autonomie verschiebt sich der Engpass vom Modell zum Kontext. Ein besseres Modell behebt das nicht, ein besser organisierter Bestand schon. ^p0465
Die Konsequenz ist keine Kürzungsregel. Radikal verknappter Kontext verliert Provenienz und Begründung, das Ergebnis wird nicht besser, sondern anders schlecht. Die Zielgröße ist dicht und hinreichend, jede Aussage trägt Information, und ein frischer Kontext wird mit dem Material allein handlungsfähig. Die architektonische Antwort ist eine geschichtete Basis, ein minimaler Kern bleibt permanent geladen, die Tiefe wird bedarfsgesteuert nachgeladen. Wie diese Architektur gebaut wird, ist Gegenstand von Phase 2. ^p0466
Ref. Chroma, Context Rot, 2025. ^p0467


Wissensmanagment mit LLMs ^p0468
Obsidian ^p0469
https://obsidian.md ^p0470
Claude Code ^p0471
https://code.claude.com/docs/de/overview ^p0472


Screencast der heutigen Einheit zum Nachschauen ^p0473
Wissens- und Projektmanagement mit Obsidian und Claude Code. Einführung. https://youtu.be/31Y6uRLnkQA ^p0474

Wissensmodellierung ^p0475
Konstruktion einer Wissensbasis: Konzepte einer Domäne identifizieren, formal repräsentieren, abfragbar machen. ^p0476
Personal Information Management ^p0477
Umgang mit eigener Information über Formate und Orte hinweg, im Dienst von Zielen und Rollen. ^p0478
Projektmanagement ^p0479
Systematische Planung, Steuerung und Kontrolle von Vorhaben innerhalb definierter Rahmenbedingungen. ^p0480
Fragen identifizieren ^p0481
Wissen erwerben ^p0482
Vokabular festlegen ^p0483
Wissen kodieren ^p0484
Instanzen beschreiben ^p0485
Abfragen und Inferenz ^p0486
Evaluieren ^p0487
Erwerben und erstellen ^p0488
Speichern und organisieren ^p0489
Pflegen und wiederfinden ^p0490
Nutzen und verteilen ^p0491
Kernproblem: Fragmentierung ^p0492
Kernkonzept: Personal Information Collection ^p0493
Initiierung ^p0494
Planung ^p0495
Durchführung ^p0496
Überwachung und Steuerung ^p0497
Abschluss ^p0498
Russell, Stuart J., and Peter Norvig. Artificial Intelligence: A Modern Approach. 4th edn. Pearson Series in Artificial Intelligence. Pearson, 2020. https://aima.cs.berkeley.edu. ^p0499
Jones, William, Jesse David Dinneen, Robert Capra, Anne R. Diekema, and Manuel A. Pérez-Quiñones. Personal Information Management. 2017. https://doi.org/10.1081/E-ELIS4-120053695. ^p0500
„Handbuch Projektmanagement von Jürg Kuster | ISBN 978-3-662-65472-9 | Fachbuch online kaufen - Lehmanns.de“. o. J. Zugegriffen 15. September 2024. https://www.lehmanns.de/shop/wirtschaft/59031377-9783662654729-handbuch-projektmanagement. ^p0501

CLAUDE.md ^p0502
CLAUDE.md-Dateien sind Markdown-Dokumente, die einem Agenten persistente Instruktionen für ein Projekt oder einen Workflow geben. Sie werden als Klartext geschrieben und zu Beginn jeder Session in das Context Window geladen. Was dort steht, gilt in jeder Session und muss nicht mehr im Chat wiederholt werden. ^p0503
Es gibt ein globales und ein projektspezifisches CLAUDE.md. ^p0504
Der Agent macht denselben Fehler ein zweites Mal. ^p0505
Ein Review findet etwas, das der Agent über diese Codebasis hätte wissen müssen. ^p0506
Dieselbe Korrektur wird im Chat getippt wie in der letzten Session. ^p0507
Ein neues Teammitglied bräuchte denselben Kontext, um produktiv zu sein. ^p0508
Speaker Notes: Die rechte Spalte hält die vier Aufnahmesignale, jedes beschreibt eine Wiederholungssituation, die ein Eintrag beendet. Daneben existiert ein zweiter Entstehungsweg, vorab gesetzte Policy wie ein Abschlusskriterium, die keinem konkreten Fehler folgt. Real gibt es weitere Ebenen, CLAUDE.local.md für persönliche, nicht versionierte Ergänzungen und eine Organisationsebene in Claude Code; die Zwei-Ebenen-Darstellung ist eine didaktische Vereinfachung. ^p0509


Globale CLAUDE.md ^p0510
todo ^p0511
Das globale CLAUDE.md liegt im Home-Verzeichnis der Person und wird in jeder Session geladen, unabhängig vom Projekt. Es hält personengebundene Policy, also Rolle und Arbeitsmodus, Arbeitsweise und Abschlusskriterien. Das Auswahlkriterium lautet dauerhaft und projektunabhängig; alles, was nur ein Projekt betrifft, wandert eine Ebene tiefer. ^p0512
Das Beispiel demonstriert nebenbei, wie Instruktionen für ein Modell geschrieben werden, ausformulierte Sätze statt Stichwortlisten, direkte Anrede, überprüfbare Regeln. Der Abschnitt Detailwissen praktiziert selbst Context Engineering, das Dokument bleibt klein und verweist auf Skills und Projektwissen, statt Details zu inlinen. Das Abschlusskriterium entspricht der Definition of Done aus Scrum und verhindert den häufigsten Agentenfehler, das vorzeitige Fertigmelden. ^p0513

Projektspezifisches CLAUDE.md ^p0514
## Rolle und Arbeitsmodus

Du bist mein Co-Researcher. Wenn ich eine Frage stelle, gib eine Einschätzung und ändere nichts. Wenn ich eine Aufgabe stelle, setze sie direkt um, ohne Optionen aufzuzählen oder um Erlaubnis zu fragen. ^p0515

## Arbeitsweise

Mache die Anforderung explizit, bevor Code entsteht. Baue die minimale Lösung, die funktioniert, und keine Abstraktion, die niemand verlangt hat. ^p0516

## Abschlusskriterium

Melde nichts als fertig, bevor die Verifikation gelaufen ist, und benenne, was geprüft wurde. War keine Verifikation möglich, sage das und begründe es. ^p0517

## Detailwissen

Stilregeln liegen in Skills, Projektwissen liegt im jeweiligen Projekt. Dieses Dokument hält nur die Verweise. ^p0518

Das projektspezifische CLAUDE.md liegt im Root des Repositories und wird zusätzlich zum globalen geladen, sobald eine Session dort startet. Es hält projektgebundene Fakten, also Build- und Testkommandos, Konventionen, Projektstruktur und Domänenbegriffe, die der Agent in jeder Session dieses Projekts braucht. Bei Widerspruch gilt das spezifischere Dokument; das ist Konvention, keine Mechanik, denn technisch werden beide Ebenen nur konkateniert. ^p0519
Die vier Abschnitte decken die Standardfragen jeder Session ab, wie wird gebaut und getestet, welche Konventionen gelten, wo liegt was, welche Domänenbegriffe trägt das Projekt. Der Präzedenzsatz rechts trägt den Übergang zur nächsten Einheit, weil das System keine Konfliktauflösung kennt, muss die Rangfolge als Regel formuliert werden; hier schließen Skills und pfadgebundene Regeln an. ^p0520

Um was geht es hier? ^p0521
Für fortgeschrittenes Arbeiten mit LLMs muss man Projektmanagement, Kontext-Engineering, AI Harness und Wissensmodellierung berücksichtigen. Das ist zumindest meine These! Das ist besonders für mythos-/abler-Tier-Modelle wichtig, da man so den Agenten ausreichend Kontext zur Verfügung stellt, damit sie produktiv autonom arbeiten können. ^p0522


Promptotyping ^p0523


Folie 7: Promptotyping (Konzeptuelle Einordnung) ^p0524
Funktion: Übergang von der Demo zur Methode, Begriffe verankern Inhalt: ^p0525
Grafik einer Kugel mit den Elementen: ^p0526
Research Data ^p0527
Research Domain & Expert in the Loop ^p0528
Co-Intelligence (Mollick) ^p0529
(Frontier-)LLM & Context Engineering ^p0530
Research Artefacts (e.g. tools, workflows, models) ^p0531
In der Mitte: Der naive Prompt als Ausgangspunkt ^p0532


Spec Driven Development ^p0533

Scholar-Centred Design und Requirements Engineering ^p0534
Knowledge Acquisition ^p0535
Deep Dives (Workshops) mit Expert:innen ^p0536
Expert Interview ^p0537
Literature Review ^p0538
… ^p0539
Erstellung von Personas ^p0540
Sozialhistoriker:in ^p0541
Liturgiewissenschaftler:in … ^p0542
User Stories & Epics ^p0543
As a ... ^p0544
I want to ... ^p0545
So that I can … ^p0546
liturgy scholar ^p0547
compare the Office structure for a specific feast across multiple Libri Ordinarii (e.g. Salzburg, Passau, Regensburg) ^p0548
identify regional differences in liturgical practice ^p0549
liturgy scholar ^p0550
match chant incipits against the Cantus Index API and retrieve genre, Cantus ID, and concordances ^p0551
verify identifications without manual lookup in printed catalogues ^p0552
liturgy scholar ^p0553
filter rubrics by spatial references (altars, chapels, processional stations) ^p0554
reconstruct ritual movement within a specific church building ^p0555
social historian ^p0556
see network changes between 1828-1859 ^p0557
track how community business relationships developed over time ^p0558
social historian ^p0559
compare business activities between different community groups ^p0560
map economic cooperation and division in Norton ^p0561
social historian ^p0562
view how men and women participated differently in credit and trade networks ^p0563
reveal gender patterns in Norton's economic life ^p0564
Pollin, Christopher. ‘Modelling, Operationalising and Exploring Historical Information. Using Historical Financial Sources as an Example’. Graz, 2025. https://resolver.obvsg.at/urn:nbn:at:at-ubg:1-220602. ^p0565

Promptotyping: Exploring Vibe Coding before it was cool ^p0566
Pollin, Christopher. ‘Modelling, Operationalising and Exploring Historical Information. Using Historical Financial Sources as an Example’. 2025. http://unipub.uni-graz.at/obvugrhs/12127700. ^p0567
“There's a new kind of coding I call 'vibe coding', where you fully give in to the vibes, embrace exponentials, and forget that the code even exists.” ^p0568
		— Andrej Karpathy, February 2025 ^p0569
“I 'Accept All' always” ^p0570
“I don't read the diffs anymore” ^p0571
“it's not really coding — I just see stuff, say stuff, run stuff” ^p0572
Andrej Karpathy. Vibe Coding. https://x.com/karpathy/status/1886192184808149383 ^p0573

Christopher Pollin. “Haters gonna hate”: Warum die Kritik an Vibe Coding berechtigt ist – und welche Proto-AGI-Potenziale sie übersieht. https://dhcraft.org/excellence/blog/Vibe-Coding ^p0574
https://chpollin.github.io/HistInfo/InfoVis/wheaton-network-vis/wheaton-network-vis.html ^p0575
Andrej Karpathy coined the term “Vibe Coding” in February 2025. “here's a new kind of coding I call 'vibe coding', where you fully give in to the vibes, embrace exponentials, and forget that the code even exists.” The accompanying statements were deliberately provocative. “I 'Accept All' always.” “I don't read the diffs anymore.” “It's not really coding — I just see stuff, say stuff, run stuff.” ^p0576
By the time Karpathy named the practice, I had been doing it for almost half a year. Starting in autumn 2023, documented in the workshop series “Angewandte Generative KI in den (digitalen) Geisteswissenschaften” (chpollin.github.io/GM-DH), I experimented with LLMs at almost every level of the research process during my dissertation on workflows for historical information (Pollin 2025). I used them to model ontologies, generate TEI-XML and RDF, write SPARQL queries, and produce code for data analysis and visualisation. The key discovery was that user stories functioned as a bridge between structured research data and visual outputs. Instead of starting from the code, I described what a researcher needed to see and why, and let the LLM generate the implementation. In the early experiments, this meant Python scripts producing matplotlib plots and simple statistical charts. The data, with its semantics encoded in RDF and domain-specific ontologies, provided the structure. The user stories provided the direction. The LLM mapped one onto the other. As models improved across generations, from GPT-4 through Claude Opus 4.5 to the current frontier, the outputs grew more ambitious. What began as Python plots evolved into interactive, browser-based HTML interfaces. Tasks that failed or required extensive manual correction in 2023 worked reliably by late 2025. The blog post "Haters gonna hate" (dhcraft.org) contextualises why the critique of Vibe Coding is justified and what proto-AGI potentials it nonetheless reveals. ^p0577


Andrej Karpathy. Vibe Coding. https://x.com/karpathy/status/1886192184808149383 ^p0578

The AI Daily Brief. Rick Rubin on Art, Life, and Vibe Coding. https://youtu.be/6BDsFUvPqI0 ^p0579

Christopher Pollin. “Haters gonna hate”: Warum die Kritik an Vibe Coding berechtigt ist – und welche Proto-AGI-Potenziale sie übersieht. https://dhcraft.org/excellence/blog/Vibe-Coding ^p0580

 Vibe Coding ^p0581
99% Vibe Code with Claude Opus 4.1 in ~6h ^p0582
Based on real research data (8 Excel Files). ^p0583

Pollin, Christopher. ‘Promptotyping: Von der Idee zur Anwendung’. Digital Humanities Craft - Research Blogs, 24 April 2025. https://dhcraft.org/excellence/blog/Promptotyping ^p0584

Promptotyping ^p0585
https://chpollin.github.io/strashun/web-prototype ^p0586

Anhang ^p0587


AI Agents gibt es schon länger als LLMs ^p0588
Norbert Wiener begründet 1948 die Kybernetik und beschreibt, wie ein System sich selbst steuert, indem es Information über die eigenen Wirkungen zurückführt ^p0589

	Regelkreis = Feedback Loop → Loop Engineering (?) ^p0590
Wooldridge und Jennings (1995) bestimmen einen Agenten über vier Eigenschaften. ^p0591
Autonomie: 		handelt ohne ständige äußere Steuerung ^p0592
Reaktivität: 		antwortet auf Veränderungen seiner Umgebung ^p0593
Proaktivität: 		verfolgt von sich aus Ziele ^p0594
“soziale” Fähigkeit: 	interagiert mit anderen Agenten ^p0595
Titelblatt von Wieners 1948 erschienenem Werk Cybernetics or Control and Communication in the Animal and the Machine. https://de.wikipedia.org/wiki/Norbert_Wiener ^p0596
Ernst Peter Fischer: Norbert Wieners Kybernetik in 90 Sekunden. https://youtu.be/PKTgbBPMzeg ^p0597

Wooldridge, Michael, and Nicholas R. Jennings. ‘Intelligent Agents: Theory and Practice’. The Knowledge Engineering Review 10, no. 2 (1995): 115–52. https://doi.org/10.1017/S0269888900008122. ^p0598
Wiener begründet 1948 die Kybernetik als Wissenschaft von Steuerung, Regelung und Kommunikation in Systemen. Der zentrale Mechanismus ist der Regelkreis, ein System steuert sich selbst, indem es Information über die eigenen Wirkungen zurückführt und sein Verhalten daran korrigiert. Der Thermostat genügt als Minimalbeispiel, messen, vergleichen, nachstellen. Die Verbindung zur Gegenwart liegt in der Struktur, die agentische Ausführungsschleife aus Handeln, Ergebnislesen und erneutem Handeln ist ein Regelkreis, dessen Feedback über Tool-Ausgaben statt über Sensoren läuft. Das Titelblatt rechts datiert den Gedanken auf siebzig Jahre vor Claude Code. ^p0599
Wooldridge und Jennings bestimmen 1995 den Agenten über vier Eigenschaften, Autonomie, Reaktivität, Proaktivität und soziale Fähigkeit. Beim Durchgehen lohnt die Rückbindung an heutige Systeme. Autonomie entspricht dem Lauf ohne Rückfrage über viele Schritte, Reaktivität dem Verarbeiten von Tool-Ergebnissen und Fehlern, Proaktivität der Zielverfolgung über die Einzelanweisung hinaus, soziale Fähigkeit den Subagents und A2A. Die Definition ist dreißig Jahre alt und passt auf Claude Code. Die LLMs haben die Agentenidee nicht neu erfunden, sondern die fehlende Komponente nachgeliefert, ein Verhaltensmodul, das Sprache versteht und Handlungen planen kann. Die Frage, welche Komponente vorher fehlte und wie sie ersetzt werden sollte, leitet zur nächsten Folie über ^p0600

Reinforcement Learning Agents und LLM-Agents ^p0601
Multi-Agent Hide and Seek. OpenAI 2017. https://www.youtube.com/watch?v=kopoLzvh5jY ^p0602
AlphaGo - The Movie | Full award-winning documentary. 2016. https://youtu.be/WXuK6gekU1Y ^p0603
Wang, Guanzhi, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, und Anima Anandkumar. “Voyager: An Open-Ended Embodied Agent with Large Language Models“, 25. Mai 2023. https://arxiv.org/abs/2305.16291v2. ^p0604

NVIDIAs new 'Foundation Agent' SHOCKS the Entire Industry! | Dr. Jim Fan and agents for any REALITY. https://www.youtube.com/watch?v=SBoen3q5AoQ ^p0605


AlphaGo schlägt 2016 Lee Sedol. Move 37 in der zweiten Partie hielten kommentierende Profis zunächst für einen Fehler, er erwies sich als spielentscheidend. AlphaGo hat den Zug nicht aus menschlichen Partien gelernt, sondern im Selbstspiel entwickelt, die Strategie liegt außerhalb des menschlichen Trainingsmaterials. Für die Dokumentation lohnt die Szene, in der Fan Hui den Zug einordnet. ^p0606
Multi-Agent Hide and Seek, OpenAI 2019, erweitert den Befund um die Interaktionsdimension. Verstecker und Sucher entwickeln über Millionen Runden Strategie und Gegenstrategie, Verbarrikadieren, Rampennutzung, zuletzt das Box-Surfing, ein Physik-Exploit der Simulationsumgebung, den die Entwickler nicht kannten. Belohnt wurde nur Verstecken und Finden, alles Weitere ist emergent. Interaktion zwischen Agenten ist damit eine eigene Emergenzquelle, unabhängig von der Größe der beteiligten Modelle. Falls Video, dann der Box-Surfing-Ausschnitt, er belegt in dreißig Sekunden, was die Folie behauptet. ^p0607
Voyager, Wang et al. 2023, unterscheidet sich strukturell von den beiden ersten Systemen. Diese sind Reinforcement-Learning-Agenten, für ihre Aufgabe trainiert. Voyager exploriert Minecraft mit GPT-4 als Steuerung ohne aufgabenspezifisches Training. Der Agent schreibt sich Fähigkeiten als Code, legt sie in einer Skill-Bibliothek ab und baut auf ihnen auf. Der Tech Tree zeigt den Fähigkeitszuwachs gegen die Baselines, der Abstand wächst mit der Zeit, weil erworbene Skills weitere ermöglichen. Die Skill-Bibliothek beiläufig markieren, das Prinzip kehrt als Agent Skills in Claude Code wieder, die Vertiefung erfolgt dort. ^p0608

The Agent Vision (Semantic Web) ^p0609
Berners-Lee, Tim, James Hendler, und Ora Lassila. „The Semantic Web“. Scientific American 284, Nr. 5 (2001): 34–43. https://www.jstor.org/stable/pdf/26059207.pdf?refreqid=excelsior%3A1d9c33aa1ea640d57940082b42df15e6 ^p0610
Berners-Lee, Tim. This Is for Everyone. Pan Macmillan UK, 2025. ^p0611
Sechs Jahre nach Wooldridge und Jennings entwarfen Tim Berners-Lee, James Hendler und Ora Lassila 2001 im Scientific American eine konkrete Vision für das Web. Software-Agenten sollten von Seite zu Seite wandern und anspruchsvolle Aufgaben für ihre Nutzer erledigen. Das bekannte Szenario zeigt zwei Geschwister, die ihre Agenten Arzttermine und Fahrdienste koordinieren lassen. ^p0612

Diese Vision wird oft missverstanden. Das Semantic Web zielte nicht darauf, dass Maschinen menschliche Sprache verstehen. Berners-Lee stellte schon 1998 klar: "The Semantic Web is not artificial intelligence." Maschinenverständliche Dokumente bedeuten nur, dass eine Maschine ein wohldefiniertes Problem auf wohldefinierten Daten löst. Nicht die Maschine versteht den Menschen, sondern der Mensch strukturiert seine Daten für die Maschine, über Ontologien, RDF und eindeutige Bezeichner. ^p0613

Die heutigen Sprachmodelle lösen dieselbe Aufgabe auf dem umgekehrten Weg, sie verarbeiten unstrukturierten Text direkt, ohne die ontologische Infrastruktur, die das Semantic Web voraussetzte. ^p0614


AI Agents und Agentic AI (Sapkota) ^p0615
AI Agents sind modulare, LLM-gestützte Systeme, die über reine Textgenerierung hinausgehen und umrissene Aufgaben automatisieren. ^p0616
LLM als Kern ^p0617
Tool Use (Codeausführung, Websuche, Dateizugriff, Terminal) ^p0618
Memory ^p0619
Plannen ^p0620
Ein AI Agent führt umrissene Aufgaben weitgehend selbstständig aus, etwa Dokumente erstellen, Daten suchen, rechnen und Arbeitsabläufe koordinieren, statt nur auf Anfragen zu reagieren. ^p0621
Agentic AI ist kein einzelner Agent, sondern ein orchestrierter Verbund mehrerer Agenten, gekennzeichnet durch Zusammenarbeit, dynamische Aufgabenzerlegung, persistentes Gedächtnis und koordinierte Autonomie. ^p0622



Sapkota, Ranjan, Konstantinos I. Roumeliotis, and Manoj Karkee. ‘AI Agents vs. Agentic AI: A Conceptual Taxonomy, Applications and Challenges’. Information Fusion 126 (September 2025): 103599. https://doi.org/10.1016/j.inffus.2025.103599 . ^p0623
Was Norbert Wiener wohl über Claude Code gesagt hätte? ^p0624
Die heutige Ausprägung des Agenten ist der LLM-gestützte AI Agent. Sapkota, Roumeliotis und Karkee unterscheiden 2025 zwei Stufen. ^p0625

Ein AI Agent ist ein modulares, von einem Sprachmodell angetriebenes System für umrissene Aufgaben. Sein Kern ist das LLM, ergänzt um Werkzeugzugriff, also Codeausführung, Websuche, Dateizugriff und Terminal, sowie um Gedächtnis und Planung. Ein solcher Agent erstellt Dokumente, sucht Daten, rechnet und koordiniert Arbeitsabläufe, statt nur auf Anfragen zu antworten. ^p0626

Agentic AI ist die nächste Stufe, aber nicht durch mehr Autonomie, sondern durch eine andere Architektur. Sie ist kein einzelner Agent, sondern ein orchestrierter Verbund mehrerer Agenten, gekennzeichnet durch Zusammenarbeit, dynamische Aufgabenzerlegung, persistentes Gedächtnis und koordinierte Autonomie. ^p0627

Claude Code zeigt beide Stufen am selben Werkzeug. Im einfachen Lauf ist es ein AI Agent. Sobald es über Subagenten Teilaufgaben an mehrere koordinierte Instanzen delegiert, die parallel arbeiten, bewegt es sich zur Agentic AI. Die Unterscheidung ist also keine Schublade, sondern beschreibt zwei Betriebsarten. ^p0628
