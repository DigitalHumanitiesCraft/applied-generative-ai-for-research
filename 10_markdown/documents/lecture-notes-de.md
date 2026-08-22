---
type: representation
source-type: document
source: "[[00_sources/lecture-notes-de.md]]"
converter: "none (Markdown original); block IDs stamped deterministically per line"
channel: handover
metadata:
  title: "Knowledge, Context and Agentic Engineering for Knowledge Work. Full Lecture Notes, German"
  creator: "Digital Humanities Craft"
  date: "2026-08-20"
  format: md
  identifier: "https://github.com/DigitalHumanitiesCraft/knowledge-context-agentic-engineering/blob/5c0e9d66bc9a169a0c184742bfe247fc232c7439/script/full-lecture-notes-de.md"
  license: "CC-BY-4.0"
  confidential: false
created: 2026-08-22
updated: 2026-08-22
---

# Knowledge, Context and Agentic Engineering

## Konzepte, Methoden und Workflows für die kontrollierte Arbeit mit LLM-basierten AI Agents

**Dr. Christopher Pollin, MA MA** ^p0001
Digital Humanities Craft OG ^p0002
[www.dhcraft.org](https://www.dhcraft.org) · [office@dhcraft.org](mailto:office@dhcraft.org) ^p0003

**Workshopskriptum · Arbeitsfassung · Juli 2026** ^p0004

**Foliensatz:** *Knowledge, Context and Agentic Engineering* ^p0005
**Begleitmaterialien:** Workshopunterlagen und Hands-on-Dateien ^p0006

## Abstract

LLM-basierte AI Agents können computer- und datenbasierte Forschungsarbeit über einzelne Modellantworten hinaus unterstützen. Sie können Dateien untersuchen, Werkzeuge aufrufen, Programme ausführen, Zwischenergebnisse verarbeiten und digitale Forschungsartefakte über mehrere Schritte hinweg entwickeln. Ihre produktive Nutzung hängt jedoch nicht allein von der Leistungsfähigkeit eines Modells oder der Formulierung einzelner Prompts ab. Sie setzt voraus, dass relevantes Projektwissen explizit dokumentiert, für konkrete Aufgaben gezielt bereitgestellt und die daraus entstehende agentische Arbeit innerhalb einer technischen Umgebung organisiert, begrenzt und geprüft wird. ^p0007

Das Skriptum unterscheidet dafür vier miteinander verbundene Arbeitsebenen. **Prompt Engineering** gestaltet die aktuelle Eingabesequenz. **Knowledge Engineering** baut und pflegt einen expliziten, inspizierbaren und revidierbaren Bestand von Projektwissen. **Context Engineering** stellt daraus und aus weiteren Ressourcen den Informationszustand zusammen, den ein Modell oder Agent für eine konkrete Aufgabe benötigt. **Agentic Engineering** organisiert die mehrschrittige Ausführung, in der ein Agent Dateien und Daten untersucht, Werkzeuge verwendet, Ergebnisse verarbeitet und auf dieser Grundlage weitere Handlungen auswählt. Ein **AI Harness** stellt dafür den technischen Zugriff auf Dateien, Werkzeuge und Ausführungsumgebungen sowie die Verwaltung von Zustand, Zugriffsrechten und Rückmeldungen bereit. ^p0008

Diese Ebenen werden im **Promptotyping** als iterativer, dokumentenbasierter Forschungsworkflow verbunden. Eine fortschreibbare Project Knowledge Base hält den gegenwärtigen Stand des Projektwissens fest. Für einzelne Aufgaben werden daraus geeignete Working Contexts zusammengestellt. AI Agents erzeugen oder verändern auf dieser Grundlage digitale Forschungsartefakte. Erkenntnisse aus Exploration, Implementation und Prüfung werden anschließend in den dokumentierten Projektstand zurückgeführt. ^p0009

Als durchgehendes Beispiel dient die Entwicklung eines kleinen Demonstrators für eine digitale Edition. Der Fall verbindet Datenerzeugung, Datenmodellierung, Transformation, Frontend-Darstellung, technische Verifikation und fachliche Validierung. Dadurch wird sichtbar, dass eine digitale Edition nicht allein aus einem Interface besteht. Sie umfasst die nachvollziehbare Verbindung von Quelle, erzeugten Daten, Datenmodell, Transformation, Darstellung und den Gründen ihrer zweckgebundenen Akzeptanz. ^p0010

## Zu diesem Skriptum

Dieses Skriptum begleitet den gleichnamigen Foliensatz und folgt grundsätzlich dessen Dramaturgie. Die Folien verdichten Begriffe, Prozesse, Beispiele und Arbeitsaufträge visuell; die zugehörigen Kapitel erläutern die Argumentation, definieren zentrale Konzepte und dokumentieren die Hands-on-Übungen. Begriffe werden zunächst orientierend eingeführt und später an einer maßgeblichen Stelle vollständig ausgearbeitet. Wiederholungen erscheinen nur dort, wo sie für das Verständnis einer neuen Anwendung erforderlich sind. Quellen werden im Text durch Kurzbelege referenziert; vollständige Angaben stehen im Literaturverzeichnis. Ergänzende technische oder begriffliche Hinweise erscheinen in Fußnoten. ^p0011

## Inhaltsverzeichnis

- [1\. Einführung](#1-einfuhrung) ^p0012
  - [1.1 Ausgangslage](#1-1-ausgangslage) ^p0013
  - [1.2 Vom einzelnen Prompt zur organisierten Arbeitsumgebung](#1-2-vom-einzelnen-prompt-zur-organisierten-arbeitsumgebung) ^p0014
  - [1.3 Zentrale These](#1-3-zentrale-these) ^p0015
  - [1.4 Durchgehendes Beispiel: eine digitale Edition](#1-4-durchgehendes-beispiel-eine-digitale-edition) ^p0016
  - [1.5 Lernziele und Aufbau](#1-5-lernziele-und-aufbau) ^p0017
- [2\. Grundlagen: LLM, Assistant, AI Agent und AI Harness](#2-grundlagen-llm-assistant-ai-agent-und-ai-harness) ^p0018
  - [2.1 LLMs als probabilistische Textsysteme](#2-1-llms-als-probabilistische-textsysteme) ^p0019
  - [2.2 Pre-Training, Post-Training und Assistant-Verhalten](#2-2-pre-training-post-training-und-assistant-verhalten) ^p0020
  - [2.3 Vom Modell zum Agenten](#2-3-vom-modell-zum-agenten) ^p0021
  - [2.4 Das AI Harness](#2-4-das-ai-harness) ^p0022
- [3\. Prompt Engineering](#3-prompt-engineering) ^p0023
  - [3.1 Prompt und Prompt Engineering](#3-1-prompt-und-prompt-engineering) ^p0024
  - [3.2 Der Prompt als begrenzte Spezifikation](#3-2-der-prompt-als-begrenzte-spezifikation) ^p0025
  - [3.3 Rollen- und Persona-Prompting](#3-3-rollen-und-persona-prompting) ^p0026
  - [3.4 Iteration, Self-Revision und strukturierte Ausgaben](#3-4-iteration-self-revision-und-strukturierte-ausgaben) ^p0027
  - [3.5 Warum Promptwirkungen schwer zu evaluieren sind](#3-5-warum-promptwirkungen-schwer-zu-evaluieren-sind) ^p0028
  - [3.6 Mechanistische Perspektive](#3-6-mechanistische-perspektive) ^p0029
  - [3.7 Grenzen des Prompt Engineering](#3-7-grenzen-des-prompt-engineering) ^p0030
  - [3.8 Hands-on: Eine Editionsaufgabe als begrenzte Spezifikation](#3-8-hands-on-eine-editionsaufgabe-als-begrenzte-spezifikation) ^p0031
- [4\. Context Engineering](#4-context-engineering) ^p0032
  - [4.1 Vom Prompt zum Informationszustand einer Aufgabe](#4-1-vom-prompt-zum-informationszustand-einer-aufgabe) ^p0033
  - [4.2 Context Window und Context Rot](#4-2-context-window-und-context-rot) ^p0034
  - [4.3 Wie Informationen in den Modellkontext gelangen](#4-3-wie-informationen-in-den-modellkontext-gelangen) ^p0035
  - [4.4 Context Compression und Distillation](#4-4-context-compression-und-distillation) ^p0036
  - [4.5 Project Knowledge Base, Working Context und Context Window](#4-5-project-knowledge-base-working-context-und-context-window) ^p0037
  - [4.6 Hands-on: Einen Working Context für eine TEI-Aufgabe zusammenstellen](#4-6-hands-on-einen-working-context-fur-eine-tei-aufgabe-zusammenstellen) ^p0038
- [5\. Knowledge Engineering](#5-knowledge-engineering) ^p0039
  - [5.1 Warum Projektwissen explizit werden muss](#5-1-warum-projektwissen-explizit-werden-muss) ^p0040
  - [5.2 Knowledge Acquisition](#5-2-knowledge-acquisition) ^p0041
  - [5.3 Project Knowledge Base](#5-3-project-knowledge-base) ^p0042
  - [5.4 Wissensdokumente](#5-4-wissensdokumente) ^p0043
  - [5.5 Markdown als technische Repräsentation](#5-5-markdown-als-technische-reprasentation) ^p0044
  - [5.6 Instruktionsdateien und Agent Skills](#5-6-instruktionsdateien-und-agent-skills) ^p0045
  - [5.7 Governance und Kuration](#5-7-governance-und-kuration) ^p0046
  - [5.8 Hands-on: Ein Wissensdokument zu editorischer Unsicherheit destillieren](#5-8-hands-on-ein-wissensdokument-zu-editorischer-unsicherheit-destillieren) ^p0047
- [6\. Agentic Engineering](#6-agentic-engineering) ^p0048
  - [6.1 Warum mehrschrittige Arbeit organisiert werden muss](#6-1-warum-mehrschrittige-arbeit-organisiert-werden-muss) ^p0049
  - [6.2 Agentische Ausführungsschleife](#6-2-agentische-ausfuhrungsschleife) ^p0050
  - [6.3 Planung, Ausführung und Feedback](#6-3-planung-ausfuhrung-und-feedback) ^p0051
  - [6.4 Werkzeuge, Berechtigungen und Reversibilität](#6-4-werkzeuge-berechtigungen-und-reversibilitat) ^p0052
  - [6.5 MCP, Subagents und Agent-to-Agent-Kommunikation](#6-5-mcp-subagents-und-agent-to-agent-kommunikation) ^p0053
  - [6.6 Versionierte Zwischenstände und menschliche Intervention](#6-6-versionierte-zwischenstande-und-menschliche-intervention) ^p0054
  - [6.7 Hands-on: TEI erzeugen, validieren und ein Frontend implementieren](#6-7-hands-on-tei-erzeugen-validieren-und-ein-frontend-implementieren) ^p0055
- [7\. Promptotyping](#7-promptotyping) ^p0056
  - [7.1 Definition und Grundprinzip](#7-1-definition-und-grundprinzip) ^p0057
  - [7.2 Preparation](#7-2-preparation) ^p0058
  - [7.3 Exploration](#7-3-exploration) ^p0059
  - [7.4 Distillation](#7-4-distillation) ^p0060
  - [7.5 Requirements Engineering und Scholar-Centred Design](#7-5-requirements-engineering-und-scholar-centred-design) ^p0061
  - [7.6 Implementation](#7-6-implementation) ^p0062
  - [7.7 Verification, Validation und Acceptance](#7-7-verification-validation-und-acceptance) ^p0063
  - [7.8 Critical Expert](#7-8-critical-expert) ^p0064
  - [7.9 Write-back](#7-9-write-back) ^p0065
  - [7.10 Der Promptotype](#7-10-der-promptotype) ^p0066
  - [7.11 Hands-on: Write-back und Acceptance dokumentieren](#7-11-hands-on-write-back-und-acceptance-dokumentieren) ^p0067
- [8\. Zusammenfassung und Begriffsübersicht](#8-zusammenfassung-und-begriffsubersicht) ^p0068
- [9\. Literaturverzeichnis](#9-literaturverzeichnis) ^p0069
- [10\. Anhang: Vorlagen](#10-anhang-vorlagen) ^p0070

## Abbildungsverzeichnis

1. Wissensbestand, Working Context und agentische Ausführung ^p0071
2. Die digitale Edition als durchgehender Arbeitszusammenhang ^p0072
3. Sprachmodell und Assistentenfigur ^p0073
4. Konkurrierende Deutungen des Prompt Engineering ^p0074
5. Modell-, aufgaben- und sprachabhängige Promptwirkungen ^p0075
6. Warum Prompt Engineering schwer zu evaluieren ist ^p0076
7. Didaktisches Modell der Promptwirkung ^p0077
8. Partielle Rekonstruktion und experimentelle Steuerung interner Verarbeitung ^p0078
9. Project Knowledge Base, Working Context und Context Window ^p0079
10. Agentische Ausführungsschleife ^p0080
11. Promptotyping als geschlossener Entwicklungszyklus ^p0081
12. Prüfung, Evidenz und verantwortliche Acceptance ^p0082

# 1\. Einführung

## 1.1 Ausgangslage

Large Language Models werden zunehmend nicht nur als Systeme für einzelne Frage-Antwort-Interaktionen eingesetzt. In Verbindung mit Dateien, Werkzeugen und Ausführungsumgebungen können sie Aufgaben über mehrere Schritte hinweg bearbeiten. Ein LLM-basierter AI Agent kann Projektressourcen untersuchen, Informationen aus unterschiedlichen Quellen zusammenführen, Code erzeugen und ausführen, Fehlermeldungen verarbeiten und sein weiteres Vorgehen an den beobachteten Projektzustand anpassen. ^p0083

Diese Entwicklung erweitert die Möglichkeiten computer- und datenbasierter Forschung. Eine Historikerin kann beispielsweise aus einer kleinen Sammlung von Quellenbildern einen ersten Transkriptionsentwurf erzeugen lassen. Ein Editionsprojekt kann TEI-Dateien gegen ein Schema prüfen, Varianten eines Frontends erzeugen und die Darstellung editorischer Unsicherheit vergleichen. Ein Forschungsteam kann Datenprofile, Transformationen und Visualisierungen erstellen, ohne jeden technischen Schritt vollständig von Grund auf programmieren zu müssen. ^p0084

Die Fähigkeit, ein Artefakt zu erzeugen, ist jedoch nicht mit der Fähigkeit gleichzusetzen, dessen technische Korrektheit oder wissenschaftliche Angemessenheit zuverlässig zu beurteilen. Eine TEI-Datei kann wohlgeformt und schema-valide sein, obwohl eine unsichere Lesung editorisch unangemessen als sicherer Text ausgezeichnet wurde. Ein Interface kann technisch funktionieren und trotzdem den Eindruck erwecken, eine normalisierte Form sei die einzig richtige Lesart. Ein Datenmodell kann konsistent sein und zugleich Unterschiede ausblenden, die für die Forschungsfrage entscheidend sind. ^p0085

Die zentrale Herausforderung liegt deshalb nicht allein in der Erzeugung von Ergebnissen. Sie liegt in der Organisation der Bedingungen, unter denen diese Ergebnisse entstehen, geprüft, revidiert und für einen benannten Zweck verwendet werden können. ^p0086

## 1.2 Vom einzelnen Prompt zur organisierten Arbeitsumgebung

Bei einer einfachen und klar abgegrenzten Aufgabe kann eine präzise formulierte Anweisung ausreichen. Ein Prompt kann etwa verlangen, aus einer Tabelle alle Datumsangaben zu extrahieren und als JSON auszugeben. Sobald eine Aufgabe jedoch mehrere Dateien, Werkzeuge und Entscheidungen umfasst, reicht die Betrachtung eines einzelnen Prompts nicht mehr aus. ^p0087

Nehmen wir an, ein Agent soll für eine digitale Edition eine historische Seite transkribieren, als TEI modellieren und anschließend in einem Frontend darstellen. Dafür muss geklärt werden: ^p0088

- Welche Transkriptionsrichtlinien gelten? ^p0089
- Welche Version des TEI-Modells ist maßgeblich? ^p0090
- Wie werden unleserliche Stellen, Ergänzungen und Streichungen repräsentiert? ^p0091
- Darf der Agent die Ausgangsdatei verändern? ^p0092
- Welche Tests müssen ausgeführt werden? ^p0093
- Was geschieht, wenn eine editorische Entscheidung nicht aus den Quellen oder Richtlinien hervorgeht? ^p0094
- Welche Erkenntnisse aus der Implementation müssen in die Projektdokumentation zurückgeschrieben werden? ^p0095

Diese Fragen betreffen unterschiedliche Ebenen. Ein Teil gehört zur Gestaltung der aktuellen Aufgabe, ein Teil zum persistenten Projektwissen, ein Teil zur Auswahl des aufgabenspezifischen Kontextes und ein Teil zur Kontrolle der mehrschrittigen Ausführung. ^p0096

## 1.3 Zentrale These

Die zentrale These dieses Skriptums lautet: ^p0097

**Abbildung 1: Wissensbestand, Working Context und agentische Ausführung.** ^p0098
*Die schematische Übersicht zeigt die vier Ebenen des Skriptums. Prompt Engineering formuliert die aktuelle Aufgabe. Knowledge Engineering pflegt den persistenten Projektbestand. Context Engineering wählt daraus und aus weiteren Ressourcen den Working Context. Agentic Engineering organisiert die Ausführung im AI Harness. Rückmeldungen aus Implementation und Prüfung können Änderungen an allen vier Ebenen auslösen.* ^p0099

> Produktive und nachvollziehbare Arbeit mit LLM-basierten AI Agents entsteht nicht allein durch bessere Modelle oder besser formulierte Prompts. Sie setzt das Zusammenspiel von organisiertem Projektwissen, aufgabenspezifischem Kontext, kontrollierter agentischer Ausführung und verantwortlicher Prüfung voraus.
^p0100


Vier Begriffe strukturieren diesen Zusammenhang: ^p0101

- **Prompt Engineering** gestaltet die aktuelle Eingabesequenz. ^p0102
- **Knowledge Engineering** baut und pflegt den verfügbaren Wissensbestand. ^p0103
- **Context Engineering** stellt den für eine konkrete Aufgabe erforderlichen Informationszustand zusammen. ^p0104
- **Agentic Engineering** organisiert die mehrschrittige Ausführung innerhalb einer technischen Umgebung. ^p0105

Das **AI Harness** vermittelt zwischen diesen Ebenen. Es stellt Werkzeuge und Zugriffe bereit, verwaltet den Zustand einer Arbeit und gibt Ergebnisse an das Modell zurück. Es entscheidet jedoch nicht, welche editorische Lesung angemessen ist oder ob ein Artefakt für eine Publikation akzeptiert werden kann. ^p0106

## 1.4 Durchgehendes Beispiel: eine digitale Edition

Das Skriptum verwendet eine kleine digitale Edition als durchgehendes Beispiel. Ausgangspunkt sind drei bis fünf historische Seitenbilder, eine Rohtranskription, editorische Richtlinien und ein begrenztes TEI-Ausgangsmodell. Ziel ist ein lokaler Demonstrator, der Faksimile, diplomatische Transkription, normalisierte Lesung und editorische Unsicherheiten sichtbar macht. ^p0107

Das Beispiel verbindet drei Arbeitsbereiche: ^p0108

**Abbildung 2: Die digitale Edition als durchgehender Arbeitszusammenhang.** ^p0109
*Die Abbildung verbindet Quellenbilder und Datenerzeugung mit TEI-basierter Datenmodellierung, Transformation und Frontend-Darstellung. Die Pfeile verlaufen nicht nur in Richtung des Interfaces: Probleme, die erst in der Darstellung sichtbar werden, führen zurück zu Transkription, Modellierungsregeln und Anforderungen.* ^p0110

1. **Datenerzeugung:** Transkription, Annotation, Normalisierung und Provenienz. ^p0111
2. **Datenmodellierung:** TEI-Strukturen, Entitäten, Relationen, Varianten und Unsicherheiten. ^p0112
3. **Frontend-Darstellung:** synoptische Ansichten, Umschaltung von Textschichten, Hervorhebung von Annotationen und Darstellung editorischer Eingriffe. ^p0113

Die Bereiche sind nicht voneinander unabhängig. Erst in der Frontend-Darstellung kann sichtbar werden, dass eine Modellierungsregel unzureichend ist. Eine als einfaches Attribut modellierte Unsicherheit kann sich beispielsweise nicht differenziert genug darstellen lassen. Umgekehrt kann eine elegante Oberfläche eine editorisch problematische Vereinfachung verdecken. Die Implementation ist daher nicht nur Ausführung, sondern auch eine Form der Untersuchung des Projektwissens. ^p0114

## 1.5 Lernziele und Aufbau

Nach der Bearbeitung des Skriptums und der zugehörigen Übungen sollen die Teilnehmenden: ^p0115

- Prompt, Knowledge, Context und Agentic Engineering unterscheiden können; ^p0116
- die Rolle eines AI Harness erklären können; ^p0117
- Prompts als begrenzte Spezifikationen formulieren können; ^p0118
- zwischen Project Knowledge Base, Working Context und Context Window unterscheiden können; ^p0119
- Wissensdokumente aus heterogenen Quellen destillieren können; ^p0120
- mehrschrittige agentische Aufgaben planen, begrenzen und prüfen können; ^p0121
- technische Verifikation von fachlicher und wissenschaftlicher Validierung unterscheiden können; ^p0122
- Erkenntnisse aus Implementation und Prüfung in den dokumentierten Projektstand zurückführen können; ^p0123
- die Grenzen agentischer Autonomie und die Notwendigkeit verantwortlicher menschlicher Entscheidungen erkennen. ^p0124

Die Kapitel folgen einer einfachen Bewegung: vom einzelnen Prompt über den aktiven Kontext und den persistenten Wissensbestand zur agentischen Ausführung und schließlich zum Promptotyping als integrierter Methode. ^p0125

# 2\. Grundlagen: LLM, Assistant, AI Agent und AI Harness

## 2.1 LLMs als probabilistische Textsysteme

Ein Large Language Model erzeugt Text, indem es auf Grundlage der bisherigen Eingabesequenz Wahrscheinlichkeiten für das nächste Token berechnet. Das ausgewählte Token wird Teil des Kontextes für die nächste Vorhersage. Dieser autoregressive Vorgang wird wiederholt, bis eine Ausgabe abgeschlossen ist.[^1] ^p0126

Die Beschreibung als *Next Token Prediction* klingt einfacher, als das beobachtete Verhalten vermuten lässt. Durch umfangreiches Pre-Training können Modelle sprachliche, fachliche und formale Muster reproduzieren, Texte transformieren, Code erzeugen und komplexe Aufgaben bearbeiten. Dennoch bleibt die Ausgabe probabilistisch. Derselbe Prompt kann bei mehreren Durchläufen unterschiedliche Ergebnisse erzeugen. Eine plausible Formulierung ist daher nicht automatisch eine rekonstruierte Tatsache, und eine kohärente Begründung ist nicht automatisch ein Nachweis ihrer Richtigkeit. ^p0127

Für die digitale Edition bedeutet dies: Ein Modell kann eine sehr überzeugende Transkription erzeugen, obwohl einzelne Zeichen falsch gelesen wurden. Es kann eine TEI-Struktur ausgeben, die formal plausibel aussieht, obwohl sie nicht den projektspezifischen Richtlinien entspricht. Die sprachliche Qualität einer Antwort darf deshalb nicht mit ihrer fachlichen Verlässlichkeit verwechselt werden. ^p0128

## 2.2 Pre-Training, Post-Training und Assistant-Verhalten

Im Pre-Training werden umfangreiche Text- und andere Datenbestände verwendet, um statistische Repräsentationen sprachlicher und fachlicher Muster zu lernen. Vereinfacht kann man sagen, dass dabei modellintern nutzbare Zusammenhänge entstehen. Diese sind jedoch nicht wie Einträge in einer Datenbank adressierbar. Das Modell besitzt kein verlässliches Seiten- oder Quellenregister und kann seltene oder editionsspezifische Informationen falsch rekonstruieren. ^p0129

Post-Training richtet das Modell stärker auf bestimmte Aufgaben-, Interaktions- und Verhaltensformen aus. Dazu gehören Instruction Tuning, Reinforcement Learning from Human Feedback und verwandte Verfahren. Ein Basismodell wird dadurch zu einem System, das typischerweise als hilfreicher Assistent antwortet, Anweisungen befolgt und bestimmte Sicherheits- oder Stilregeln berücksichtigt. ^p0130

Die in einer Interaktion erscheinende Assistentenfigur ist nicht mit einem menschlichen Gegenüber gleichzusetzen. ^p0131

Folie zur Unterscheidung zwischen Sprachmodell und Assistentenfigur ^p0132

**Abbildung 3: Sprachmodell und Assistentenfigur.** ^p0133
*Die Folie unterscheidet das zugrunde liegende Modell von dem durch Post-Training, Systeminstruktionen und aktuellen Kontext stabilisierten Assistentenverhalten. Die anthropomorphe Form der Interaktion ist praktisch nützlich, darf aber nicht als Nachweis menschlicher Intentionalität oder fachlicher Autorität verstanden werden.* Sie ist ein durch Training, Systeminstruktionen und aktuellen Kontext stabilisiertes Verhaltensmuster. Das erklärt, warum sachliche, strukturierte Kommunikation häufig produktiv ist: Das Modell ist auf menschliche Kommunikationsformen ausgerichtet. Es erklärt zugleich, warum soziale Kohärenz nicht mit menschlicher Intentionalität oder fachlicher Autorität verwechselt werden darf.[^2] ^p0134

## 2.3 Vom Modell zum Agenten

Ein isolierter Modellaufruf erzeugt eine Ausgabe. Ein Agent verfolgt dagegen ein Ziel über mehrere Modell- und Werkzeugaufrufe hinweg. Er kann seine Umgebung untersuchen, eine Handlung auswählen, das Ergebnis beobachten und sein Vorgehen aktualisieren. ^p0135

Im Editionsbeispiel kann ein Agent: ^p0136

1. den Projektordner untersuchen, ^p0137
2. die editorischen Richtlinien lesen, ^p0138
3. eine TEI-Datei erzeugen, ^p0139
4. einen Validator ausführen, ^p0140
5. die Fehlermeldung analysieren, ^p0141
6. die Datei korrigieren, ^p0142
7. eine Transformation starten, ^p0143
8. das Frontend prüfen, ^p0144
9. offene fachliche Fragen dokumentieren. ^p0145

Das LLM bildet dabei das flexible Planungs- und Interpretationsmodul. Seine tatsächlichen Handlungsmöglichkeiten entstehen erst durch Werkzeuge und eine Arbeitsumgebung. ^p0146

## 2.4 Das AI Harness

Ein **AI Harness** ist die technische Software-Schicht, über die ein LLM-basierter Agent Kontext erhält, Werkzeuge aufruft, auf Dateien zugreift, Programme ausführt und Rückmeldungen verarbeitet. Systeme wie Claude Code, Codex oder Cursor stellen unterschiedliche Formen eines solchen Harness bereit.[^3] ^p0147

Das Harness kann beispielsweise festlegen: ^p0148

- welche Ordner gelesen oder verändert werden dürfen; ^p0149
- welche Befehle ohne Bestätigung ausgeführt werden können; ^p0150
- wie Werkzeugausgaben in den Modellkontext zurückgelangen; ^p0151
- wie lange ein Lauf fortgesetzt wird; ^p0152
- wann ein Mensch einbezogen werden muss; ^p0153
- wie Zwischenergebnisse gespeichert werden. ^p0154

Das Harness stellt technische Kontrollmöglichkeiten bereit. Es entscheidet jedoch nicht, ob eine editorische Modellierung wissenschaftlich angemessen ist. Ein XML-Validator kann feststellen, dass `<unclear>` an einer bestimmten Stelle zulässig ist. Er kann nicht entscheiden, ob die Quelle tatsächlich unleserlich ist oder ob eine alternative Lesung wahrscheinlicher wäre. ^p0155

# 3\. Prompt Engineering

## 3.1 Prompt und Prompt Engineering

Ein Prompt ist mehr als eine Frage. Er ist die für einen Modellaufruf bereitgestellte Eingabesequenz. Sie kann eine Aufgabe, Ausgangsmaterialien, Kontextinformationen, Anforderungen, Einschränkungen, Beispiele, Verfahrenshinweise und Vorgaben für die erwartete Ausgabe enthalten. ^p0156

**Prompt Engineering** bezeichnet die iterative Entwicklung einzelner Prompts durch Veränderungen ihres Inhalts, ihrer Struktur oder der auf sie angewandten Prompting-Techniken ^p0157

Folie mit konkurrierenden öffentlichen Vorstellungen von Prompt Engineering ^p0158

**Abbildung 4: Konkurrierende Deutungen des Prompt Engineering.** ^p0159
*Die Folie kontrastiert Prompting als vermeintliche Beschwörungskunst, als vermarktetes Versprechen perfekter Formeln und als Verstärkung vorhandener Expertise. Die Gegenüberstellung motiviert eine engere Arbeitsdefinition: Prompt Engineering gestaltet eine konkrete Eingabesequenz, ohne fehlendes Fachwissen oder Projektkontext ersetzen zu können.* (Schulhoff et al. 2024). Der Begriff ist bewusst enger als Context Engineering. Er richtet sich auf eine konkrete Eingabesequenz, nicht auf die gesamte Informationsumgebung einer längeren Arbeitstrajektorie. ^p0160

Ein einfacher Prompt kann lauten: ^p0161

> Transkribiere diese Seite.
^p0162


Eine begrenztere und prüfbarere Fassung wäre: ^p0163

> Transkribiere die bereitgestellte Seite diplomatisch. Erhalte Zeilenumbrüche, markiere unleserliche Stellen als `[unleserlich]`, normalisiere keine Schreibweisen und ergänze keine Wörter, die nicht sichtbar sind. Gib zuerst die Transkription und anschließend eine Liste unsicherer Lesungen mit Zeilenreferenz aus.
^p0164


Die zweite Fassung macht sichtbar, welche Eigenschaften des Ergebnisses erwartet werden. Sie garantiert noch keine korrekte Transkription, reduziert aber die Zahl stiller Annahmen. ^p0165

## 3.2 Der Prompt als begrenzte Spezifikation

Ein guter Prompt ist weniger eine rhetorische Formel als eine **begrenzte Spezifikation**. Er beschreibt eine aktuelle Aufgabe innerhalb eines bereits vorhandenen Wissens- und Arbeitskontextes. ^p0166

Typische Bestandteile sind: ^p0167

- **Ziel:** Was soll erzeugt oder verändert werden? ^p0168
- **Ausgangslage:** Welche Dateien, Daten oder bisherigen Ergebnisse sind relevant? ^p0169
- **Anforderungen:** Welche Eigenschaften muss das Ergebnis besitzen? ^p0170
- **Einschränkungen:** Was darf nicht verändert oder angenommen werden? ^p0171
- **Vorgehen:** Welche Schritte oder Prüfungen sind erforderlich? ^p0172
- **Ausgabeform:** In welchem Format soll das Ergebnis vorliegen? ^p0173
- **Abschlusskriterium:** Woran ist erkennbar, dass die Aufgabe hinreichend bearbeitet wurde? ^p0174

Nicht jede Aufgabe benötigt alle Bestandteile in gleicher Ausführlichkeit. Eine einfache Formatumwandlung kann durch einen kurzen Prompt eindeutig beschrieben werden. Eine editorisch folgenreiche Transformation benötigt dagegen eine genauere Spezifikation. ^p0175

Die Präzision eines Prompts hängt nicht von seiner Länge ab. Ein sehr langer Prompt kann widersprüchlich oder schwer priorisierbar sein. Ein kurzer Prompt kann ausreichen, wenn die relevanten Regeln bereits in Wissensdokumenten und Instruktionsdateien vorliegen. ^p0176

### Beispiel: TEI-Erzeugung

Erzeuge für \`page-001.txt\` eine TEI-Datei. ^p0177

Verwende: ^p0178

\- \`knowledge/transcription-rules.md\` ^p0179

\- \`knowledge/tei-model.md\` ^p0180

\- \`knowledge/uncertainty.md\` ^p0181

Anforderungen: ^p0182

\- Erhalte Seiten- und Zeilenwechsel. ^p0183

\- Verändere den Transkriptionstext nicht stillschweigend. ^p0184

\- Markiere unsichere Lesungen nach den dokumentierten Regeln. ^p0185

\- Verwende nur Elemente und Attribute, die im Projektmodell vorgesehen sind. ^p0186

\- Validere die Datei gegen \`schema/edition.rng\`. ^p0187

Abschluss: ^p0188

\- Speichere die Datei unter \`tei/page-001.xml\`. ^p0189

\- Führe die Validierung aus. ^p0190

\- Berichte über verbleibende fachliche Unsicherheiten getrennt von technischen Fehlern. ^p0191

Der Prompt enthält keine vollständige Erklärung der editorischen Regeln. Er verweist auf den persistenten Wissensbestand. Dadurch bleibt er kompakt und auf die aktuelle Aufgabe begrenzt. ^p0192

## 3.3 Rollen- und Persona-Prompting

Eine verbreitete Form des Promptings weist dem Modell eine Rolle zu: ^p0193

> Du bist eine erfahrene Editionswissenschaftlerin.
^p0194


Eine solche Formulierung kann Terminologie, Stil, Perspektive und Detaillierungsgrad beeinflussen. Sie fügt dem Modell jedoch kein neues Fachwissen hinzu. Die Rolle kann höchstens gelernte Muster fachsprachlicher Kommunikation wahrscheinlicher machen. ^p0195

**Role Prompting** bezeichnet eine knappe funktionale Zuweisung. **Persona Prompting** beschreibt eine ausgearbeitete Perspektive mit Hintergrund, Erfahrung, Zielen, Einschränkungen und Nutzungssituation. Beide sollten gemeinsam betrachtet, aber nicht gleichgesetzt werden. ^p0196

Beispiel einer Persona: ^p0197

Du repräsentierst eine Teilnehmerin des Workshops. ^p0198

Hintergrund: ^p0199

\- Literaturwissenschaftlerin ^p0200

\- Erfahrung mit digitalen Editionen ^p0201

\- regelmäßige Arbeit mit Word und Excel ^p0202

\- keine Erfahrung mit Terminal, Git oder VS Code ^p0203

\- grundsätzlich interessiert, aber vorsichtig bei Installationen ^p0204

\- arbeitet mit Windows ^p0205

Prüfe die folgende Anleitung aus dieser Perspektive. ^p0206

Identifiziere: ^p0207

1\. unklare Begriffe, ^p0208

2\. fehlende Zwischenschritte, ^p0209

3\. stillschweigend vorausgesetztes Wissen, ^p0210

4\. Stellen, an denen du wahrscheinlich Unterstützung benötigst. ^p0211

Eine synthetische Persona kann mögliche Probleme sichtbar machen. Sie erzeugt jedoch keine empirischen Nutzerdaten. Ihre Antworten sind Hypothesen, die mit realen Personen, Beobachtungen oder vorhandener Nutzerforschung geprüft werden müssen. ^p0212

Rollen- und Persona-Prompting eignen sich besonders für: ^p0213

- Stilvariation, ^p0214
- Perspektivwechsel, ^p0215
- frühe Interface- und Materialkritik, ^p0216
- Vorbereitung von Interviews, ^p0217
- Identifikation möglicher Rückfragen. ^p0218

Sie ersetzen nicht: ^p0219

- Fachwissen, ^p0220
- reale Stakeholder, ^p0221
- empirische Nutzerforschung, ^p0222
- fachliche Validierung. ^p0223

## 3.4 Iteration, Self-Revision und strukturierte Ausgaben

Prompts entstehen häufig nicht in einem Schritt. Eine produktive Interaktion kann aus mehreren begrenzten Durchgängen bestehen: ^p0224

> erzeugen → prüfen → korrigieren → verdichten
^p0225


Ein erster Prompt kann einen Entwurf erzeugen. Ein zweiter fordert eine kriteriengeleitete Prüfung. Ein dritter überarbeitet nur die tatsächlich identifizierten Probleme. ^p0226

Beispiel: ^p0227

Prüfe die TEI-Datei auf: ^p0228

1\. Abweichungen von \`transcription-rules.md\`, ^p0229

2\. unzulässige oder nicht definierte Elemente, ^p0230

3\. stillschweigende Normalisierungen, ^p0231

4\. unmarkierte Unsicherheiten. ^p0232

Liste zuerst die Befunde mit Zeilenreferenz. ^p0233

Verändere die Datei noch nicht. ^p0234

Danach: ^p0235

Überarbeite ausschließlich die bestätigten Befunde. ^p0236

Bewahre alle nicht betroffenen Strukturen. ^p0237

Führe anschließend die Schema-Validierung erneut aus. ^p0238

Diese Form der **Self-Revision** kann Fehler sichtbar machen, ist aber keine unabhängige Verifikation. Dasselbe Modell kann seine eigenen Fehlannahmen übersehen oder nachträglich plausibel begründen. Self-Revision wird verlässlicher, wenn explizite Kriterien, externe Tests und überprüfbare Referenzen vorliegen. ^p0239

Strukturierte Ausgabeformate reduzieren Mehrdeutigkeit. Ein Prompt kann eine Markdown-Tabelle, JSON, XML oder eine definierte Dateistruktur verlangen. Dabei sind unterschiedliche Ebenen zu unterscheiden: ^p0240

- syntaktische Konformität, ^p0241
- strukturelle Vollständigkeit, ^p0242
- semantische Richtigkeit, ^p0243
- wissenschaftliche Angemessenheit. ^p0244

Gültiges JSON beweist nur, dass die Syntax stimmt. Schema-valide TEI beweist nur, dass die formalen Regeln eingehalten wurden. Ob die Quelle angemessen repräsentiert ist, bleibt eine fachliche Frage. ^p0245

## 3.5 Warum Promptwirkungen schwer zu evaluieren sind

Prompting kann überraschend empfindlich auf Formulierungen reagieren. ^p0246

Folie mit empirischen Beispielen ungewöhnlicher Promptwirkungen ^p0247

**Abbildung 5: Modell-, aufgaben- und sprachabhängige Promptwirkungen.** ^p0248
*Die Beispiele zeigen, dass emotionale Zusätze, Höflichkeit, Formalität und kleine sprachliche Veränderungen messbare, aber heterogene Effekte erzeugen können. Die Folie dient nicht als Sammlung empfohlener Tricks, sondern als Evidenz dafür, dass beobachtete Promptwirkungen lokal und schwer zu verallgemeinern sind.* Frühere Studien berichteten Effekte emotionaler Zusätze, von Höflichkeit oder ungewöhnlichen automatisch erzeugten Prompts. Andere Untersuchungen zeigen, dass irrelevante Zusätze die Leistung verschlechtern oder dass Effekte auf neueren Modellen nicht stabil repliziert werden (Li et al. 2023; Yin et al. 2024; Battle und Gollapudi 2024; Rajeev et al. 2025). ^p0249

Daraus folgt nicht, dass Prompt Engineering wirkungslos ist. Es folgt vielmehr, dass Promptwirkungen häufig lokal sind. Sie hängen ab von: ^p0250

- Modell und Modellversion, ^p0251
- Aufgabe und Datensatz, ^p0252
- Sprache, ^p0253
- Position und Struktur der Information, ^p0254
- Evaluationsmetrik, ^p0255
- Zufallsvariation. ^p0256

Eine veränderte Leistung nach einer Promptvariation beweist außerdem nicht, dass die Formulierung aus dem vermuteten Grund wirkt. Ein Star-Trek-Präfix kann in einem Benchmark die Leistung verbessern. Daraus folgt nicht automatisch, dass „analytische Präzision“ mechanistisch als Star-Trek-Konzept aktiviert wurde. Solche Erklärungen sind Hypothesen, solange keine direkte mechanistische Evidenz vorliegt. ^p0257

Promptvarianten sollten deshalb wie experimentelle Interventionen behandelt werden: ^p0258

Folie zur schwierigen Evaluation von Prompt Engineering ^p0259

**Abbildung 6: Warum Prompt Engineering schwer zu evaluieren ist.** ^p0260
*Die Abbildung verbindet drei Probleme: irrelevante Zusätze können Reasoning stören, ungewöhnliche automatisch erzeugte Prompts können unerwartet gut abschneiden, und Rollenformulierungen verbessern nicht zuverlässig Faktentreue oder Schlussfolgerungsleistung. Einzelne erfolgreiche Prompts sind daher keine hinreichende Grundlage für allgemeine Best Practices.* ^p0261

1. Ziel und Metrik festlegen. ^p0262
2. Eine Baseline definieren. ^p0263
3. Möglichst nur einen relevanten Bestandteil verändern. ^p0264
4. Mehrere Beispiele und Wiederholungen verwenden. ^p0265
5. Auf neuen Fällen prüfen. ^p0266
6. Modell und Version dokumentieren. ^p0267
7. Fachliche Qualität getrennt von Stil und Format bewerten. ^p0268

## 3.6 Mechanistische Perspektive

Sprachliche Eingaben werden in hochdimensionale numerische Repräsentationen überführt. Unterschiedliche Formulierungen verändern die internen Aktivierungen, aus denen die Wahrscheinlichkeitsverteilung möglicher Ausgaben entsteht. Semantische und funktionale Beziehungen können sich in diesen Repräsentationen widerspiegeln. ^p0269

Der Ausdruck *Latent Program Space* kann als Metapher ^p0270

Didaktisches Modell von Prompt, Aktivierungspfad und Latent Program Space ^p0271

**Abbildung 7: Didaktisches Modell der Promptwirkung.** ^p0272
*Die Darstellung veranschaulicht, dass eine Eingabe interne Repräsentationen und Verarbeitungspfade beeinflusst. Der „Latent Program Space“ ist dabei als konzeptionelle Metapher für gelernte Verarbeitungsroutinen zu lesen, nicht als klar abgegrenzter Speicher klassischer Programme.* für die Menge gelernter Verarbeitungsroutinen verstanden werden, die ein Modell abhängig von Eingabe und Kontext unterschiedlich aktiviert. Übersetzen, Zusammenfassen, Klassifizieren oder Erklären sind keine klar getrennten Programme im klassischen Sinn. Sie sind wiederkehrende Verhaltensmuster, die aus den Gewichten und dem aktuellen Aktivierungsverlauf entstehen. ^p0273

Mechanistische Interpretierbarkeitsverfahren versuchen, Teile solcher internen Berechnungen zu rekonstruieren. ^p0274

Folie mit Attribution Graph und Steuerung interner Aktivierungsrichtungen ^p0275

**Abbildung 8: Partielle Rekonstruktion und experimentelle Steuerung interner Verarbeitung.** ^p0276
*Links wird ein Attribution Graph als partielle Rekonstruktion einer internen Berechnung gezeigt. Rechts verändert die Verstärkung bestimmter Aktivierungsrichtungen das beobachtete Verhalten. Die Beispiele stützen die Annahme systematischer interner Verarbeitung, liefern aber keine vollständige Erklärung natürlicher Promptwirkungen.* Attribution Graphs und verwandte Verfahren zeigen, dass bestimmte interne Strukturen und Aktivierungsrichtungen mit beobachtbarem Verhalten zusammenhängen können (Lindsey et al. 2025). Diese Befunde machen plausibel, dass unterschiedliche Prompts unterschiedliche Verarbeitungsverläufe begünstigen. Sie liefern jedoch noch keine vollständige Theorie, mit der sich natürliche Promptwirkungen zuverlässig vorhersagen lassen. ^p0277

## 3.7 Grenzen des Prompt Engineering

Prompt Engineering kann eine aktuelle Aufgabe präzisieren. Es kann jedoch grundlegende Probleme der Wissens- und Arbeitsorganisation nicht allein lösen. ^p0278

Ein guter Prompt ersetzt nicht: ^p0279

- fehlendes oder unzugängliches Projektwissen; ^p0280
- widersprüchliche Richtlinien; ^p0281
- ungeklärte Anforderungen; ^p0282
- einen überladenen oder irrelevanten Kontext; ^p0283
- persistente Dokumentation; ^p0284
- Werkzeug- und Berechtigungsmanagement; ^p0285
- technische Tests; ^p0286
- fachliche Validierung; ^p0287
- die Organisation längerer Arbeitstrajektorien. ^p0288

Je länger und ressourcenreicher eine Aufgabe wird, desto weniger lässt sie sich als Optimierung einer einzelnen Eingabesequenz beschreiben. Dann verschiebt sich der Gegenstand von der Formulierung des Prompts zur Organisation des Informationszustands, in dem der Agent arbeitet. ^p0289

## 3.8 Hands-on: Eine Editionsaufgabe als begrenzte Spezifikation

### Ziel

Aus einer vagen Aufgabe wird ein begrenzter und prüfbarer Prompt. ^p0290

### Ausgangsformulierung

> Erstelle eine digitale Edition dieser Seite.
^p0291


### Arbeitsauftrag

Präzisieren Sie: ^p0292

- Zielartefakt, ^p0293
- Ausgangsdateien, ^p0294
- editorische Regeln, ^p0295
- unveränderliche Ressourcen, ^p0296
- erwartete Ausgabe, ^p0297
- technische Prüfungen, ^p0298
- offene fachliche Entscheidungen. ^p0299

### Musterlösung

Untersuche \`sources/page-001.jpg\` und \`transcription/page-001.txt\`. ^p0300

Erzeuge einen ersten TEI-Entwurf unter \`tei/page-001.xml\`. ^p0301

Verwende: ^p0302

\- \`knowledge/transcription-rules.md\` ^p0303

\- \`knowledge/tei-model.md\` ^p0304

\- \`knowledge/uncertainty.md\` ^p0305

Regeln: ^p0306

\- Verändere die Quelldateien nicht. ^p0307

\- Erhalte Seiten- und Zeilengrenzen. ^p0308

\- Normalisiere keine Schreibweise, sofern dies nicht ausdrücklich vorgesehen ist. ^p0309

\- Markiere unsichere Lesungen und unleserliche Stellen. ^p0310

\- Erfinde keine fehlenden Inhalte. ^p0311

Prüfung: ^p0312

\- Validiere gegen \`schema/edition.rng\`. ^p0313

\- Trenne technische Fehler von fachlichen Unsicherheiten. ^p0314

\- Benenne Annahmen, die nicht aus den Quellen oder Wissensdokumenten hervorgehen. ^p0315

### Reflexion

- Welche Informationen gehören in den Prompt? ^p0316
- Welche Informationen sollten persistent in Wissensdokumenten stehen? ^p0317
- Welche Entscheidungen kann der Agent ausführen, aber nicht autorisieren? ^p0318

# 4\. Context Engineering

## 4.1 Vom Prompt zum Informationszustand einer Aufgabe

Ein Agent soll für eine Seite einer digitalen Edition einen TEI-Entwurf erzeugen. Im Projektordner liegen jedoch weit mehr Informationen, als er für diesen Arbeitsschritt unmittelbar benötigt: mehrere hundert Seitenbilder, allgemeine Editionsrichtlinien, verschiedene Versionen des Schemas, Protokolle, Testberichte, frühere Fehlversuche und bereits erzeugte TEI-Dateien. ^p0319

Der vollständige Projektbestand ist für das Projekt relevant, aber nicht alles daraus muss gleichzeitig im Modellkontext liegen. Für die konkrete Seite benötigt der Agent vor allem: ^p0320

- das Seitenbild, ^p0321
- die Transkription, ^p0322
- die geltenden Transkriptionsregeln, ^p0323
- den einschlägigen Teil des TEI-Modells, ^p0324
- einige geprüfte Beispiele, ^p0325
- die aktuelle Aufgabe und ihre Prüfkriterien. ^p0326

Weitere Ressourcen können im Projektbestand verbleiben und bei Bedarf über Werkzeuge gelesen oder abgefragt werden. ^p0327

**Context Engineering** bezeichnet die systematische Auswahl, Organisation, Pflege und Bereitstellung dieses aufgabenspezifischen Informationszustands (Mei et al. 2025). Es bestimmt nicht nur, welche Informationen ein Modell erhält, sondern auch, in welcher Form und Reihenfolge sie vorliegen, wann weitere Informationen nachgeladen werden und was bewusst außerhalb des aktuellen Kontextes bleibt. ^p0328

## 4.2 Context Window und Context Rot

Ein Modell kann nicht gleichzeitig auf alle Dateien, Notizen und Daten eines Projekts zugreifen. Es verarbeitet nur jene Informationen, die innerhalb eines aktuellen Laufs tatsächlich bereitgestellt werden. Dazu gehören je nach System: ^p0329

- System- und Projektinstruktionen, ^p0330
- die aktuelle Nutzereingabe, ^p0331
- der bisherige Gesprächs- oder Arbeitsverlauf, ^p0332
- bereitgestellte Dokumentauszüge, ^p0333
- Werkzeugbeschreibungen, ^p0334
- Tool-Ausgaben, ^p0335
- Zwischenergebnisse, ^p0336
- die erzeugte Antwort. ^p0337

Dieser technisch begrenzte Verarbeitungsraum wird als **Context Window** bezeichnet. Seine nominelle Größe gibt an, wie viele Tokens ein System grundsätzlich verarbeiten kann. Sie sagt jedoch nicht, dass alle enthaltenen Informationen gleich zuverlässig genutzt werden. ^p0338

Untersuchungen zu langen Kontexten zeigen, dass Position, Ablenkung und Umfang der bereitgestellten Information die Leistung beeinflussen können. Relevante Information kann in langen Eingaben schwerer auffindbar sein, insbesondere wenn sie zwischen ähnlichen oder widersprüchlichen Inhalten steht.[^4] ^p0339

Der Ausdruck **Context Rot** bezeichnet beobachtete Leistungsabfälle bei wachsender Kontextlänge. Er ist kein einzelner, abschließend geklärter technischer Mechanismus. Für agentische Arbeit ist der Begriff dennoch hilfreich: Während längerer Läufe sammeln sich Werkzeugausgaben, Fehlversuche, überholte Planungen und Zwischenstände an. Sie beanspruchen Tokens und können mit aktuell relevanter Information konkurrieren. ^p0340

Daraus folgt nicht, dass Kontext immer möglichst kurz sein sollte. Zu starke Reduktion kann Bedingungen, Unsicherheiten und Provenienz entfernen. Die Zielgröße ist ein **dichter und hinreichender Kontext**: so begrenzt wie möglich, aber so vollständig und differenziert wie für die Aufgabe erforderlich. ^p0341

## 4.3 Wie Informationen in den Modellkontext gelangen

Eine Datei im Projektordner ist nicht automatisch Teil des Context Window. Damit ihr Inhalt für das Modell verfügbar wird, muss das System sie lesen, extrahieren, transformieren oder durch ein Werkzeug untersuchen. ^p0342

Der Weg lässt sich schematisch darstellen: ^p0343

> **Datei oder Datenbestand → Werkzeug, Parser oder Skript → bereitgestellte Repräsentation → Tokenisierung → Context Window**
^p0344


Unterschiedliche Formate erfordern unterschiedliche Zugriffe: ^p0345

- Markdown und Quellcode können meist direkt gelesen werden. ^p0346
- CSV-Dateien können selektiv profiliert oder abgefragt werden. ^p0347
- Word-Dateien müssen strukturiert ausgelesen werden. ^p0348
- PDFs können Text, Layout und Bilder kombinieren. ^p0349
- Bilder werden multimodal verarbeitet oder in strukturierte Beschreibungen überführt. ^p0350
- Datenbanken werden über Abfragen genutzt, ohne vollständig in den Kontext geladen zu werden. ^p0351

Im Editionsprojekt kann der Agent ein Bild öffnen, ohne dessen Binärdaten als Tokens zu „lesen“. Ein multimodales System verarbeitet das Bild und erzeugt interne Repräsentationen. Ein Skript kann aus hundert TEI-Dateien nur jene Elemente zählen, die für eine aktuelle Modellierungsfrage relevant sind. In den Modellkontext gelangt dann die Ausgabe des Skripts, nicht zwingend der gesamte Datenbestand. ^p0352

Die methodisch relevante Einheit ist daher nicht die Datei als solche, sondern ihre **für das Modell bereitgestellte Repräsentation**. ^p0353

## 4.4 Context Compression und Distillation

Umfangreiche Informationsbestände enthalten häufig mehr Material, als für eine einzelne Aufgabe benötigt wird. Sie können Wiederholungen, alte Fassungen, implizite Voraussetzungen und widersprüchliche Aussagen enthalten. ^p0354

**Context Compression** reduziert die Menge des unmittelbar bereitgestellten Kontextes. Dazu gehören: ^p0355

- Auswahl relevanter Abschnitte, ^p0356
- Zusammenfassung, ^p0357
- Entfernung von Wiederholungen, ^p0358
- Aggregation von Daten, ^p0359
- Auswahl repräsentativer Beispiele, ^p0360
- Kompaktierung eines bisherigen Arbeitsverlaufs. ^p0361

Eine kürzere Fassung ist jedoch nicht automatisch besser. Eine Zusammenfassung kann Unsicherheit glätten, Begründungen entfernen oder mehrere alternative Aussagen in eine scheinbar eindeutige Regel verwandeln. ^p0362

**Distillation** geht deshalb über bloße Kompression hinaus. Sie überführt verfügbares Verständnis in eine selektive, strukturierte, inspizierbare und revidierbare Repräsentation. Für die digitale Edition kann eine Destillation beispielsweise festhalten: ^p0363

- welche Arten von Unsicherheit unterschieden werden; ^p0364
- wie sie in TEI repräsentiert werden; ^p0365
- welche Begründung hinter der Regel steht; ^p0366
- welche Ausnahmen bekannt sind; ^p0367
- wie Unsicherheit im Frontend sichtbar werden soll; ^p0368
- welche Fragen noch offen sind. ^p0369

Distillation umfasst drei Operationen: ^p0370

1. **Auswahl:** Was ist für den Gegenstand relevant? ^p0371
2. **Strukturierung:** Welche Begriffe, Regeln und Beziehungen müssen explizit werden? ^p0372
3. **Verdichtung:** Welche Redundanz kann entfernt werden, ohne notwendige Differenzierungen zu verlieren? ^p0373

Das Gegenrisiko ist **Überdestillation**. Sie liegt vor, wenn Provenienz, Unsicherheiten oder handlungsnotwendige Details verloren gehen. ^p0374

## 4.5 Project Knowledge Base, Working Context und Context Window

Zwischen drei Ebenen ist zu unterscheiden: ^p0375

**Abbildung 9: Project Knowledge Base, Working Context und Context Window.** ^p0376
*Die Project Knowledge Base enthält den persistenten Projektbestand. Der Working Context ist eine aufgabenspezifische Auswahl aus Wissensdokumenten, Daten, Instruktionen, Werkzeugbeschreibungen und aktuellen Rückmeldungen. Nur die tatsächlich bereitgestellte Repräsentation gelangt in das technisch begrenzte Context Window.* ^p0377

- Die **Project Knowledge Base** bewahrt den persistenten, inspizierbaren und revidierbaren Wissensbestand. ^p0378
- Der **Working Context** ist der für eine konkrete Aufgabe zusammengestellte Informationszustand. ^p0379
- Das **Context Window** ist der technische Verarbeitungsraum, in dem dieser Kontext vom Modell genutzt wird. ^p0380

Für die Aufgabe „TEI für Seite 17 erzeugen“ könnte der Working Context enthalten: ^p0381

Aktuelle Aufgabe ^p0382

├── page-017.jpg ^p0383

├── page-017.txt ^p0384

├── transcription-rules.md ^p0385

├── uncertainty.md ^p0386

├── relevanter Abschnitt aus tei-model.md ^p0387

├── zwei geprüfte Beispiele ^p0388

├── Schema- und Validierungsbefehl ^p0389

└── aktuelles Feedback des Validators ^p0390

Nicht enthalten sein müssen: ^p0391

- allgemeine Projektberichte, ^p0392
- Richtlinien zu anderen Quellentypen, ^p0393
- vollständige Protokolle, ^p0394
- alte Schema-Versionen, ^p0395
- nicht mehr relevante Fehlversuche. ^p0396

Die zentrale Unterscheidung lautet: ^p0397

> Knowledge Engineering baut und pflegt den Wissensbestand; Context Engineering stellt daraus und aus weiteren Ressourcen den für eine konkrete Aufgabe erforderlichen Kontext zusammen.
^p0398


## 4.6 Hands-on: Einen Working Context für eine TEI-Aufgabe zusammenstellen

### Aufgabe

Wählen Sie aus einem bereitgestellten Projektbestand jene Ressourcen aus, die ein Agent benötigt, um eine Seite korrekt als TEI zu modellieren. ^p0399

### Kategorien

Ordnen Sie jede Ressource einer Kategorie zu: ^p0400

1. unmittelbar laden, ^p0401
2. bei Bedarf nachladen, ^p0402
3. nur über ein Werkzeug abfragen, ^p0403
4. für diese Aufgabe nicht verwenden. ^p0404

### Beispielmatrix

| Ressource | Unmittelbar | Bei Bedarf | Tool-Zugriff | Nicht verwenden | Begründung |
| :---- | ----: | ----: | ----: | ----: | :---- |
| `page-017.jpg` | ✓ |  |  |  | Primärquelle |
| `transcription-rules.md` | ✓ |  |  |  | verbindliche Regeln |
| vollständiges Projektprotokoll |  |  |  | ✓ | zu breit und teilweise überholt |
| `edition.rng` |  |  | ✓ |  | durch Validator verwenden |
| zwei geprüfte TEI-Beispiele | ✓ |  |  |  | konkretisieren Grenzfälle |
| alte Schema-Version |  |  |  | ✓ | nicht maßgeblich |
^p0405


### Reflexion

- Welche Ressource ist wichtig, muss aber nicht vollständig in den Kontext? ^p0406
- Welche Information fehlt im Bestand? ^p0407
- Welche Auswahlentscheidung ist fachlich und nicht nur technisch? ^p0408

# 5\. Knowledge Engineering

## 5.1 Warum Projektwissen explizit werden muss

In einem Editionsprojekt ist Wissen häufig verteilt. Ein Teil steht in Richtlinien, ein Teil in E-Mails, ein Teil in TEI-Beispielen und ein Teil nur im Erfahrungswissen einzelner Editor:innen. Menschen, die lange am Projekt arbeiten, ergänzen fehlende Zusammenhänge oft unbewusst. Eine neue Person oder eine neue Agenteninstanz besitzt diesen Hintergrund nicht. ^p0409

Ein Agent kann zwar alle Dateien durchsuchen, aber daraus entsteht nicht automatisch ein konsistentes Projektverständnis. Er kann eine alte Regel mit einer neuen vermischen oder aus einem einzelnen Beispiel eine allgemeine Konvention ableiten. ^p0410

**Knowledge Engineering** betrifft den Aufbau und die Pflege expliziten, inspizierbaren und revidierbaren Projektwissens. Es macht relevante Begriffe, Regeln, Entscheidungen, Einschränkungen und Unsicherheiten so sichtbar, dass sie gelesen, kritisiert und fortgeschrieben werden können. ^p0411

Ziel ist keine vollständige Repräsentation aller verfügbaren Informationen. Eine Wissensbasis ist zweckgebunden. Sie hält jenen Teil des Wissens fest, der für bestimmte Formen der Arbeit, Entscheidung und Prüfung erforderlich ist. ^p0412

## 5.2 Knowledge Acquisition

Projektwissen stammt aus zwei grundlegenden Quellen: ^p0413

1. bereits vorhandenen Dokumenten und Daten; ^p0414
2. implizitem Wissen von Personen und Organisationen. ^p0415

Vorhandene Materialien können sein: ^p0416

- Forschungsdaten, ^p0417
- Publikationen, ^p0418
- editorische Richtlinien, ^p0419
- Datenmodelle, ^p0420
- Quellcode, ^p0421
- Protokolle, ^p0422
- frühere Artefakte. ^p0423

Implizites Wissen umfasst beispielsweise: ^p0424

- Gründe für frühere Entscheidungen, ^p0425
- bekannte Ausnahmen, ^p0426
- Erwartungen an das Zielartefakt, ^p0427
- Kriterien für Akzeptanz, ^p0428
- praktische Erfahrungen mit bestimmten Quellentypen. ^p0429

**Knowledge Acquisition** bezeichnet die Erhebung und Explizierung dieses relevanten Wissens. Mögliche Verfahren sind Dokumentenanalyse, Interviews, Workshops, Beobachtung von Arbeitsabläufen, Fehleranalyse und gemeinsame Modellierungssitzungen. ^p0430

Im Editionsprojekt könnte ein Interview ergeben, dass `<supplied>` nur verwendet werden darf, wenn eine Ergänzung mit hoher Sicherheit aus dem unmittelbaren Kontext erschlossen werden kann. Diese Regel steht vielleicht nicht in der alten Richtlinie, wird aber seit Jahren praktiziert. Knowledge Acquisition macht sie sichtbar; Distillation überführt sie anschließend in eine überprüfbare Form. ^p0431

## 5.3 Project Knowledge Base

Eine Sammlung von Dateien ist noch keine Wissensbasis. ^p0432

Eine **Project Knowledge Base** ist der persistente, inspizierbare und revidierbare Bestand des dokumentierten Projektwissens. Sie hält die gegenwärtige Auffassung des Projekts über seine Daten, seinen Zweck und die relevanten Entscheidungen fest. ^p0433

Für eine digitale Edition kann sie enthalten: ^p0434

knowledge/ ^p0435

├── research-context.md ^p0436

├── source-description.md ^p0437

├── transcription-rules.md ^p0438

├── terminology.md ^p0439

├── tei-model.md ^p0440

├── entities.md ^p0441

├── uncertainty.md ^p0442

├── requirements.md ^p0443

├── design.md ^p0444

├── verification.md ^p0445

└── decisions.md ^p0446

Die Wissensbasis ersetzt Quellen und Forschungsdaten nicht. Sie beschreibt und kontextualisiert deren Verwendung. `source-description.md` ist nicht die Quelle. `tei-model.md` ist nicht die TEI-Datei. Beide dokumentieren jedoch, wie mit den Quellen und Daten gearbeitet werden soll. ^p0447

## 5.4 Wissensdokumente

Ein Editionsprojekt kann seine Regeln in einer langen Richtlinie, mehreren E-Mails und mündlich weitergegebenem Erfahrungswissen verteilen. Für eine konkrete Aufgabe ist ein solcher Bestand schwer nutzbar. Ein Agent müsste die relevanten Aussagen jedes Mal neu suchen und könnte widersprüchliche Fassungen miteinander vermischen. ^p0448

Ein Wissensdokument führt die für einen abgegrenzten Gegenstand relevanten Aussagen in einer überprüfbaren Form zusammen. Es kann beispielsweise festhalten, wie unsichere Lesungen markiert werden, welche Ausnahmen gelten und wie diese Unsicherheit im Frontend sichtbar werden soll. ^p0449

Ein **Wissensdokument** ist eine begrenzte, strukturierte und revidierbare Repräsentation relevanten Wissens, die aus einem umfangreicheren Bestand destilliert, von Menschen geprüft und von LLM-basierten Systemen als Kontext genutzt werden kann. ^p0450

Wichtige Eigenschaften sind: ^p0451

- klar abgegrenzter Gegenstand, ^p0452
- nachvollziehbare Struktur, ^p0453
- sichtbare Unsicherheiten, ^p0454
- dokumentierte Provenienz, ^p0455
- Revidierbarkeit, ^p0456
- duale Lesbarkeit für Menschen und LLM-basierte Systeme. ^p0457

Beispiel: ^p0458

\--- ^p0459

document\_type: knowledge ^p0460

status: reviewed ^p0461

topic: uncertain readings ^p0462

sources: ^p0463

  \- editorial-guidelines-v2.pdf ^p0464

  \- workshop-2026-04-12.md ^p0465

\--- ^p0466

\<a id="unsichere-lesungen"\>\</a\> ^p0467

\# Unsichere Lesungen ^p0468

\<a id="grundregel"\>\</a\> ^p0469

\#\# Grundregel ^p0470

Eine lesbare, aber nicht sicher identifizierbare Zeichenfolge wird mit ^p0471

\`\<unclear\>\` ausgezeichnet. ^p0472

\<a id="unleserliche-stellen"\>\</a\> ^p0473

\#\# Unleserliche Stellen ^p0474

Ist keine belastbare Zeichenfolge erkennbar, wird keine hypothetische ^p0475

Lesung als regulärer Text eingetragen. ^p0476

\<a id="erganzungen"\>\</a\> ^p0477

\#\# Ergänzungen ^p0478

\`\<supplied\>\` wird nur verwendet, wenn eine Ergänzung durch den unmittelbaren ^p0479

Kontext begründet ist. Die Begründung muss nachvollziehbar bleiben. ^p0480

\<a id="darstellung-im-frontend"\>\</a\> ^p0481

\#\# Darstellung im Frontend ^p0482

Unsichere Lesungen werden visuell markiert. Die Benutzeroberfläche darf ^p0483

sie nicht wie sicheren Text darstellen. ^p0484

\<a id="offene-frage"\>\</a\> ^p0485

\#\# Offene Frage ^p0486

Für teilweise lesbare Eigennamen ist noch zu klären, ob Zeichen- oder ^p0487

Wortebene ausgezeichnet wird. ^p0488

## 5.5 Markdown als technische Repräsentation

Das Wissensdokument ist ein konzeptionelles Artefakt und nicht an ein bestimmtes Dateiformat gebunden. Im hier beschriebenen Workflow wird Markdown verwendet, weil es offen, textbasiert und sowohl für Menschen als auch für LLM-basierte Systeme gut lesbar ist. ^p0489

Markdown trennt Struktur und Inhalt durch einfache Zeichen: ^p0490

- `#` für Überschriften, ^p0491
- Listenpunkte, ^p0492
- Links, ^p0493
- Tabellen, ^p0494
- Codeblöcke. ^p0495

Vorteile: ^p0496

- mit unterschiedlichen Editoren lesbar; ^p0497
- zeilenweise versionierbar; ^p0498
- einfach referenzierbar; ^p0499
- in Obsidian oder anderen Systemen verlinkbar; ^p0500
- gezielt in Working Contexts aufnehmbar. ^p0501

Markdown macht Inhalte nicht automatisch korrekt. Es schafft lediglich eine Form, in der Menschen und Agents am selben dokumentierten Bestand arbeiten können. ^p0502

## 5.6 Instruktionsdateien und Agent Skills

Nicht jede persistente Information ist ein Wissensdokument. ^p0503

### Wissensdokument

Beschreibt, was über einen Gegenstand bekannt ist: ^p0504

- `uncertainty.md` ^p0505
- `tei-model.md` ^p0506
- `requirements.md` ^p0507

### Instruktionsdatei

Legt wiederkehrende Regeln für agentische Arbeit fest, etwa in `CLAUDE.md` oder `AGENTS.md`: ^p0508

\<a id="arbeitsweise"\>\</a\> ^p0509

\#\# Arbeitsweise ^p0510

\- Verändere keine Quelldateien. ^p0511

\- Lies vor jeder TEI-Änderung die relevanten Wissensdokumente. ^p0512

\- Trenne technische Fehler von fachlichen Fragen. ^p0513

\- Melde eine Aufgabe erst als abgeschlossen, nachdem die vorgesehenen ^p0514

  Validatoren und Tests ausgeführt wurden. ^p0515

### Agent Skill

Bündelt Instruktionen, Skripte und Ressourcen für eine wiederkehrende Aufgabenklasse. Ein Skill könnte beschreiben, wie: ^p0516

- TEI-Dateien validiert werden, ^p0517
- ein Datenprofil erzeugt wird, ^p0518
- eine Editionsseite transformiert wird, ^p0519
- ein Acceptance Report erstellt wird. ^p0520

Die Unterscheidung lautet: ^p0521

> Ein Wissensdokument beschreibt den Gegenstand. Eine Instruktionsdatei regelt die wiederkehrende Arbeit. Ein Skill operationalisiert ein wiederverwendbares Verfahren. Ein Prompt formuliert die aktuelle Aufgabe.
^p0522


## 5.7 Governance und Kuration

Wissensbasen verlieren ohne Pflege an Nutzbarkeit. Dokumente werden veraltet, Begriffe uneinheitlich und parallele Fassungen widersprüchlich. ^p0523

**Governance** bestimmt Regeln für Aufbau, Änderung und Nutzung. **Kuration** wendet diese Regeln auf den konkreten Bestand an. ^p0524

Strukturelle Kuration betrifft: ^p0525

- Dateinamen, ^p0526
- Metadaten, ^p0527
- Links, ^p0528
- Dokumenttypen, ^p0529
- Versionsangaben, ^p0530
- Dubletten. ^p0531

Inhaltliche Kuration betrifft: ^p0532

- widersprüchliche Aussagen, ^p0533
- veraltete Regeln, ^p0534
- fehlende Einschränkungen, ^p0535
- unangemessene Verdichtungen, ^p0536
- Revision von Anforderungen. ^p0537

Ein Agent kann Probleme lokalisieren und Vorschläge erzeugen. Inhaltlich folgenreiche Änderungen müssen jedoch geprüft und verantwortet werden. ^p0538

## 5.8 Hands-on: Ein Wissensdokument zu editorischer Unsicherheit destillieren

### Ausgangsmaterial

- zwei Richtlinienauszüge, ^p0539
- drei E-Mails, ^p0540
- ein Protokoll, ^p0541
- zwei TEI-Beispiele, ^p0542
- eine mündlich ergänzte Projektregel. ^p0543

### Auftrag

1. Identifizieren Sie relevante Aussagen. ^p0544
2. Markieren Sie Widersprüche. ^p0545
3. Trennen Sie verbindliche Regeln, Beispiele und offene Fragen. ^p0546
4. Erstellen Sie `uncertainty.md`. ^p0547
5. Dokumentieren Sie die Quellen. ^p0548
6. Prüfen Sie, welche Information bei der Verdichtung verloren gehen könnte. ^p0549

### Prüfkriterien

- Sind Unsicherheiten sichtbar? ^p0550
- Wurden Ausnahmen erhalten? ^p0551
- Ist die Provenienz nachvollziehbar? ^p0552
- Ist das Dokument kompakt, aber hinreichend? ^p0553
- Kann es unmittelbar als Kontext für eine TEI-Aufgabe verwendet werden? ^p0554

# 6\. Agentic Engineering

## 6.1 Warum mehrschrittige Arbeit organisiert werden muss

Mit wachsender Aufgabendauer steigt nicht nur die mögliche Leistung eines Agents, sondern auch die Zahl der Stellen, an denen Fehler in spätere Schritte eingehen können. ^p0555

Ein Agent liest eine veraltete Richtlinie, erzeugt daraufhin ein ungeeignetes TEI-Muster, transformiert dieses in HTML und passt anschließend das Frontend an die falsche Struktur an. Jeder einzelne Schritt kann technisch plausibel wirken. Der ursprüngliche Fehler wird dennoch über die gesamte Arbeitstrajektorie fortgeschrieben. ^p0556

**Agentic Engineering** bezeichnet die systematische Organisation und Kontrolle mehrschrittiger agentischer Arbeit. Es betrifft: ^p0557

- Abgrenzung und Zerlegung von Aufgaben, ^p0558
- Werkzeugnutzung, ^p0559
- Verarbeitung von Zwischenergebnissen, ^p0560
- Zustände und Übergaben, ^p0561
- Abbruch- und Eskalationsbedingungen, ^p0562
- Prüfung und Fortführung. ^p0563

Die zentrale Frage lautet nicht nur, ob ein Agent handeln kann, sondern unter welchen Bedingungen seine Handlungen nachvollziehbar, begrenzt und korrigierbar bleiben. ^p0564

## 6.2 Agentische Ausführungsschleife

Eine vereinfachte Ausführungsschleife lautet: ^p0565

**Abbildung 10: Agentische Ausführungsschleife.** ^p0566
*Der Agent erfasst den aktuellen Projektzustand, plant einen begrenzten nächsten Schritt, verwendet ein Werkzeug, beobachtet dessen Ergebnis und aktualisiert sein Vorgehen. Der Zyklus bleibt an dokumentierte Anforderungen, Berechtigungen, Abbruchbedingungen und menschliche Interventionspunkte gebunden.* ^p0567

> **Zustand erfassen → nächsten Schritt planen → Werkzeug oder Aktion ausführen → Ergebnis beobachten → Vorgehen aktualisieren**
^p0568


Im Editionsprojekt: ^p0569

1. Agent liest Aufgabe und relevante Wissensdokumente. ^p0570
2. Agent untersucht die vorhandene Transkription. ^p0571
3. Agent erzeugt TEI. ^p0572
4. Agent führt Schema-Validierung aus. ^p0573
5. Agent liest Fehlermeldungen. ^p0574
6. Agent korrigiert technische Fehler. ^p0575
7. Agent dokumentiert verbleibende fachliche Unsicherheiten. ^p0576
8. Agent transformiert TEI in HTML. ^p0577
9. Agent prüft die Darstellung. ^p0578
10. Agent schlägt Write-back vor. ^p0579

Autonomie bezeichnet dabei den Umfang der Arbeit zwischen zwei menschlichen Eingriffen. Sie bedeutet nicht Abwesenheit menschlicher Kontrolle. ^p0580

## 6.3 Planung, Ausführung und Feedback

Komplexe Aufgaben können in Planung und Ausführung getrennt werden. Ein Plan sollte bestimmen: ^p0581

- welche Teilprobleme vorliegen, ^p0582
- welche Informationen fehlen, ^p0583
- welche Werkzeuge benötigt werden, ^p0584
- welche Prüfungen vorgesehen sind, ^p0585
- welche Reihenfolge sinnvoll ist. ^p0586

Planung ist jedoch kein Selbstzweck. Ein umfangreicher Plan vor der Untersuchung des Projektbestands kann falsche Sicherheit erzeugen. Gute Pläne sind kompakt, gegen den aktuellen Zustand prüfbar und revidierbar. ^p0587

Feedback kann aus unterschiedlichen Quellen stammen: ^p0588

- Validatoren, ^p0589
- Tests, ^p0590
- Fehlermeldungen, ^p0591
- Werkzeugausgaben, ^p0592
- Reviews anderer Agents, ^p0593
- menschliche Rückmeldungen, ^p0594
- veränderte Anforderungen. ^p0595

Agentic Engineering organisiert, wie dieses Feedback in weitere Schritte überführt wird. ^p0596

## 6.4 Werkzeuge, Berechtigungen und Reversibilität

Werkzeuge erweitern ein LLM von einem Textgenerator zu einem System, das auf eine Umgebung einwirken kann. Dazu gehören: ^p0597

- Dateizugriff, ^p0598
- Terminal, ^p0599
- Codeausführung, ^p0600
- Websuche, ^p0601
- Datenbankabfragen, ^p0602
- Browsersteuerung, ^p0603
- Validatoren, ^p0604
- spezialisierte APIs. ^p0605

Ein Werkzeugaufruf kann den Projektzustand verändern. Daher sollten Zugriffe nach dem Prinzip der geringsten erforderlichen Berechtigung vergeben werden. ^p0606

Im Editionsprojekt: ^p0607

- Quelldateien dürfen gelesen, aber nicht überschrieben werden. ^p0608
- Generierte TEI-Dateien dürfen in einem Arbeitsordner verändert werden. ^p0609
- Schema-Validatoren dürfen ohne Bestätigung laufen. ^p0610
- Veröffentlichungs- oder Deployment-Schritte benötigen eine explizite Freigabe. ^p0611
- Änderungen sollten versioniert und reversibel bleiben. ^p0612

## 6.5 MCP, Subagents und Agent-to-Agent-Kommunikation

Das **Model Context Protocol (MCP)** standardisiert die Verbindung von LLM-Anwendungen mit Werkzeugen und Datenquellen. Ein MCP-Server kann beispielsweise Zugriff auf ein Repository, eine Datenbank oder einen Validator bereitstellen.[^5] ^p0613

MCP löst ein technisches Integrationsproblem. Es entscheidet nicht, ob ein Werkzeug für die Aufgabe geeignet ist oder wie seine Ergebnisse fachlich interpretiert werden. ^p0614

Ein **Subagent** ist eine abgegrenzte Agenteninstanz mit einer Teilaufgabe. Im Editionsprojekt könnten parallel arbeiten: ^p0615

- ein Agent für Datenprofil und TEI-Struktur, ^p0616
- ein Agent für Schema-Validierung, ^p0617
- ein Agent für Frontend-Tests, ^p0618
- ein Agent für den Vergleich von Anforderungen und Implementation. ^p0619

Mehr Agents erzeugen nicht automatisch bessere Ergebnisse. Sie erhöhen Koordinations- und Prüfaufwand. Jeder Subagent benötigt einen klaren Auftrag, begrenzten Kontext, ein definiertes Rückgabeformat und Regeln für Unsicherheit. ^p0620

Agent-to-Agent-Protokolle verbinden eigenständige Agents. Die methodischen Fragen bleiben: ^p0621

- Welche Zuständigkeit besitzt jeder Agent? ^p0622
- Welche Informationen werden übergeben? ^p0623
- Wie werden Konflikte sichtbar? ^p0624
- Wer entscheidet bei widersprüchlichen Ergebnissen? ^p0625

## 6.6 Versionierte Zwischenstände und menschliche Intervention

Mehrschrittige Arbeit sollte in überprüfbaren Inkrementen erfolgen. Ein sinnvoller Zwischenstand ist: ^p0626

- ausführbar oder untersuchbar, ^p0627
- einem definierten Projektzustand zuordenbar, ^p0628
- gegen Anforderungen prüfbar, ^p0629
- klein genug, um Fehlerursachen zu rekonstruieren. ^p0630

Zwischenergebnisse sollten nicht ausschließlich im Chatverlauf verbleiben. Relevante Pläne, Entscheidungen, Prüfergebnisse und offene Fragen gehören in persistente Projektartefakte. ^p0631

Typische menschliche Interventionspunkte sind: ^p0632

- widersprüchliche Anforderungen, ^p0633
- fehlende fachliche Grundlagen, ^p0634
- schwer reversible Änderungen, ^p0635
- sensible Ressourcen, ^p0636
- fachlich folgenreiche Modellierungsentscheidungen, ^p0637
- Validierung und Acceptance. ^p0638

Agents können Evidenz sammeln. Sie übernehmen dadurch nicht automatisch die Autorität, ein Ergebnis fachlich zu validieren oder für einen Zweck zu akzeptieren. ^p0639

## 6.7 Hands-on: TEI erzeugen, validieren und ein Frontend implementieren

### Teil A: TEI erzeugen

Der Agent erhält: ^p0640

- Seitenbild, ^p0641
- Rohtranskription, ^p0642
- Wissensdokumente, ^p0643
- Schema, ^p0644
- zwei geprüfte Beispiele. ^p0645

Auftrag: ^p0646

1. TEI erzeugen, ^p0647
2. Schema validieren, ^p0648
3. technische Fehler korrigieren, ^p0649
4. fachliche Unsicherheiten separat dokumentieren. ^p0650

### Teil B: Frontend implementieren

Das lokale Frontend soll zeigen: ^p0651

- Faksimile, ^p0652
- diplomatische Transkription, ^p0653
- normalisierte Ansicht, ^p0654
- Unsicherheiten, ^p0655
- Annotationen. ^p0656

### Teil C: Rückkopplung prüfen

Fragen: ^p0657

- Sind Seiten- und Zeilenwechsel sichtbar? ^p0658
- Werden Unsicherheiten als Unsicherheiten dargestellt? ^p0659
- Erzeugt die Oberfläche falsche Eindeutigkeit? ^p0660
- Welche Modellierungsprobleme werden erst im Interface sichtbar? ^p0661
- Welche Wissensdokumente müssen revidiert werden? ^p0662

# 7\. Promptotyping

## 7.1 Definition und Grundprinzip

Promptotyping ist eine iterative, dokumentenbasierte Methode zur Entwicklung projektspezifischer digitaler Forschungsartefakte mit LLM-basierten AI Agents. ^p0663

Der Begriff bezeichnet nicht lediglich das Erzeugen eines Prototyps durch Prompts. Im Mittelpunkt steht die gemeinsame Entwicklung von: ^p0664

- dokumentiertem Projektverständnis, ^p0665
- digitalem Forschungsartefakt, ^p0666
- Prüfverfahren, ^p0667
- begrenzten Gründen der Akzeptanz. ^p0668

Der grundlegende Zyklus lautet: ^p0669

**Abbildung 11: Promptotyping als geschlossener Entwicklungszyklus.** ^p0670
*Projektwissen wird für eine Aufgabe in einen Working Context überführt und durch einen Agenten in ein digitales Forschungsartefakt operationalisiert. Verification und Validation erzeugen Evidenz und neue Erkenntnisse. Write-back führt diese Erkenntnisse in Wissensdokumente, Anforderungen und Modelle zurück.* ^p0671

> **Projektwissen → Working Context → agentische Implementation → digitales Forschungsartefakt → Prüfung → Revision des Projektwissens**
^p0672


Das Artefakt und das dokumentierte Projektverständnis entwickeln sich gemeinsam weiter. ^p0673

## 7.2 Preparation

Preparation macht Daten, Quellen, Standards und Forschungskontext zugänglich. ^p0674

Für die digitale Edition umfasst dies: ^p0675

- Seitenbilder beschaffen und eindeutig benennen; ^p0676
- Provenienz dokumentieren; ^p0677
- vorhandene Transkriptionen sichern; ^p0678
- Richtlinien und Schema-Versionen sammeln; ^p0679
- Ausgangsdateien vor Veränderungen schützen; ^p0680
- Projektstruktur anlegen. ^p0681

Preparation ist mehr als Dateiverwaltung. Sie schafft einen nachvollziehbaren Ausgangszustand. ^p0682

## 7.3 Exploration

Exploration untersucht, was die Daten und Quellen ermöglichen und begrenzen. ^p0683

Im Editionsprojekt kann sie zeigen: ^p0684

- welche Seitentypen vorliegen; ^p0685
- welche Schriften und Layouts auftreten; ^p0686
- welche wiederkehrenden editorischen Phänomene vorhanden sind; ^p0687
- wo die Rohtranskription unsicher ist; ^p0688
- welche Anforderungen das Frontend an das Modell stellt. ^p0689

Exploration erzeugt noch keine endgültige Spezifikation. Sie macht sichtbar, welche Fragen geklärt und welche Entscheidungen dokumentiert werden müssen. ^p0690

## 7.4 Distillation

Distillation überführt das entwickelte Verständnis in gepflegte Dokumente: ^p0691

- `source-description.md` ^p0692
- `transcription-rules.md` ^p0693
- `tei-model.md` ^p0694
- `requirements.md` ^p0695
- `design.md` ^p0696
- `verification.md` ^p0697

Diese Dokumente bilden die Grundlage weiterer agentischer Arbeit. Sie bleiben revidierbar, weil neue Erkenntnisse aus der Implementation frühere Annahmen verändern können. ^p0698

## 7.5 Requirements Engineering und Scholar-Centred Design

Requirements Engineering macht explizit, was ein Artefakt leisten soll. In einem wissenschaftlichen Projekt reicht es nicht, „eine schöne digitale Edition“ zu verlangen. ^p0699

Anforderungen können lauten: ^p0700

- Faksimile und Transkription müssen eindeutig zugeordnet sein. ^p0701
- Diplomatische und normalisierte Lesung müssen unterscheidbar bleiben. ^p0702
- Unsichere Lesungen dürfen nicht wie sicherer Text erscheinen. ^p0703
- Editorische Eingriffe müssen nachvollziehbar sein. ^p0704
- Quelldaten dürfen nicht stillschweigend verändert werden. ^p0705
- Das Artefakt muss lokal und ohne proprietären Dienst ausführbar sein. ^p0706

**Scholar-Centred Design** richtet die Entwicklung an den Forschungspraktiken, Interpretationsaufgaben und Verantwortlichkeiten der beteiligten Wissenschaftler:innen aus. Es fragt nicht nur, ob eine Oberfläche benutzbar ist, sondern welche wissenschaftlichen Unterscheidungen sie sichtbar oder unsichtbar macht. ^p0707

## 7.6 Implementation

Implementation macht die Wissensbasis handlungsfähig. Der Agent übersetzt dokumentierte Anforderungen in: ^p0708

- TEI-Dateien, ^p0709
- Transformationsskripte, ^p0710
- Stylesheets, ^p0711
- Tests, ^p0712
- ein lokales Frontend, ^p0713
- Dokumentation. ^p0714

Implementation ist keine neutrale Ausführung einer vollständig bestimmten Spezifikation. Erst durch das funktionierende Artefakt kann sichtbar werden, dass eine Regel fehlt oder eine Modellierung zu grob ist. ^p0715

Ein Beispiel: Im TEI-Modell werden alle unsicheren Lesungen gleich behandelt. Im Frontend zeigt sich jedoch, dass zwischen „teilweise lesbar“, „editorisch ergänzt“ und „vollständig unleserlich“ unterschieden werden muss. Diese Erkenntnis gehört nicht nur in den Code, sondern zurück in das Wissensdokument und gegebenenfalls in das Datenmodell. ^p0716

## 7.7 Verification, Validation und Acceptance

Drei Ebenen müssen unterschieden werden. ^p0717

**Abbildung 12: Prüfung, Evidenz und verantwortliche Acceptance.** ^p0718
*Deterministische Validation und agentisches Review liefern überprüfbare Evidenz. Die fachliche und wissenschaftliche Beurteilung verbleibt beim Critical Expert. Erst diese verantwortliche Prüfung kann zu einer zweckgebundenen Acceptance führen; technische Konformität allein autorisiert kein Forschungsartefakt.* ^p0719

### Technische Verifikation

Prüft Konformität mit formalisierten Anforderungen: ^p0720

- XML ist wohlgeformt; ^p0721
- TEI entspricht dem Schema; ^p0722
- Tests laufen erfolgreich; ^p0723
- Transformationen erzeugen die erwarteten Dateien; ^p0724
- Quelldateien wurden nicht verändert. ^p0725

### Fachliche und wissenschaftliche Validierung

Prüft, ob Repräsentation und Artefakt für den vorgesehenen Forschungszweck angemessen sind: ^p0726

- Entspricht die Transkription der Quelle? ^p0727
- Sind editorische Unsicherheiten angemessen repräsentiert? ^p0728
- Unterstützt das Interface die vorgesehenen Interpretationshandlungen? ^p0729
- Werden Modellierungsentscheidungen sichtbar oder irreführend naturalisiert? ^p0730

### Acceptance

Bezeichnet die verantwortliche Entscheidung, einen identifizierbaren Projektzustand für einen benannten Zweck anzunehmen. ^p0731

Ein technisch verifiziertes Artefakt kann wissenschaftlich ungeeignet sein. Umgekehrt kann ein wissenschaftlich interessanter Demonstrator technisch noch nicht publikationsreif sein. Acceptance muss deshalb zweckgebunden formuliert werden. ^p0732

## 7.8 Critical Expert

Der **Critical Expert** trägt die Verantwortung dort, wo Prüfung Quellenkenntnis, Interpretation oder Designurteil verlangt. ^p0733

Agents und Validatoren können: ^p0734

- Fehler lokalisieren, ^p0735
- Kriterien anwenden, ^p0736
- Unterschiede berichten, ^p0737
- Evidenz zusammenstellen. ^p0738

Der Critical Expert entscheidet: ^p0739

- welche Lesung vertretbar ist; ^p0740
- ob eine Modellierung der Quelle angemessen entspricht; ^p0741
- ob die Oberfläche wissenschaftliche Differenzierungen erhält; ^p0742
- ob der Zustand für den benannten Zweck akzeptiert wird. ^p0743

Die Rolle ist nicht auf eine einzelne Person beschränkt. Sie bezeichnet die verantwortliche fachliche Autorität im Projekt. ^p0744

## 7.9 Write-back

Implementation und Prüfung erzeugen neues Wissen. Dieses Wissen muss in die zuständigen Dokumente zurückgeschrieben werden. ^p0745

Mögliche Write-backs: ^p0746

- Transkriptionsregel präzisieren; ^p0747
- neuen Unsicherheitstyp ergänzen; ^p0748
- Datenmodell revidieren; ^p0749
- Designentscheidung begründen; ^p0750
- bekannte Einschränkung dokumentieren; ^p0751
- Verifikationskriterium erweitern. ^p0752

Write-back verhindert, dass relevantes Wissen nur im Chat, im Code oder im Gedächtnis einzelner Personen verbleibt. ^p0753

## 7.10 Der Promptotype

Ein **Promptotype** ist der dokumentierte und referenzierbare Zustand einer Iteration. Er umfasst: ^p0754

- den relevanten Stand der Project Knowledge Base, ^p0755
- das digitale Forschungsartefakt, ^p0756
- den referenzierten Datenzustand, ^p0757
- dokumentierte Prüfungen, ^p0758
- offene Fragen, ^p0759
- die begrenzten Gründe der Acceptance. ^p0760

Ein Promptotype ist kein endgültiges Produkt. Er ist ein hinreichend bestimmter Zustand, von dem weitere Arbeit ausgehen kann. ^p0761

## 7.11 Hands-on: Write-back und Acceptance dokumentieren

### Write-back

Analysieren Sie die Implementation und dokumentieren Sie: ^p0762

- neue Erkenntnisse über die Quelle, ^p0763
- neue Anforderungen, ^p0764
- unzureichende Regeln, ^p0765
- offene fachliche Fragen, ^p0766
- notwendige Änderungen an Datenmodell oder Frontend. ^p0767

### Acceptance Statement

\<a id="acceptance-statement-2"\>\</a\> ^p0768

\# Acceptance Statement ^p0769

\<a id="identifizierter-zustand"\>\</a\> ^p0770

\#\# Identifizierter Zustand ^p0771

\- Knowledge Base: Commit \`abc123\` ^p0772

\- TEI-Daten: Version \`0.3\` ^p0773

\- Frontend: Build \`2026-08-01\` ^p0774

\- Schema: \`edition.rng\`, Version \`1.2\` ^p0775

\<a id="accepted-for"\>\</a\> ^p0776

\#\# Accepted for ^p0777

Interner Demonstrator zur Prüfung des TEI-Modells und der synoptischen ^p0778

Darstellung von Faksimile, diplomatischer Transkription und Normalisierung. ^p0779

\<a id="technisch-verifiziert"\>\</a\> ^p0780

\#\# Technisch verifiziert ^p0781

\- XML-Wohlgeformtheit ^p0782

\- Schema-Konformität ^p0783

\- erfolgreiche lokale Transformation ^p0784

\- unveränderte Quelldateien ^p0785

\- Navigation zwischen den Beispielseiten ^p0786

\<a id="fachlich-gepruft"\>\</a\> ^p0787

\#\# Fachlich geprüft ^p0788

\- Zuordnung von Faksimile und Transkription ^p0789

\- Darstellung der markierten Unsicherheiten ^p0790

\- Nachvollziehbarkeit editorischer Eingriffe ^p0791

\<a id="nicht-nachgewiesen"\>\</a\> ^p0792

\#\# Nicht nachgewiesen ^p0793

\- vollständige philologische Verifikation des Korpus ^p0794

\- Eignung für eine öffentliche oder zitierfähige Edition ^p0795

\- Barrierefreiheit und produktive Langzeitverfügbarkeit ^p0796

\<a id="offene-fragen"\>\</a\> ^p0797

\#\# Offene Fragen ^p0798

\- Unterscheidung zwischen teilweise lesbaren und ergänzten Eigennamen ^p0799

\- Darstellung konkurrierender Normalisierungen ^p0800

# 8\. Zusammenfassung und Begriffsübersicht

Die vier Engineering-Ebenen erfüllen unterschiedliche Funktionen: ^p0801

| Ebene | Gegenstand | Leitfrage |
| :---- | :---- | :---- |
| Prompt Engineering | aktuelle Eingabesequenz | Wie wird die Aufgabe formuliert? |
| Knowledge Engineering | persistenter Wissensbestand | Was muss explizit dokumentiert und gepflegt werden? |
| Context Engineering | Informationszustand einer Aufgabe | Welche Informationen benötigt der Agent jetzt? |
| Agentic Engineering | mehrschrittige Ausführung | Wie wird die Arbeit organisiert, begrenzt und geprüft? |
^p0802


Promptotyping verbindet diese Ebenen in einem iterativen Forschungsworkflow. ^p0803

Die zentrale Formel lautet: ^p0804

> **Prompt Engineering gestaltet die aktuelle Eingabesequenz.**
> **Context Engineering organisiert den Informationszustand einer Aufgabe.**
> **Knowledge Engineering baut und pflegt den dafür verfügbaren Wissensbestand.**
> **Agentic Engineering organisiert die mehrschrittige Ausführung.**
> **Promptotyping verbindet diese Ebenen in der iterativen Entwicklung und verantwortlichen Prüfung digitaler Forschungsartefakte.**
^p0805


Die digitale Edition zeigt, warum diese Verbindung notwendig ist. Quelle, Transkription, Datenmodell, Transformation und Frontend bilden keinen neutralen technischen Ablauf. Jede Stufe enthält Entscheidungen darüber, welche Unterschiede sichtbar, bearbeitbar und interpretierbar werden. AI Agents können diese Arbeit erheblich unterstützen. Sie können jedoch die fachliche Verantwortung für Repräsentation, Validierung und Acceptance nicht übernehmen. ^p0806

# 9\. Literaturverzeichnis

Anthropic. 2025\. “Claude’s Character.” Anthropic Research. ^p0807

Anthropic. 2026\. “Claude’s Constitution.” Anthropic. ^p0808

Battle, Rick, and Teja Gollapudi. 2024\. “The Unreasonable Effectiveness of Eccentric Automatic Prompts.” arXiv:2402.10949. ^p0809

Hong, Kelly, Anton Troynikov, and Jeff Huber. 2025\. “Context Rot: How Increasing Input Tokens Impacts LLM Performance.” Chroma Research. ^p0810

Hu, Tiancheng, and Nigel Collier. 2024\. “Quantifying the Persona Effect in LLM Simulations.” arXiv:2402.10811. ^p0811

Li, Cheng, Jindong Wang, Yixuan Zhang, Kaijie Zhu, Wenxin Hou, Jianxun Lian, Fang Luo, Qiang Yang, and Xing Xie. 2023\. “Large Language Models Understand and Can Be Enhanced by Emotional Stimuli.” arXiv:2307.11760. ^p0812

Lindsey, Jack, Wes Gurnee, Emmanuel Ameisen, et al. 2025\. “On the Biology of a Large Language Model.” Transformer Circuits. ^p0813

Mei, et al. 2025\. “Context Engineering for Large Language Models.” arXiv:2507.13334. ^p0814

Pollin, Christopher. 2026\. “Asymmetric Amplification.” Digital Humanities Craft. ^p0815

Pollin, Christopher. 2026\. “Promptotyping.” Manuskript in Vorbereitung. ^p0816

Rajeev, Meghana, Rajkumar Ramamurthy, Prapti Trivedi, et al. 2025\. “Cats Confuse Reasoning LLM: Query Agnostic Adversarial Triggers for Reasoning Models.” arXiv:2503.01781. ^p0817

Schulhoff, Sander, Michael Ilie, Nishant Balepur, Konstantine Kahadze, Amanda Liu, et al. 2024\. “The Prompt Report: A Systematic Survey of Prompting Techniques.” arXiv:2406.06608. ^p0818

Yin, Ziqi, Hao Wang, Kaito Horio, Daisuke Kawahara, and Satoshi Sekine. 2024\. “Should We Respect LLMs? A Cross-Lingual Study on the Influence of Prompt Politeness on LLM Performance.” arXiv:2402.14531. ^p0819

# 10\. Anhang: Vorlagen

## A. Vorlage für ein Wissensdokument

\--- ^p0820

document\_type: knowledge ^p0821

status: draft ^p0822

owner: ^p0823

sources: ^p0824

last\_reviewed: ^p0825

\--- ^p0826

\<a id="gegenstand"\>\</a\> ^p0827

\# Gegenstand ^p0828

\<a id="zweck"\>\</a\> ^p0829

\#\# Zweck ^p0830

\<a id="begriffe-und-unterscheidungen"\>\</a\> ^p0831

\#\# Begriffe und Unterscheidungen ^p0832

\<a id="regeln"\>\</a\> ^p0833

\#\# Regeln ^p0834

\<a id="einschrankungen-und-ausnahmen"\>\</a\> ^p0835

\#\# Einschränkungen und Ausnahmen ^p0836

\<a id="unsicherheiten"\>\</a\> ^p0837

\#\# Unsicherheiten ^p0838

\<a id="offene-fragen-2"\>\</a\> ^p0839

\#\# Offene Fragen ^p0840

\<a id="quellen"\>\</a\> ^p0841

\#\# Quellen ^p0842

## B. Vorlage für eine Instruktionsdatei

\<a id="rolle-und-arbeitsmodus"\>\</a\> ^p0843

\# Rolle und Arbeitsmodus ^p0844

\<a id="projektstruktur"\>\</a\> ^p0845

\# Projektstruktur ^p0846

\<a id="verbindliche-arbeitsregeln"\>\</a\> ^p0847

\# Verbindliche Arbeitsregeln ^p0848

\<a id="werkzeuge-und-befehle"\>\</a\> ^p0849

\# Werkzeuge und Befehle ^p0850

\<a id="regeln-fur-ruckfragen-und-eskalation"\>\</a\> ^p0851

\# Regeln für Rückfragen und Eskalation ^p0852

\<a id="abschlusskriterien"\>\</a\> ^p0853

\# Abschlusskriterien ^p0854

\<a id="verweise-auf-wissensdokumente"\>\</a\> ^p0855

\# Verweise auf Wissensdokumente ^p0856

## C. Vorlage für einen Working Context

\<a id="aufgabe-2"\>\</a\> ^p0857

\# Aufgabe ^p0858

\<a id="relevante-anforderungen"\>\</a\> ^p0859

\# Relevante Anforderungen ^p0860

\<a id="bereitgestellte-wissensdokumente"\>\</a\> ^p0861

\# Bereitgestellte Wissensdokumente ^p0862

\<a id="ausgangsdateien-und-daten"\>\</a\> ^p0863

\# Ausgangsdateien und Daten ^p0864

\<a id="verfugbare-werkzeuge"\>\</a\> ^p0865

\# Verfügbare Werkzeuge ^p0866

\<a id="aktueller-projektzustand"\>\</a\> ^p0867

\# Aktueller Projektzustand ^p0868

\<a id="prufkriterien-2"\>\</a\> ^p0869

\# Prüfkriterien ^p0870

\<a id="bekannte-unsicherheiten"\>\</a\> ^p0871

\# Bekannte Unsicherheiten ^p0872

\<a id="bewusst-nicht-geladene-ressourcen"\>\</a\> ^p0873

\# Bewusst nicht geladene Ressourcen ^p0874

## D. Vorlage für einen Verification Report

\<a id="verification-report"\>\</a\> ^p0875

\# Verification Report ^p0876

\<a id="identifizierter-zustand-2"\>\</a\> ^p0877

\#\# Identifizierter Zustand ^p0878

\<a id="ausgefuhrte-technische-prufungen"\>\</a\> ^p0879

\#\# Ausgeführte technische Prüfungen ^p0880

\<a id="ergebnisse"\>\</a\> ^p0881

\#\# Ergebnisse ^p0882

\<a id="abweichungen"\>\</a\> ^p0883

\#\# Abweichungen ^p0884

\<a id="nicht-geprufte-aspekte"\>\</a\> ^p0885

\#\# Nicht geprüfte Aspekte ^p0886

\<a id="fachliche-fragen"\>\</a\> ^p0887

\#\# Fachliche Fragen ^p0888

\<a id="empfohlene-nachste-schritte"\>\</a\> ^p0889

\#\# Empfohlene nächste Schritte ^p0890

## E. Vorlage für ein Acceptance Statement

\<a id="acceptance-statement-3"\>\</a\> ^p0891

\# Acceptance Statement ^p0892

\<a id="identifizierter-zustand-3"\>\</a\> ^p0893

\#\# Identifizierter Zustand ^p0894

\<a id="accepted-for-2"\>\</a\> ^p0895

\#\# Accepted for ^p0896

\<a id="technisch-verifiziert-2"\>\</a\> ^p0897

\#\# Technisch verifiziert ^p0898

\<a id="fachlich-gepruft-2"\>\</a\> ^p0899

\#\# Fachlich geprüft ^p0900

\<a id="nicht-nachgewiesen-2"\>\</a\> ^p0901

\#\# Nicht nachgewiesen ^p0902

\<a id="offene-fragen-3"\>\</a\> ^p0903

\#\# Offene Fragen ^p0904

\<a id="verantwortliche-entscheidung"\>\</a\> ^p0905

\#\# Verantwortliche Entscheidung ^p0906


[^1]: Die Beschreibung als Next Token Prediction ist eine funktionale Vereinfachung. Sie erklärt den unmittelbaren Generationsmechanismus, nicht die gesamte interne Verarbeitung eines Transformer-Modells. ^p0907

[^2]: Für die Unterscheidung zwischen zugrunde liegendem Modell, Assistant-Verhalten und trainiertem Charakter sind insbesondere die Veröffentlichungen von Anthropic zu Claude’s Character und zur Constitution relevant. Die ontologische Interpretation dieser Begriffe bleibt jedoch umstritten. ^p0908

[^3]: Produktbezeichnungen und konkrete Funktionen agentischer Arbeitsumgebungen verändern sich schnell. Die im Skriptum genannten Systeme dienen als Beispiele; Funktionsumfang und Terminologie sollten vor einer Publikation gegen die jeweils aktuelle Dokumentation geprüft werden. ^p0909

[^4]: Die nominelle Kontextgröße ist nicht mit einer garantierten effektiven Nutzung aller enthaltenen Information gleichzusetzen. Forschung zu Long-Context-Systemen untersucht unter anderem Positions-, Distraktor- und Retrievaleffekte. ^p0910

[^5]: MCP bezeichnet eine technische Spezifikation für die Verbindung von LLM-Anwendungen mit Werkzeugen und Datenquellen. Die konkrete Sicherheits- und Berechtigungsarchitektur hängt von der jeweiligen Implementation ab. ^p0911
