---
type: representation
source-type: document
source: "[[00_sources/promptotyping-document-templates.md]]"
converter: "none (Markdown originals concatenated); block IDs stamped deterministically per line"
channel: handover
metadata:
  title: "Promptotyping Document Templates"
  creator: "Digital Humanities Craft"
  date: "2026-08-22"
  format: md
  identifier: "https://github.com/DigitalHumanitiesCraft/Promptotyping/tree/6a5cfa46a767a8443908aeecbbf44831f3aea277/_content/promptotyping-document"
  license: "MIT (repository licence of DigitalHumanitiesCraft/Promptotyping)"
  confidential: false
created: 2026-08-22
updated: 2026-08-22
---

# Promptotyping Document Templates

The template set of the Promptotyping method, seventeen documents that define what each document type of a Promptotyping knowledge base holds, how it is structured, and what does not belong in it. Copied from `_content/promptotyping-document/` of DigitalHumanitiesCraft/Promptotyping at commit 6a5cfa46a767a8443908aeecbbf44831f3aea277. Each template is reproduced in full under a heading that names it; the templates are written in German and carry English technical terms. ^p0001

## Template `index.md`: Vorlage Index

Source file `_content/promptotyping-document/index.md`, template version 0.4. ^p0002

### Vorlage Index

Diese Vorlage strukturiert das Navigationsdokument einer Promptotyping-Wissensbasis. Das resultierende Dokument heißt `INDEX.md` und liegt im `knowledge/`-Ordner. Die Großschreibung ist die begründete Hub-Ausnahme des Naming Contract. Hier erschließen Menschen und Agents Dokumentregister, Lesereihenfolge, Ablagezonen sowie konstitutive Begriffe und Abkürzungen. ^p0003

#### Geltungsbereich

Die Vorlage trägt, sobald die Wissensbasis mehr als drei Dokumente enthält. Bei kleineren Repos ist ein Index überflüssig und kann in das Charter-Dokument (`project.md` oder `README.md`) integriert werden. Sie trägt nicht für projektübergreifende Übersichten oder MOCs im Vault; dafür gilt der Vault-Standard aus CLAUDE §3. ^p0004

Lebenszyklus: der Index entsteht, sobald das vierte Dokument die Schwelle reißt, und wird bei jeder neuen, umbenannten oder entfernten Datei nachgepflegt, parallel zur Wissensbasis, nicht erst zum Schluss. Die Konsistenz gegen den realen Ordnerinhalt ist seine einzige Update-Pflicht; ein Index, der sie verliert, ist schlechter als keiner, weil er falsche Sicherheit erzeugt. ^p0005

#### Funktion des Dokuments

Das Indexdokument adressiert einen menschlichen Reviewer, einen neu aufgesetzten Coding-Agenten und den Projekt-Verantwortlichen, der nach Wochen zurückkommt. Es beantwortet, welche Dokumente und Artefaktbereiche existieren, welche Routing Question jeder Pfad bedient, in welcher Reihenfolge gelesen wird und welche Begriffe oder Abkürzungen konstitutiv sind. Es ist zugleich Navigationsknoten und Begriffslexikon. ^p0006

#### Strukturprinzipien

Fünf Prinzipien tragen das Dokument. ^p0007

Erstens speichert der Index nicht, er zeigt. Jede Information, die im Index zusammengefasst wird, muss im verlinkten Geschwister-Dokument selbst stehen, sonst entstehen Wahrheitskonflikte zwischen Index und Quelle. Ausnahme: die Begriffsdefinitionen, die hier kanonisch leben, weil das Glossar zentralisiert ist. ^p0008

Zweitens liefert der Index Lesepfade, nicht nur eine Liste. Eine flache Aufzählung der Dokumente ist eine Datei-Übersicht, keine Lesehilfe. Lesepfade ordnen Dokumente nach Anliegen ("Onboarding", "Reproduktion", "Architektur-Review") und schicken den Leser durch die Wissensbasis in einer Reihenfolge, die der Aufgabe angemessen ist. ^p0009

Drittens trägt der Index die kanonischen Begriffe des Projekts. Begriffe sind dort definiert, wo sie gebraucht werden; der Index ist die einzige Stelle, an der die definierenden Begriffe vault-weit konsistent gepflegt sind. Geschwister-Dokumente verlinken auf einzelne Begriffe (`INDEX`), statt sie selbst zu definieren. Bei sehr vielen Begriffen (mehr als 15 bis 20) ist die Auslagerung in ein eigenes `glossary.md` zulässig; in der Regel reicht eine Sektion im Index. ^p0010

Viertens ist der Index gegen den realen Ordnerinhalt konsistent. Jede relevante Datei ist gelistet, kein Eintrag zeigt auf eine gelöschte oder geplante Datei. Nicht relevante Funktionen bleiben ohne ausgeschriebene Begründung weg. ^p0011

Fünftens erklärt der Index jede offizielle oder konstitutive Abkürzung, die in einem Dateinamen vorkommt. Die Dokumentenmatrix führt die echte Schreibweise des Pfads und bestätigt damit das primäre Routing-Signal. ^p0012

#### Frontmatter-Schema

Das Indexdokument folgt dem Frontmatter-Schema aus [Konvention Promptotyping Documents](#konvention-v0.1) (Pflichtkern: `title, project, method, status, created, updated`). Spezifisch für den Index: ^p0013

- `topics:` üblicherweise leer; der Index ist Meta-Dokument der Wissensbasis und trägt keine domänen-thematische Verortung. ^p0014
- `related:` listet alle Geschwister-Dokumente, die der Index anbindet. Dies ist die einzige Stelle in der Wissensbasis, an der `related:` vollständig sein muss. ^p0015
- `knowledge-sources:` entfällt, weil der Index keine inhaltliche Substanz trägt. ^p0016

#### Abschnitte im Detail

##### Lead

Funktion: in zwei bis drei Sätzen klar machen, was die Wissensbasis dokumentiert, für wen sie geschrieben ist, was bewusst nicht enthalten ist. Inhalt: Adressatenkreis, thematische Abdeckung, Verweis auf Operatives (Maintenance, Datenexport-Workflow), das nicht in der Wissensbasis selbst liegt. Keine Marketing-Sätze. ^p0017

##### Dokumentenmatrix

Funktion: tabellarische Übersicht aller dauerhaften Promptotyping Documents mit Pfad, Funktion, Routing Question und Aktualisierungsanlass. Die Matrix ist die maschinenlesbare Form der Wissensbasis-Struktur und wird von einem Agenten als erstes konsultiert. Die Reihenfolge folgt der Funktionslogik. ^p0018

##### Ablagezonen

Funktion: die Grenzen zwischen `knowledge/`, `research-artefacts/`, `source-material/`, `snapshots/`, `handoffs/` und `generated/` erklären. Inhalt: pro vorhandener Zone ein Satz zu Artefaktklasse und Lebenszyklus. Repo-spezifische oder domänentypische Ausgabepfade werden hier auf eine dieser Klassen abgebildet. ^p0019

##### Lesepfade

Funktion: Reihenfolgenempfehlungen für unterschiedliche Anliegen. Inhalt: zwei bis vier Pfade in Prosa oder als Liste, etwa "Onboarding eines neuen Mitarbeiters: project → data → specification → architecture", "Reproduktion eines Datenexports: data → architecture → journal", "Verstehen einer Designentscheidung: specification (Decisions-Sektion) → journal → design". Jeder Pfad ist begründet. ^p0020

##### Konvention

Funktion: Verweis auf die Konvention, nach der die Wissensbasis gepflegt wird. Inhalt: Wikilink auf [Konvention Promptotyping Documents](#konvention-v0.1) oder die Repo-Variante und ein Satz dazu, dass sie Naming Contract, Frontmatter-Schema und Routing-Heuristik erklärt. ^p0021

##### Begriffe

Funktion: kanonische Definitionen der projekt-konstitutiven Begriffe und der in Dateinamen verwendeten Abkürzungen, alphabetisch sortiert. Jede Abkürzung wird ausgeschrieben und in ihrer projektbezogenen Bedeutung eingeordnet. Geschwister-Dokumente verlinken bei Bedarf auf die Definition. Bei einem umfangreichen Begriffsbestand kann ein eigenes `glossary.md` übernehmen; die Dateinamen-Abkürzungen bleiben im Index sichtbar. ^p0022

#### Was nicht reingehört

- Inhaltsabschriften aus den Geschwistern. Der Index zeigt, er speichert nicht. Ausnahme: die Begriffsdefinitionen, die hier kanonisch leben. ^p0023
- Konkrete Zahlen aus der Anwendung (Coverage, Datensatzgrößen, Testcounts). Diese liegen in der Anwendung selbst und im `persons.json#meta` oder vergleichbar; siehe Vault-Regel zu volatilen Quantitäten in CLAUDE §6. ^p0024
- Sessionprotokolle und Verlaufserzählungen. Sachliche Übergänge werden knapp in `journal.md` nachgewiesen. ^p0025
- Eine "Was fehlt und warum"-Sektion. Bis zur Regeländerung vom 2026-06-29 gefordert, seitdem untersagt; nicht relevante Funktionen bleiben unkommentiert weg, Verweise auf anderswo liegendes Material stehen positiv am Bedarfsort. ^p0026
- Methodische Einführungen ins Promptotyping. Dafür ist [Promptotyping](#ueberblick) im Vault zuständig; der Index zeigt nur darauf. ^p0027
- Definitionen für Begriffe, die nur in einem einzigen Geschwister-Dokument vorkommen. Diese leben in der "Begriffe"-Sektion des betreffenden Dokuments, nicht im Index. ^p0028

#### Vorlage zum Befüllen

Der folgende Block ist als Template gedacht. Befüllungshinweise stehen als HTML-Kommentare und verschwinden im gerenderten Markdown. ^p0029

````markdown
---
title: Index
project:
  name: [Projektname]
  repository: [Repository-URL]
status: draft
language: [de | en]
version: [Repo-Schema-Version]
created: [YYYY-MM-DD]
updated: [YYYY-MM-DD]
authors: [Autor 1, Autor 2]
generated-with: [Harness (LLM), falls relevant]
method:
  name: Promptotyping
  url: https://lisa.gerda-henkel-stiftung.de/digitale_geschichte_pollin
template:
  name: Vorlage Index
  version: 0.4
  url: https://dhcraft.org/Promptotyping/promptotyping-document/index
  alias: https://dhcraft.org/Promptotyping/#promptotyping-document-index
related: [project, data, specification, architecture, design, handoff, journal]
---

<!-- Lead: zwei bis drei Sätze. Wer adressiert wird, was abgedeckt ist, was woanders liegt. -->

[Lead-Absatz]

#### Dokumente

| Pfad | Funktion | Routing Question | Aktualisierung |
|---|---|---|---|
| [[project]] | Charter | Was ist dieses Projekt? | bei Änderung von Identität oder Scope |
| [[data]] | Material | Was ist die Datengrundlage? | bei Datenexport oder Schemaänderung |
| [[specification]] | Specification | Was soll das System tun und warum? | bei Anforderungs- oder Entscheidungsänderung |
| [[architecture]] | Architecture | Wie ist es technisch realisiert? | bei Architekturänderung |
| [[design]] | Design | Wie sieht es aus und wie verhält es sich? | bei Änderung des Designsystems |
| [[handoff]] | Handoff | Welche Übergabepunkte sind offen? | bei Eingang oder Verarbeitung eines Handoff-Punkts |
| [[journal]] | Provenance | Welche Übergänge wurden integriert, verworfen oder korrigiert? | nach sachlich zusammengehörigen Übergängen |

<!-- Reihenfolge folgt Funktions-Logik, nicht alphabetisch. Nicht relevante Funktionen weglassen. -->

#### Ablagezonen

- `knowledge/` enthält dauerhaft gepflegte Promptotyping Documents einschließlich `handoff.md` als Process Inbox.
- `research-artefacts/` enthält wissenschaftliche Arbeitsprodukte.
- `source-material/` enthält übernommene Quellen und Transkripte.
- `snapshots/` enthält datierte Reports und Audits.
- `handoffs/` enthält außergewöhnliche, datierte Übergabe-Snapshots.
- `generated/` enthält reproduzierbar erzeugte Artefakte.

<!-- Nur vorhandene Zonen führen. Domänenspezifische Ausgabeordner ihrer Artefaktklasse zuordnen. -->

#### Lesepfade

<!-- Zwei bis vier Pfade. Jeder Pfad mit kurzer Begründung. -->

- Sessionstart: [[INDEX]] → [[handoff]] → [[project]] → [aufgabenrelevantes Dokument].
- Reproduktion eines Datenexports: [[data]] → [[architecture]] → [[verification]].
- Verstehen einer Designentscheidung: [[specification]] → [[journal]] → [[design]].

#### Konvention

Diese Wissensbasis folgt der Konvention für Promptotyping Documents. Sie regelt Naming Contract, Frontmatter-Schema, Routing-Heuristik und Strukturprinzipien. Siehe [Konvention im Vault] oder die Repo-Kopie unter `[Pfad falls vorhanden]`.

#### Begriffe

<!-- Alphabetisch sortiert. Offizielle oder konstitutive Abkürzungen in Dateinamen immer hier ausschreiben und definieren. Umfangreiche Fachbegriffe können in glossary.md ausgelagert werden. -->

##### [Begriff A]

[Definition. Was der Begriff im Projekt bezeichnet, abgegrenzt von verwandten Begriffen.]

Verwendet in [[document#Sektion]], [[anderes-document]].

##### [Begriff B]

[Definition.]

[Abgrenzung gegenüber verwandtem Begriff, falls Verwechslungsgefahr.]

Verwendet in [[document#Sektion]].
````

#### Anwendung als Prompt-Template

Strukturanker beim Setup eines neuen Repos. Der Agent erhält den Template-Block, kopiert ihn als `INDEX.md` in den `knowledge/`-Ordner und füllt die Tabelle aus, sobald die ersten Geschwister-Dokumente angelegt sind. Der Index entsteht parallel zur Wissensbasis und wird mit jeder neuen Datei nachgepflegt, nicht erst zum Schluss. ^p0030

Review-Folie für eine bestehende Wissensbasis. Ein vorhandener Index wird gegen die Vorlage gehalten, um zu prüfen, ob alle Geschwister gelistet sind und kein Eintrag auf eine gelöschte Datei zeigt, ob Lesepfade tatsächlich Pfade sind und nicht nur Listen, und ob die Konvention referenziert ist. ^p0031

#### Beispiel

HerData führt `INDEX.md` mit Lead, Dokumentenmatrix, Lesepfad-Sektionen und Konventionsverweis. Charakteristisch ist der Schlusssatz im Lead: "Konkrete Zahlen erscheinen ausschliesslich in der Anwendung selbst, in den Stat-Cards der Hauptansichten und im Meta-Block der `persons.json`." Das ist ein positiver Verweis auf den Ort der Wahrheit für volatile Zahlen und bleibt auch nach der Regeländerung vom 2026-06-29 zulässig, die ausgeschriebene "Was fehlt"-Sektionen abgeschafft hat. HerData führt die Begriffe-Sektion noch nicht; der Refactor sollte sie ergänzen, weil Termini wie „Erwähnt", „Erwähnung", „Brief", „Person" projekt-konstitutiv sind und in mehreren Dokumenten konsistent verwendet werden. ^p0032

Das wiederkehrende Fehlmuster zeigt das Inhaltsaudit vom Juli (2026-07-19 - Promptotyping-Wissensbasen Inhaltsaudit (Befund)): Indexe, die gegen den Ordnerinhalt driften, ein Index listet nur die Hälfte der real existierenden Dokumente, ein anderer lässt drei Dateien unregistriert, ein dritter verlinkt ein gelöschtes Datenmodell. Der Index ist das Dokument mit der höchsten Drift-Anfälligkeit der Wissensbasis, weil jede Änderung an einer Geschwister-Datei ihn mittelbar betrifft. ^p0033

sugw-Edition trägt das Glossar als eigenständiges Dokument `glossar.md` mit zwölf Begriffen (Erschließungsform, Event, Faksimile, Gesamtnennung, Individuelle Person, Menschen-Event, Quelle, Quellenkorpus, Rechtsgeschäft, Regest, Rolle, Volltext). Das ist die Auslagerungs-Variante, die die Konvention oberhalb von 15 bis 20 Begriffen empfiehlt; bei zwölf wäre eine Index-Sektion auch zulässig, sugw hat sich für die Auslagerung entschieden, weil das Glossar als UI-Tooltip-Quelle im Frontend dient und damit auch maschinen-konsumiert wird. ^p0034

#### Begriffe

- Wissensbasis: die Sammlung aller Markdown-Dokumente im `knowledge/`-Ordner eines Promptotyping-Repos. ^p0035
- Lesepfad: empfohlene Reihenfolge mehrerer Dokumente, die ein bestimmtes Anliegen am effizientesten beantwortet. ^p0036
- Dokumentenmatrix: tabellarische Übersicht der Promptotyping Documents mit Pfad, Funktion, Routing Question und Aktualisierungsanlass. ^p0037

#### Versionshistorie

- 0.4 (2026-08-21): `handoff.md` als verpflichtende Process Inbox in Dokumentenmatrix, Ablagezonen und Lesepfade aufgenommen. ^p0038
- 0.3 (2026-08-21): Naming Contract übernommen. Dokumentenmatrix um Pfad, Routing Question und Aktualisierungsanlass erweitert; Ablagezonen und Abkürzungsdefinitionen registriert. ^p0039
- 0.2 (2026-07-19): "Was fehlt und warum"-Sektion entfernt (Propagierung der Regeländerung Keine Selbstbeschreibung vom 2026-06-29), Ordnerinhalts-Konsistenz als viertes Strukturprinzip, englisches Funktionsvokabular, Block-Status auf `draft`, Lebenszyklus-Absatz. Migration: bestehende Indexe entfernen die Sektion beim nächsten Anfassen; begründete Lücken wandern ersatzlos, positive Verweise an den Bedarfsort. ^p0040
- 0.1 (2026-05-09): Erstfassung. ^p0041

#### Related

- [Vorlagen Promptotyping Documents](#vorlagen) ^p0042
- [Konvention Promptotyping Documents](#konvention-v0.1) ^p0043
- [Promptotyping](#ueberblick) ^p0044
- [Vorlage Projekt-Wissensdokument](#promptotyping-document-project) ^p0045
- [Vorlage Journal](#promptotyping-document-journal) ^p0046
- [Vorlage Handoff](#promptotyping-document-handoff) ^p0047

## Template `project.md`: Vorlage Projekt-Wissensdokument

Source file `_content/promptotyping-document/project.md`, template version 0.3. ^p0048


### Vorlage Projekt-Wissensdokument

Diese Vorlage strukturiert `project.md`, den kanonischen Charter-Träger eines Promptotyping-Projekts. Sie ist aus konkreten Projektüberblicken abstrahiert und überführt deren Strukturlogik in eine wiederverwendbare Form. Ein öffentliches `README.md` kann daraus ableiten und verweist auf die Wissensbasis; es ersetzt `knowledge/project.md` nicht. ^p0049

#### Geltungsbereich

Die Vorlage eignet sich für das zentrale Projekt-Wissensdokument `knowledge/project.md`. Sie trägt für Projekte, die mindestens drei Eigenschaften aufweisen: ^p0050

- Sie verarbeiten oder produzieren ein abgegrenztes Material, etwa Daten, Korpora, Dokumente. ^p0051
- Sie sind in einen institutionellen, methodologischen oder technischen Kontext eingebettet, der nicht selbsterklärend ist. ^p0052
- Sie haben definierte Funktionen, deren Beschreibung sich von der Beschreibung dessen unterscheidet, was bewusst nicht geleistet wird. ^p0053

Die Vorlage trägt nicht für Aufgaben-, Tagebuch- oder Diskussionsdokumente. Für solche Dokumenttypen sind andere Vorlagen sinnvoll. Sie ist auch nicht als Bibliotheks- oder Tool-README gedacht, bei denen Installation und API-Dokumentation im Vordergrund stehen. ^p0054

#### Strukturprinzipien

Drei Prinzipien tragen die Vorlage und sollten bei der Befüllung erhalten bleiben. ^p0055

Erstens trennt die Struktur konsequent zwischen dem, was das Projekt tut, dem, was es nicht tut, und dem, woher seine Substanz stammt. Diese Dreiteilung verhindert, dass Beschreibung, Selbstüberhöhung und Datenherkunft zu einer ununterscheidbaren Mischung werden. ^p0056

Zweitens werden Datenherkunft und Standards als strukturelle Hauptbestandteile geführt, nicht als Anhänge. Das spiegelt eine epistemische Haltung, in der Anschlussfähigkeit an externes Wissen Teil der Projektidentität ist. ^p0057

Drittens enthält die Struktur eine negative Selbstdefinition. Was bewusst nicht geleistet wird, wird genauso explizit benannt wie das, was geleistet wird. Diese Auslassung ist konstitutiv und sollte erhalten bleiben. ^p0058

#### Aufbau im Überblick

Die Vorlage besteht aus Frontmatter und neun Abschnitten, von denen einige obligatorisch und einige kontextabhängig sind. ^p0059

Obligatorisch: ^p0060

- Lead ^p0061
- Datengrundlage (oder „Materialgrundlage" für nicht-datenzentrierte Projekte) ^p0062
- Worum es geht ^p0063
- Funktionsumfang ^p0064
- Lizenz ^p0065

Stark empfohlen: ^p0066

- Standards ^p0067
- Begriffe ^p0068

Kontextabhängig: ^p0069

- Übergeordneter Kontext ^p0070
- Technische Umsetzung ^p0071
- Abgrenzungen ^p0072

#### Frontmatter-Schema

Das Frontmatter ist der maschinenlesbare Teil des Dokuments und folgt einem festen Schema. Es trägt fünf Felderfamilien. ^p0073

Identifikation. `title` als menschenlesbarer Titel; `project` als verschachteltes Feld mit `name` und `repository`. ^p0074

Status und Versionierung. `status` mit Werten wie `active`, `draft`, `archived`; `language` als Sprachcode; `version` als Versionsnummer; `created` und `updated` als Datumswerte im Format `YYYY-MM-DD`. ^p0075

Verantwortung. `authors` als Liste, die ausschließlich Menschen trägt, auch wenn ein LLM den Text erzeugt hat; `generated-with` als Werkzeugangabe im Format `Harness (LLM)`, etwa `Claude Code (Claude Opus 5)`, falls das Dokument LLM-gestützt entstanden ist. Siehe Sektion *Provenienz im Frontmatter* der [Konvention Promptotyping Documents](#konvention-v0.1). ^p0076

Methodologie. `method` als verschachteltes Feld mit `name` und `url`, das die methodologische Rahmung benennt. ^p0077

Wissensquellen. `knowledge-sources` als verschachteltes Mapping, das externe Wissensbestände als URI-Referenzen trägt. Die zweite Ebene gruppiert nach Typ (z. B. `institutions`, `standards`, `methods`, `vocabularies`), die dritte Ebene listet jeweils ein menschenlesbares Label als Schlüssel und eine dereferenzierbare URI als Wert. ^p0078

Das Feld `knowledge-sources` ist das Strukturmerkmal, das die Vorlage von generischen READMEs unterscheidet. Es macht das Dokument LOD-anschlussfähig: Jede aufgelistete Quelle ist durch eine URI eindeutig identifiziert und beim Auflösen direkt erreichbar. Bei Bedarf kann eine URI auch als Namespace zur semantischen Auszeichnung anderer Inhalte des Dokuments verwendet werden. ^p0079

Topics. Optional, als Wikilinks zu Vault-Konzepten. Beim Identitätsdokument typischerweise sparsam, etwa Scholar-Centered Design oder das überfachliche Forschungsfeld, soweit es das Projekt-Befüllen leitet. Wenn keine eindeutige Verortung trägt, weglassen. ^p0080

#### Abschnitte im Detail

Jeder Abschnitt erfüllt eine spezifische Funktion. Die folgenden Hinweise erklären, was hineingehört und was nicht. ^p0081

##### Lead

Funktion: schnelle Verständigung über die Identität des Projekts. Inhalt: ein bis zwei Sätze, die das Projekt definieren, die Datengrundlage knapp benennen und die zentralen Komponenten der Anwendung auflisten. Kein Marketing-Ton, keine Versprechen. Wer den Lead liest, soll wissen, worum es geht und wo das Material herkommt. ^p0082

##### Datengrundlage

Funktion: epistemische Verantwortung für die Datenbasis explizit machen. Inhalt: Herkunft der Daten, Auswahl- und Erfassungslogik, Charakter der Datenmenge (vollständig oder kuratiert), Abgrenzung der eigenen Leistung gegenüber der Datenproduktion. Verweis auf ein Detaildokument, falls vorhanden. Keine Personennamen, wenn die Datenproduktion institutionell zugeschrieben werden kann. ^p0083

##### Übergeordneter Kontext

Funktion: Verortung des Projekts im Verhältnis zu größeren Rahmen. Inhalt: institutioneller, akademischer oder methodologischer Rahmen, in den das Projekt eingebettet ist; Klärung, ob das Projekt offizieller Bestandteil dieses Rahmens ist oder eine eigenständige Anwendung darauf. Dieser Abschnitt entfällt, wenn das Projekt isoliert steht. ^p0084

##### Worum es geht

Funktion: Motivation und Werte sichtbar machen. Inhalt: Problemstellung, die das Projekt adressiert; Anliegen, die es verfolgt; programmatische Setzung von Prioritäten, falls einschlägig. Hier darf eine sachlich gefasste Wertaussage stehen, etwa „Das Projekt priorisiert X gegenüber Y". ^p0085

##### Standards

Funktion: technische und methodologische Anschlussfähigkeit dokumentieren. Inhalt: Liste der eingesetzten Standards, Vokabulare, Ontologien oder Frameworks, jeweils mit kurzer Funktionszuweisung. Anschließend ein Reflexionsabsatz, der die Wahl begründet und Verzerrungen oder Begrenzungen des Materials benennt. ^p0086

##### Technische Umsetzung

Funktion: Zurechenbarkeit der technischen Arbeit. Inhalt: wer für die Implementation verantwortlich ist, in welchem methodologischen Rahmen sie steht, wie sie sich gegenüber der inhaltlichen Datenproduktion abgrenzt. Knapper Absatz, keine Lebensläufe. ^p0087

##### Funktionsumfang

Funktion: Verständnis der Anwendung selbst. Inhalt: zentrale Designprinzipien und ihre konkrete Umsetzung, in zwei Absätzen. Erster Absatz: Einstieg, Navigation, Datensichten, Filter, Export. Zweiter Absatz: Designhaltung gegenüber Datenabdeckung und Unsicherheit, also wie mit fehlenden Daten und Provenance umgegangen wird. Keine erschöpfende Feature-Liste; UI-Details gehören in ein Detaildokument. ^p0088

##### Abgrenzungen

Funktion: Erwartungen kalibrieren und Begrenzungen als Designentscheidung markieren. Inhalt: Liste dessen, was bewusst nicht geleistet wird, gefolgt von einem Begründungssatz. Die Liste sollte fünf bis acht Punkte umfassen; weniger wirkt zu beiläufig, mehr wirkt verteidigend. ^p0089

##### Begriffe

Funktion: terminologische Kohärenz im Vault. Inhalt: Glossar projektzentraler Begriffe, jeder Eintrag in einem Satz definiert. Begriffe, die nur in einem einzigen Abschnitt vorkommen, gehören nicht ins Glossar; das Glossar ist für Begriffe, die in mehreren Vault-Dokumenten konsistent verwendet werden sollen. ^p0090

##### Lizenz

Funktion: rechtlicher Anker. Inhalt: knapper Verweis auf das eigentliche Lizenzdokument, mit Andeutung der wichtigsten Lizenzlogik (etwa Code-Lizenz und Datenlizenz, falls sie sich unterscheiden). Drei bis vier Sätze reichen; juristische Details liegen im Lizenzdokument. ^p0091

#### Vorlage zum Befüllen

Der folgende Block ist als Template gedacht. Befüllungshinweise stehen als HTML-Kommentare und verschwinden im gerenderten Markdown. ^p0092

````markdown
---
title: [Dokumenttitel]
project:
  name: [Projektname]
  repository: [Repository-URL]
status: complete
language: [de | en]
version: 0.1
created: [YYYY-MM-DD]
updated: [YYYY-MM-DD]
authors: [Autor 1, Autor 2]
generated-with: [Harness (LLM), falls relevant]
method:
  name: [Methodenname]
  url: [Methodendokumentation]
template:
  name: Vorlage Projekt-Wissensdokument
  version: 0.3
  url: https://dhcraft.org/Promptotyping/promptotyping-document/project
  alias: https://dhcraft.org/Promptotyping/#promptotyping-document-project
### topics: ["[[Wissensfeld]]"]  # optional, nur falls eine Verortung das Befüllen leitet
knowledge-sources:
  institutions:
    [Institution]: [URI]
  standards:
    [Standard]: [URI]
---

<!-- Lead: ein bis zwei Sätze. Was ist das Projekt, woher kommen die Daten, welche Komponenten gehören dazu. -->

[Lead-Absatz]

#### Datengrundlage

<!-- Herkunft der Daten, Auswahllogik, Charakter der Datenmenge, Abgrenzung der eigenen Leistung. Verweis auf Detaildokument. Keine Personennamen, wenn Institutionen tragen. -->

[...]

#### Übergeordneter Kontext

<!-- Optional. Nur wenn größerer Rahmen besteht. Klärung, ob offizieller Bestandteil oder eigenständig. -->

[...]

#### Worum es geht

<!-- Problemstellung, Anliegen, programmatische Prioritäten. -->

[...]

#### Standards

<!-- Liste der Standards mit Funktionszuweisung, danach Reflexionsabsatz. -->

Die technische Anschlussfähigkeit folgt etablierten Standards:

- [Funktion]: [Standard mit Kurzbeschreibung]
- [Funktion]: [Standard mit Kurzbeschreibung]

[Reflexionsabsatz]

#### Technische Umsetzung

<!-- Optional. Verantwortliche, methodologische Rahmung, Abgrenzung gegenüber inhaltlicher Arbeit. -->

[...]

#### Funktionsumfang

<!-- Erster Absatz: Designprinzipien und konkrete Funktionen. Zweiter Absatz: Umgang mit Datenabdeckung und Unsicherheit. -->

[Erster Absatz]

[Zweiter Absatz]

#### Abgrenzungen

<!-- Optional, aber empfohlen. Fünf bis acht Negationen, gefolgt von Begründungssatz. -->

Das Projekt leistet nicht:

- [Negativaussage]
- [Negativaussage]

[Begründungssatz]

#### Begriffe

<!-- Glossar projektzentraler Begriffe, vault-übergreifend konsistent. -->

- [Begriff]: [Definition].
- [Begriff]: [Definition].

#### Lizenz

<!-- Drei bis vier Sätze, Verweis auf [[license]] oder Äquivalent. -->

[...]
````

#### Anwendung als Prompt-Template

Die Vorlage kann in einem Promptotyping-Workflow auf zwei Weisen eingesetzt werden. ^p0093

Erstens als Strukturanker im Preparation-Schritt. Das LLM erhält den Template-Block als Kontext und wird gebeten, die Abschnitte auf Basis bereits vorhandener Materialien (Notizen, Skizzen, Vorgespräche) zu befüllen. Die HTML-Kommentare im Template fungieren dabei als implizite Befüllungsregeln. ^p0094

Zweitens als Review-Folie für ein bestehendes Dokument. Ein vorhandenes Projektdokument wird gegen die Vorlage gehalten, um zu prüfen, welche Abschnitte fehlen, welche überflüssig sind und welche stilistisch nicht zur Struktur passen. ^p0095

In beiden Fällen sollte das Befüllen iterativ erfolgen. Ein einmaliges Generieren des gesamten Dokuments aus einem Prompt führt erfahrungsgemäß zu oberflächlichen Befüllungen, weil die einzelnen Abschnitte unterschiedliche Quellen benötigen. Sinnvoller ist eine abschnittsweise Befüllung mit gezielten Rückfragen. ^p0096

#### Begriffe

- Wissensdokument: ein im Promptotyping-Sinn verdichtetes, vault-internes Markdown-Dokument, das Kontext für die Weiterarbeit mit einem LLM bereitstellt. ^p0097
- Frontmatter: der maschinenlesbare YAML-Block am Anfang eines Markdown-Dokuments, der strukturierte Metadaten trägt. ^p0098
- knowledge-sources: Frontmatter-Feld, das externe Wissensquellen als URI-Mapping aggregiert, gruppiert nach Quellentyp. ^p0099
- Negative Selbstdefinition: bewusste, explizite Aufzählung dessen, was ein Projekt nicht leistet, als Teil der Projektbeschreibung. ^p0100
- Geltungsbereich: Bedingungen, unter denen eine Vorlage trägt; Abgrenzung gegenüber Anwendungsfällen, für die andere Strukturen geeigneter sind. ^p0101

#### Lizenz

Die Vorlage steht unter der Lizenz des umgebenden Vaults oder Projekts und kann frei angepasst werden. Lizenzhinweise zu konkreten Projekten, die diese Vorlage einsetzen, gehören in das jeweilige Projektdokument. ^p0102

## Template `plan.md`: Vorlage Plan

Source file `_content/promptotyping-document/plan.md`, template version 0.3. ^p0103


### Vorlage Plan

Diese Vorlage strukturiert das vorwärts gerichtete Process-Dokument einer Promptotyping-Wissensbasis. Ein einzelner Träger heißt `plan.md`; getrennte Arbeitsströme werden als `<subject>-plan.md` spezialisiert. Das Dokument liegt im `knowledge/`-Ordner und ist das Gegenstück zum rückblickenden `journal.md`. Es ordnet die noch ausstehende Arbeit in Phasen und Milestones mit Entry- und Exit-Bedingungen, die gegen `specification.md` verankert sind. Der erste Absatz bestätigt die Funktion; ein eigenes `zweck:`- oder `function:`-Frontmatter-Feld entsteht nicht. ^p0104

#### Geltungsbereich

Die Vorlage trägt, sobald ein Projekt eine geordnete, mehrschrittige Sequenz noch ausstehender Arbeit hat, deren Reihenfolge und Abschlussbedingungen festgehalten werden sollen. Das ist der Regelfall für jedes aktiv entwickelte Repo, das über einen einzelnen Arbeitsgang hinausgeht. Triggerkriterium: es existieren mindestens zwei aufeinander aufbauende Arbeitsabschnitte mit prüfbaren Abschlussbedingungen, oder das Projekt steuert auf einen festen Termin (Meeting, Deployment, Abgabe) zu, gegen den die Arbeit getaktet wird. ^p0105

Sie trägt nicht für triviale Tool-Repos, die in einer Sitzung fertiggestellt werden, und nicht für reine Veröffentlichungs-Repos ohne weitere Entwicklung. Sie trägt nicht als Ersatz für ein Backlog ungeordneter Einzelaufgaben; ein Plan ordnet, ein Backlog sammelt. Die operative Tagesplanung einer einzelnen Sitzung gehört nicht hierher, sondern bleibt im Kopf des Bearbeiters oder im Action-Layer. ^p0106

Lebenszyklus: der Plan entsteht, sobald die Sequenz erkennbar ist, meist nach der ersten Fassung der `specification.md`, und wird bei jedem Milestone-Abschluss fortgeschrieben; sein Status ist `active`. Am Projektende wird er abgeschlossen (`archived`) oder seine übertragbaren Einsichten wandern in ein `learnings.md`; ein Plan, der nach Projektende unverändert stehen bleibt, wird zur falschen Quelle über den Projektstand. ^p0107

#### Funktion des Dokuments

Das Dokument beantwortet "was ist der nächste Schritt, in welcher Reihenfolge bauen die Schritte aufeinander auf, woran erkenne ich, dass ein Schritt abgeschlossen ist, und was muss vorher wahr sein, damit er beginnen kann". Es ist die vorwärts gerichtete Steuerungsschicht der Wissensbasis. Adressiert sind primär der Projekt-Verantwortliche, der die Arbeit taktet und gegen einen Termin priorisiert, und der Coding-Agent, der eine Session aufnimmt und wissen muss, welcher Milestone als Nächstes dran ist und unter welcher Bedingung er ihn als erledigt markieren darf. ^p0108

Die Abgrenzung gegen die Nachbardokumente ist scharf und definiert die Funktion. Gegen das `journal.md`: das Journal ist rückblickend und wird nie umgeschrieben, der Plan ist vorwärts gerichtet und wird fortgeschrieben. Was erledigt ist, wandert aus dem aktiven Teil des Plans in den Status-Tracker und verdichtet sich im Journal zu einem Eintrag; der Plan trägt nicht die Genese, sondern die Vorausschau. Gegen die `specification.md`: die Spezifikation sagt, was gebaut wird und warum (Anforderungen, Akzeptanzkriterien, Entscheidungen), der Plan sagt, wann und in welcher Reihenfolge. Die Exit-Bedingungen des Plans verweisen auf die Akzeptanzkriterien und Quality Gates der Spezifikation, dupliziert sie aber nicht. ^p0109

#### Strukturprinzipien

Drei Prinzipien tragen das Dokument. ^p0110

Erstens ist jeder Milestone gegen die Spezifikation verankert. Eine Phase oder ein Milestone trägt eine Entry-Bedingung (was muss wahr sein, um zu beginnen) und eine Exit-Bedingung (was muss wahr sein, um abzuschließen); die Exit-Bedingung verweist auf die Akzeptanzkriterien, Quality Gates oder Entscheidungen in der `specification.md`, statt sie neu zu formulieren. Ohne diese Verankerung wird der Plan zu einer Wunschliste ohne prüfbares Erledigt-Kriterium. Der Plan ist die Sequenz, die Spezifikation der Maßstab. ^p0111

Zweitens ist der Plan vorwärts gerichtet und wird fortgeschrieben, nicht angesammelt. Anders als das Journal, in dem alte Stände unverändert lesbar bleiben, wird der Plan beim Abschluss eines Milestones aktualisiert: der Status wandert in den Status-Tracker, neue Erkenntnisse über die nächste Phase fließen ein. Der Plan trägt immer den aktuellen Blick nach vorn, nicht die Historie. Die Historie liegt im Journal und in der Git-History; der Plan verweist darauf, kopiert sie nicht. ^p0112

Drittens dürfen im Status-Tracker volatile Zahlen stehen. Anders als Wissens-, Strategie- und Überblicksdokumente, die keine flüchtigen Quantitäten tragen, ist der Status-Tracker ein zeitpunktbezogener Snapshot des Arbeitsfortschritts und fällt damit unter die Snapshot-Ausnahme wie der Report. Commit-Hashes, abgeschlossene Anzahl von Artefakten, erreichte Messwerte gehören dort hin, weil der Status-Tracker genau diesen Stand festhält. Außerhalb des Status-Trackers, etwa in der Beschreibung künftiger Phasen, bleibt die Vorausschau frei von Zahlen, die beim nächsten Schritt veralten. ^p0113

#### Frontmatter-Schema

Das Dokument folgt dem reduzierten Pflichtkern aus der [Konvention Promptotyping Documents](#konvention-v0.1) (Stand 2026-06-13): `title`, `project` (Objekt mit `name` und `repository`), `method` (Objekt mit `name` und `url`), `status`, `created`, `updated`. Der Zweck lebt als erster Absatz unter der H1, in einem Satz, verständlich ohne Repo-Kontext. Die Vorlage stellt sicher, dass dieser erste Absatz den Zweck trägt. ^p0114

`status:` meint die Dokument-Maturity (`idea`, `draft`, `stub`, `complete`, `reviewed`, `archived`; seit 2026-07-19 auch `active` für fortlaufende Prozessdokumente und `snapshot` für Stichtagsdokumente), nicht den operativen Projektstatus. Für einen laufend fortgeschriebenen Plan ist `active` der passende Wert; der operative Fortschritt steht im Status-Tracker, nicht im Frontmatter. ^p0115

`template:` wird empfohlen, sobald diese Vorlage angewandt wurde, als Block mit `name`, `version`, `url` und optional `alias` (siehe Sektion *Vorlagen-Adressierbarkeit* der Konvention). Spezifisch für den Plan: ^p0116

- `related:` listet typischerweise `specification` (der Maßstab, gegen den die Milestones verankert sind), `journal` (das rückblickende Gegenstück) und `index`, gegebenenfalls `data` und `architecture`, wenn einzelne Milestones dort aufsetzen. ^p0117
- `topics:` entfällt typischerweise. Der Plan ist Process-Dokument und trägt keine domänen-thematische Verortung; die thematischen Topics leben in den Knowledge-Geschwistern. ^p0118
- `knowledge-sources:` entfällt; der Plan trägt keine externen Anschlüsse. ^p0119
- `updated:` wird bei jedem Abschluss eines Milestones aktualisiert; das Feld ist neben dem Journal eines der am häufigsten geänderten in der Wissensbasis. ^p0120
- Empfohlen zusätzlich `language`, `version` (repo-weit konsistent), `authors` und `generated-with`, falls das Dokument LLM-gestützt entstanden ist. `authors` trägt ausschließlich Menschen, `generated-with` das Format `Harness (LLM)`, etwa `Claude Code (Claude Opus 5)`. Siehe Sektion *Provenienz im Frontmatter* der Konvention. ^p0121

#### Abschnitte im Detail

##### Lead

Funktion: in einem Satz den Zweck tragen, dann in zwei bis drei Sätzen die Funktion abgrenzen. Inhalt: was der Plan steuert, ausdrückliche Positionierung als vorwärts gerichtetes Gegenstück zum Journal, Hinweis darauf, dass er fortgeschrieben und nicht angesammelt wird. Das FemPrompt-`plan.md` macht diese Selbstpositionierung mustergültig vor: "This is a process document; it is updated as phases close (mark done with date), and decisions made along the way go into specification as ADRs, not here." Der Lead positioniert den Plan gegen Spezifikation und Journal: er trägt weder das Was-und-Warum noch die Genese. ^p0122

##### Zielbild

Funktion: definieren, was "fertig" bedeutet, bevor die Sequenz beginnt. Inhalt: die Bedingungen, unter denen das Projekt oder die geplante Etappe als abgeschlossen gilt, in zwei bis vier Punkten. Das Zielbild ist der Fixpunkt, auf den alle Phasen zulaufen; ohne es wird die Phasenfolge richtungslos. Das FemPrompt-`plan.md` führt diese Sektion als "Zielbild (what done means)" mit vier prüfbaren Bedingungen. Bei kleineren Plänen kann das Zielbild in den Lead einrücken; bei mehrstufigen Projekten trägt es eine eigene Sektion. ^p0123

##### Phasen und Milestones

Funktion: die Arbeit in eine geordnete Sequenz prüfbarer Etappen gliedern. Inhalt: pro Phase ein Ziel in einem Satz, darunter ein oder mehrere Milestones; pro Milestone eine Entry-Bedingung, die zu leistende Arbeit, eine Exit-Bedingung. Eine Übersichtstabelle (Phase, Milestones, Quality Gate) am Kopf der Sektion gibt den Gesamtblick, wie im `roadmap.md` des DH Developer Skriptums. Reihenfolge stets älteste-Phase-zuerst, weil der Plan die Bauabfolge abbildet. ^p0124

Pro Milestone: ^p0125

- Entry-Bedingung. Was muss wahr sein, damit der Milestone beginnen kann; in der Regel der Abschluss eines vorherigen Milestones oder eine externe Voraussetzung. ^p0126
- Arbeit. Was zu tun ist, als Stichpunkte oder als thematisch geordnete Commit-Blöcke. Konkret genug, dass ein Agent ohne Rückfrage beginnen kann. ^p0127
- Exit-Bedingung. Woran erkennbar ist, dass der Milestone abgeschlossen ist; verankert gegen ein Akzeptanzkriterium, ein Quality Gate oder eine Entscheidung in der `specification.md`. Formuliert als "Done when", nicht als Absichtserklärung. ^p0128

Eine optionale eingerückte `Status (YYYY-MM-DD)`-Notiz pro Milestone hält fest, wo dieser Milestone gerade steht, wenn der zentrale Status-Tracker für die Detailtiefe nicht reicht. Das FemPrompt-`plan.md` nutzt diese eingerückten Status-Blöcke pro Phase intensiv. ^p0129

##### Status-Tracker

Funktion: den aktuellen Fortschritt aller Milestones zeitpunktbezogen festhalten. Inhalt: eine Tabelle (Milestone, Status, Notizen), aktualisiert beim Abschluss jedes Milestones. Hier sind volatile Zahlen ausdrücklich erlaubt: Commit-Hashes, abgeschlossene Anzahlen, erreichte Messwerte, weil der Tracker genau diesen Stand einfriert (Snapshot-Ausnahme, vgl. [Vorlage Report](#promptotyping-document-report)). Eine kleine Legende (`completed`, `in progress`, `pending`) hält die Statuswerte konsistent. Das `roadmap.md` führt diese Sektion als "Status Tracker" mit Commit-Refs in der Notizspalte; das `IMPLEMENTATION-PLAN.md` löst dasselbe über Phasentabellen mit `[x]`-Markern und einer Legende. ^p0130

##### Offene Entscheidungen und Abhängigkeiten

Funktion: festhalten, was noch zu entscheiden ist und was die Sequenz blockiert. Inhalt: offene Entscheidungspunkte mit dem Milestone, vor dem sie fallen müssen ("Decide before P3"), und harte Abhängigkeiten zwischen Milestones oder zu externen Ereignissen ("TP4 freeze precedes the B2 screening start"). Das FemPrompt-`plan.md` führt sowohl "Open items" als auch explizite "Hard ordering"-Hinweise. Diese Sektion verhindert, dass eine Phase begonnen wird, deren Vorbedingung noch ungeklärt ist. ^p0131

##### Abweichungen

Funktion: regeln, was passiert, wenn von der geplanten Reihenfolge abgewichen wird. Inhalt: unter welchen Bedingungen die Sequenz neu priorisiert werden darf, wohin die Abweichung dokumentiert wird (in der Regel ins `journal.md` mit Begründung), und welche Bedingungen unabhängig von der Reihenfolge gelten (typischerweise die Quality Gates). Das `roadmap.md` führt diese Sektion als "Deviations" und hält fest, dass die Wellen-Reihenfolge Empfehlung ist, die Gates aber unabhängig gelten. Bei kurzen, fest getakteten Plänen entfällt die Sektion. ^p0132

#### Was nicht reingehört

- Provenance und Sessionchronik. Wie sich das Projekt zum Stand gearbeitet hat, gehört ins `journal.md`; der Plan blickt nach vorn, nicht zurück. ^p0133
- Anforderungen und Entscheidungsbegründungen. Was gebaut wird und warum, steht in der `specification.md`; der Plan verweist auf ihre Akzeptanzkriterien als Exit-Bedingungen, formuliert sie nicht neu. Entscheidungen, die unterwegs fallen, wandern als ADR in die Spezifikation, nicht in den Plan. ^p0134
- Volatile Zahlen außerhalb des Status-Trackers. In der Beschreibung künftiger Phasen bleiben flüchtige Quantitäten draußen; sie veralten, bevor die Phase beginnt. Nur der Status-Tracker trägt den eingefrorenen Stand. ^p0135
- Zeitschätzungen. Die Sequenz ist fixiert, das Tempo offen; der Plan nennt keine Minuten-, Tages- oder Wochenschätzungen ("No time estimates", `roadmap.md`). ^p0136
- Ein ungeordnetes Backlog. Der Plan ordnet aufeinander aufbauende Schritte; lose gesammelte Einzelideen ohne Sequenz gehören in ein eigenes Backlog-Dokument. ^p0137

#### Vorlage zum Befüllen

Der folgende Block ist als Template gedacht. Der erste Absatz nach dem Frontmatter trägt den Zweck. ^p0138

````markdown
---
title: Plan
project:
  name: [Projektname]
  repository: [Repository-URL]
status: active
language: [de | en]
version: [Repo-Schema-Version]
created: [YYYY-MM-DD]
updated: [YYYY-MM-DD]
authors: [Autor 1, Autor 2]
generated-with: [Harness (LLM), falls relevant]
method:
  name: Promptotyping
  url: https://lisa.gerda-henkel-stiftung.de/digitale_geschichte_pollin
template:
  name: Vorlage Plan
  version: 0.3
  url: https://dhcraft.org/Promptotyping/promptotyping-document/plan
  alias: https://dhcraft.org/Promptotyping/#promptotyping-document-plan
related: [specification, journal, index]
---

<!-- Lead: erster Absatz trägt den Zweck in einem Satz, dann Abgrenzung. Vorwärts gerichtetes Gegenstück zum Journal, fortgeschrieben statt angesammelt, Entscheidungen wandern in die specification. -->

[Lead-Absatz mit dem Zweck im ersten Satz]

#### Zielbild

<!-- Was "fertig" bedeutet, in zwei bis vier prüfbaren Punkten. Der Fixpunkt, auf den alle Phasen zulaufen. -->

[...]

#### Phasen und Milestones

<!-- Übersichtstabelle, dann pro Phase ein Ziel und ein oder mehrere Milestones mit Entry, Arbeit, Exit. Reihenfolge: älteste Phase zuerst. -->

| Phase | Milestones | Quality Gate |
|---|---|---|
| Phase 0 — [Name] | M1 [Kurzname] | — |
| Phase 1 — [Name] | M2 [Kurzname] | Gate A |

##### Phase 0 — [Name]

**Ziel:** [Ein Satz.]

###### Milestone 1 — [Kurzname]

**Entry-Bedingung:** [Was vorher wahr sein muss.]

[Zu leistende Arbeit als Stichpunkte oder Commit-Blöcke.]

**Exit-Bedingung (M1):** [Done when ..., verankert gegen ein Akzeptanzkriterium oder Quality Gate in specification.md.]

<!-- Optional pro Milestone: -->
Status (YYYY-MM-DD): [Wo dieser Milestone gerade steht.]

#### Status-Tracker

<!-- Zeitpunktbezogener Snapshot. Hier sind volatile Zahlen erlaubt (Commit-Hashes, Anzahlen, Messwerte). Aktualisiert beim Abschluss jedes Milestones. -->

| Milestone | Status | Notizen |
|---|---|---|
| M1 — [Kurzname] | pending | |
| M2 — [Kurzname] | pending | |

Legende: completed, in progress, pending.

#### Offene Entscheidungen und Abhängigkeiten

<!-- Offene Entscheidungspunkte mit dem Milestone, vor dem sie fallen müssen. Harte Abhängigkeiten zwischen Milestones oder zu externen Ereignissen. -->

[...]

#### Abweichungen

<!-- Optional. Unter welchen Bedingungen neu priorisiert werden darf, wohin die Abweichung dokumentiert wird (journal.md), welche Bedingungen unabhängig von der Reihenfolge gelten (Quality Gates). -->

[...]
````

#### Anwendung als Prompt-Template

Strukturanker beim Aufsetzen eines Plans. Der Agent erhält den Template-Block und befüllt ihn aus der `specification.md` (die Akzeptanzkriterien und Quality Gates, gegen die er die Exit-Bedingungen verankert) und dem aktuellen Repo-Stand (für den initialen Status-Tracker). Beim Aufnehmen einer Session liest der Agent zuerst den Status-Tracker und die Sektion *Offene Entscheidungen und Abhängigkeiten*, um den nächsten zulässigen Milestone zu bestimmen, bevor er mit der Arbeit beginnt. Beim Abschluss eines Milestones aktualisiert er den Status-Tracker und das `updated:`-Feld und verdichtet die geleistete Arbeit zu einem `journal.md`-Eintrag; der Plan selbst bleibt vorwärts gerichtet. ^p0139

Review-Folie für einen bestehenden Plan. Ein vorhandenes `plan.md` oder `roadmap.md` wird gegen die Vorlage gehalten, um zu prüfen, ob jeder Milestone eine Entry- und eine Exit-Bedingung trägt, ob die Exit-Bedingungen gegen die Spezifikation verankert sind statt frei formuliert, ob volatile Zahlen ausschließlich im Status-Tracker stehen, und ob erledigte Arbeit aus dem aktiven Plan herausgewandert ist statt sich anzusammeln. ^p0140

#### Beispiel

Das `plan.md` von FemPrompt SozArb (`knowledge/plan.md`, [chpollin/FemPrompt_SozArb](https://github.com/chpollin/FemPrompt_SozArb)) nennt sich im Lead selbst "a process document" und das Gegenstück zum Journal: Entscheidungen, die unterwegs fallen, "go into specification as ADRs, not here". Es trägt ein "Zielbild (what done means)" mit vier prüfbaren Bedingungen, gliedert die Arbeit in Stages A bis C mit nummerierten Milestones (P0 bis P7), und jeder Milestone schließt mit einer "Done when"-Exit-Bedingung. Die eingerückten `Status (2026-06-09)`-Blöcke pro Milestone tragen volatile Stände wie konkrete Dateipfade und Zähldifferenzen (das 292-vs-291-Pairing-Problem), die im Fließtext der künftigen Phasen bewusst fehlen. ^p0141

Das `roadmap.md` des DH Developer Skriptums (`knowledge/roadmap.md`, [chpollin/Teaching](https://github.com/chpollin/Teaching)) wird im `INDEX.md` ausdrücklich als eigene Funktion "Plan" geführt, mit der Frage "What is the sequence of work, what milestones, what is next?". Es eröffnet mit einer Phasen-Milestone-Tabelle, verankert jeden Milestone gegen die "Quality Gates" der `specification.md`, hält "No time estimates" fest, schließt mit einer "Status Tracker"-Tabelle (Commit-Refs wie `28dd38e` in der Notizspalte) und einer "Deviations"-Sektion, die die Wellen-Reihenfolge als Empfehlung kennzeichnet, die Gates aber als unabhängig geltend. ^p0142

Das `IMPLEMENTATION-PLAN.md` von co-ocr-htr (`knowledge/IMPLEMENTATION-PLAN.md`, [ResearchTools/co-ocr-htr](https://github.com/chpollin/co-ocr-htr)) zeigt die kompakte Variante: dichte Phasentabellen (Feature, Status, Location) mit `[x]`/`[~]`/`[ ]`-Markern und einer expliziten Legende am Ende. Es belegt, dass der Status-Tracker und die Phasenstruktur in einem einzigen tabellengetragenen Dokument zusammenfallen können, wenn das Projekt klein genug ist; Entry- und Exit-Bedingungen sind dort in die Phasenziele eingerückt statt pro Milestone ausformuliert. ^p0143

Das Fehlmuster aus dem Inhaltsaudit vom Juli 2026 ist der Plan als Sammelsurium: ein `plan.md`, das Charter, Spezifikation, Status und Session-Protokoll in einem Dokument mischt, verliert die Steuerungsfunktion, weil kein Leser mehr erkennt, welcher Teil vorwärts gerichtet ist. ^p0144

#### Begriffe

- Phase: thematisch abgegrenzter Arbeitsabschnitt mit einem Ziel, der einen oder mehrere Milestones bündelt. ^p0145
- Milestone: prüfbare Etappe innerhalb einer Phase, mit Entry-Bedingung, zu leistender Arbeit und Exit-Bedingung. ^p0146
- Entry-Bedingung: was wahr sein muss, damit ein Milestone beginnen darf; in der Regel der Abschluss eines vorherigen Milestones oder eine externe Voraussetzung. ^p0147
- Exit-Bedingung: woran erkennbar ist, dass ein Milestone abgeschlossen ist; verankert gegen ein Akzeptanzkriterium oder Quality Gate der `specification.md`. ^p0148
- Status-Tracker: zeitpunktbezogener Snapshot des Milestone-Fortschritts; die einzige Sektion des Plans, in der volatile Zahlen zulässig sind. ^p0149
- Quality Gate: in der Spezifikation definierter Prüfpunkt aus mechanischen und menschlichen Checks, an den eine Exit-Bedingung gebunden sein kann. ^p0150

#### Versionshistorie

- 0.3 (2026-08-21): Naming Contract übernommen. Einzelträger heißt `plan.md`, Spezialisierungen folgen `<subject>-plan.md`. ^p0151
- 0.2 (2026-07-19): Freigabe (status complete), englisches Funktionsvokabular, Block-Status auf `active`, Lebenszyklus-Absatz, Fehlmuster im Beispiel. Keine Migrationspflicht für bestehende Repos. ^p0152
- 0.1 (2026-06-13): Erstfassung. ^p0153

#### Related

- [Konvention Promptotyping Documents](#konvention-v0.1) ^p0154
- [Vorlage Journal](#promptotyping-document-journal) ^p0155
- [Vorlage Specification](#promptotyping-document-specification) ^p0156
- [Vorlage Report](#promptotyping-document-report) ^p0157
- [Vorlage Index](#promptotyping-document-index) ^p0158
- [Vorlage Projekt-Wissensdokument](#promptotyping-document-project) ^p0159

## Template `data.md`: Vorlage Datengrundlage

Source file `_content/promptotyping-document/data.md`, template version 0.3. ^p0160


### Vorlage Datengrundlage

Diese Vorlage strukturiert das Material-Dokument einer Promptotyping-Wissensbasis. Ein einzelner Träger heißt `data.md`; getrennte Datengrundlagen werden als `<subject>-data.md` oder nach ihrer präziseren Funktion, etwa `data-schema.md`, spezialisiert. Das Dokument liegt im `knowledge/`-Ordner und trägt die epistemische Verantwortung für das verarbeitete oder produzierte Material. ^p0161

Diese Fassung (v0.1, 2026-05-09) ist auf Basis einer Querschau durch 19 reale `data.md` aus den aktiven Promptotyping-Repos entwickelt. Sie unterscheidet vier Pflichtsektionen von sechs optionalen Sektionen mit Triggerkriterium. ^p0162

#### Geltungsbereich

Die Vorlage trägt, sobald das Projekt Daten verarbeitet oder produziert. Bei reinen Tool-, Bibliotheks- oder Methoden-Repos entfällt sie; das Identitätsdokument trägt die Materialgrundlage dann selbst in einer kompakten Sektion. Die Vorlage trägt nicht für API-Dokumentationen, Datenbankschema-Beschreibungen ohne Inhaltsbezug oder Datenbeispiele ohne Provenienz. ^p0163

Sie trägt sowohl für Repos, die eigene Daten produzieren (HerData, klawiter-rescue, notker-edition, sugw-Edition), als auch für Repos, die fremde Datensätze nur als Input nehmen (wiiw-figaro-nam, vetmed-berichtswesen, objekt-bestimmung-workshop). Die optionalen Sektionen unterscheiden die Fälle. ^p0164

#### Funktion des Dokuments

Das Dokument beantwortet "was sind die Daten, woher kommen sie, wie sind sie modelliert, wo hört das Material auf zu tragen". Adressiert sind drei Lesergruppen: ein Reviewer, der die Datenqualität beurteilen will; ein Coding-Agent, der die Daten verarbeiten oder transformieren soll; ein Domänenexperte, der die Auswahllogik nachvollziehen will. Das Dokument ist epistemisch verantwortlich; es macht transparent, was die Daten leisten und was nicht. ^p0165

#### Strukturprinzipien

Drei Prinzipien tragen das Dokument. ^p0166

Erstens trennt es Datenproduktion von Datenverarbeitung. Wer die Daten erfasst hat (Institution, Editionsteam, externe Quelle) trägt eine andere Art von Autorschaft als wer sie hier verarbeitet; diese Trennung muss explizit benannt werden. Die eigene Leistung gegenüber der Datenproduktion abzugrenzen ist eine Grundregel, kein Höflichkeitsgestus. ^p0167

Zweitens praktiziert das Dokument negative Selbstdefinition. Was bewusst nicht geleistet wird oder nicht abgedeckt ist, wird genauso explizit benannt wie das, was geleistet wird. Diese Auslassung ist konstitutiv und trägt die Sektion `Grenzen`. ^p0168

Drittens steht im Dokument keine konkrete Zahl, die sich beim nächsten Datenexport ändert. Coverage-Werte, Datensatzgrößen und Verteilungs-Statistiken liegen in der Anwendung selbst (im `persons.json#meta` oder vergleichbar) und in den Stat-Cards der Hauptansichten. Das Dokument verweist auf diese Quellen, dupliziert sie nicht. ^p0169

#### Frontmatter-Schema

Das Dokument folgt dem Frontmatter-Schema aus der [Konvention Promptotyping Documents](#konvention-v0.1) (Pflichtkern: `title, project, method, status, created, updated`). Spezifisch für die Datengrundlage: ^p0170

- `topics:` typisch sind Verweise auf Wissensfelder wie Data Modelling, Normdata, Controlled Vocabularies. Bei Editions-Repos zusätzlich TEI, Prosopography o.ä. Sie verorten den Agenten in den Wissensfeldern, die für Materialdokumentation tragen. ^p0171
- `knowledge-sources:` ist hier zentral und sollte gepflegt sein. Mindestens `institutions:` (datenproduzierende Institutionen mit URI) und `standards:` (eingesetzte Datenstandards, Vokabulare, Ontologien mit URI). Optional `vocabularies:` für kontrollierte Vokabulare und `datasets:` für referenzierte externe Datensätze. ^p0172
- `related:` typischerweise `project`, `architecture`, `specification`; die drei Dokumente, die auf die Datengrundlage aufbauen. ^p0173
- `output-of:` trägt den Befehl, der das Dokument erzeugt, und wird gesetzt, sobald ein Skript die Korpusbeschreibung aus den Quelldaten rendert. Das ist bei großen oder heterogenen Beständen der Regelfall. Steht das Feld, wird das Dokument nicht von Hand bearbeitet und eine Korrektur geht an das Skript. Siehe Sektion *Provenienz im Frontmatter* der Konvention. ^p0174
- `updated:` wird bei jedem neuen Datenexport aktualisiert. ^p0175

#### Sektionsstruktur

Vier Pflichtsektionen, sechs optionale Sektionen mit Triggerkriterium. Optionale Sektionen, die nicht zutreffen, werden weggelassen, nicht leer geführt. ^p0176

```
PFLICHT:    Gegenstand → Quellen → Modell → Grenzen
OPTIONAL:   Normdaten und Anschlüsse
            Verzerrungen
            Provenance pro Wert
            Verhältnis zur externen Datenquelle
            Workflow
            Beispiele
```

#### Pflichtsektionen

##### Gegenstand

Funktion: was ist das Material überhaupt. Definition: knappe inhaltliche Charakterisierung dessen, was die Daten beschreiben, der historisch-wissenschaftliche Gegenstand, nicht das Format. Eine bis drei Sätze. Beantwortet die Frage, worüber geredet wird, bevor über Strukturen geredet wird. Trägt nicht: Datenformat, Pipeline, Bewertung. ^p0177

##### Quellen

Funktion: woher kommt das Material. Definition: pro Quelle Herkunft, Erfassungslogik, Lizenz, Provenienz, Erfassungszeitraum. Bei mehreren Quellen wird die Beziehung zwischen ihnen erklärt, etwa "Quelle A liefert die Personenliste, Quelle B liefert die Briefmetadaten, Verknüpfung über GND-Identifier". Personenbezogene Erfassung wird in Institutionen-Sprache gesetzt, nicht mit Personennamen; wenn ein Bearbeiterinnen-Team namentlich anerkannt werden soll, geschieht das im eigenen Dokument oder in einer Anerkennungs-Sektion am Ende, nicht im Quellen-Block. Trägt nicht: eigene Bearbeitungslogik. ^p0178

##### Modell

Funktion: wie ist das Material strukturiert. Definition: die Hauptentitäten und ihre Relationen, die Schemata oder Annotationsebenen, kontrollierte Vokabulare. Bei eigener Datenproduktion das semantische Modell der erzeugten Daten (JSON-Schema, RDF-Vokabular). Bei standardgebundener Auszeichnung die Annotationsebenen und Schema-Constraints (TEI-Elemente, RelaxNG-Constraints, ODD-Mismatches mit dem Korpus). Bei externen Datenlieferungen die gelieferte Struktur (Spalten, Typen, Hive-Partitionierung). Verweis auf Schema-Dateien im Repo als Source of Truth; das Dokument paraphrasiert das Schema, ersetzt es nicht. Trägt nicht: Pipeline-Schritte, UI-Logik, Implementations-Details. ^p0179

##### Grenzen

Funktion: was leistet das Material nicht. Definition: was nicht abgedeckt ist und warum. Lücken, Auslassungen, strukturelle Beschränkungen, geschlossene Bestände, nicht digitalisierte Teile, bewusste Selektion. Qualitativ formuliert, nicht in Prozentzahlen; konkrete Coverage-Werte gehören in den `meta`-Block der Datendatei und in die Stat-Cards der Anwendung. Beantwortet, wo das Material aufhört zu tragen. Trägt nicht: Verzerrungen (das ist die optionale Sektion `Verzerrungen`); konkrete Coverage-Zahlen. ^p0180

#### Optionale Sektionen

##### Normdaten und Anschlüsse

Trigger: Material verwendet externe Identifier (GND, Wikidata, GeoNames, AGRELON, VIAF, ORCID, IIIF, DOI). Funktion: externe Anschlüsse offenlegen. Definition: welche Identifier-Systeme das Material an externes Wissen anschließen, wie sie eingebunden sind, welche Coverage qualitativ erreicht wird ("vollständig", "lückenhaft", "selektiv"). Verlinkung auf die offiziellen Dokumentationen der Normdaten-Systeme. Bei reinen Editionsdaten ohne Normdaten-Anbindung entfällt die Sektion. ^p0181

##### Verzerrungen

Trigger: Material trägt erkennbare systematische Schiefen, die für die Interpretation relevant sind. Funktion: systematische Schiefen explizit machen. Definition: zwei bis fünf benannte Verzerrungen mit Begründung, etwa "Map Bias: Geodaten konzentrieren sich auf Mitteleuropa, weil die Quelle institutionell dort verankert ist", "Genderverzerrung: Frauen unterrepräsentiert, weil die Quellgrundlage Goethe-zentriert ist", "Sprachbias: deutschsprachige Sekundärliteratur überproportional präsent, weil Sammelschwerpunkt der Bibliothek". Eine Verzerrung ohne Begründung ist eine Vermutung; eine begründete ist eine Designentscheidung. Bei standardisierten Datensätzen ohne erkennbare Schiefen oder bei rein technischen Datenbeständen entfällt die Sektion. ^p0182

Abgrenzung zu `Grenzen`: `Grenzen` benennt strukturelle Auslassungen ("Zeitraum 1418 bis 1447 ist nicht ausgewertet"), `Verzerrungen` benennt asymmetrische Abdeckungen innerhalb des erfassten Materials ("innerhalb der erfassten Personen sind Frauen mit beruflichen Netzwerken zu Männern überrepräsentiert"). ^p0183

##### Provenance pro Wert

Trigger: Werte entstehen mehrstufig, durch Regex, LLM, manuelle Annotation, KI-Korrektur oder Hybrid-Verfahren. Funktion: die Extraktionsspur pro Wert dokumentieren, sodass ein Critical-Expert-Reviewer entscheiden kann, was er prüft. Definition: pro Feldgruppe die Extraktionsmethode (regex / llm / manuell / missing) und qualitative Coverage-Aussage, ohne konkrete Prozentzahlen. Verweis auf maschinell generierte Quality-Report-Datei oder Debug-JSON im Repo als Source of Truth. Bei Daten aus einer einzigen verlässlichen Quelle (Excel-Lieferung, einzelner Export) entfällt die Sektion. ^p0184

##### Verhältnis zur externen Datenquelle

Trigger: Daten werden geliefert, nicht erzeugt. Das Repo nimmt fremde Daten als Input und verändert sie nicht zurück. Funktion: das Verhältnis zur Quelle markieren. Definition: in welcher Form geliefert (Excel, Parquet, RDS, REST-API), was bewusst nicht getan wird (keine Modifikation, kein Edit-Pfad, kein Re-Upload, kein localStorage-Edit), wo die Source of Truth bleibt (Sammlungsmanagementsystem, externe API, Lieferdatei). Bei Repos mit eigener Datenproduktion entfällt die Sektion. ^p0185

##### Workflow

Trigger: Pipeline transformiert die Quelle zu einer Anwendungsdatei. Funktion: den Weg von der Quelle zur Anwendungsdatei dokumentieren. Definition: knapp die Pipeline-Stufen (Import, Bereinigung, Verknüpfung, Export) mit Verweis auf die Skripte im Repo. Nicht die Implementation des Workflows beschreiben, das gehört in `architecture.md`. Bei reinen Lese-Repos ohne Transformation entfällt die Sektion. ^p0186

##### Beispiele

Trigger: das Datenmodell ist ohne konkretes Beispiel schwer greifbar. Funktion: das Datenmodell konkret machen. Definition: ein bis drei kompakte Records (JSON, XML, RDF, je nach Format) im Codeblock, die das Modell exemplarisch zeigen. Die Beispiele sind aus den realen Daten gewählt, nicht erfunden. Bei sehr einfachen Datenmodellen, die im `Modell`-Abschnitt selbsterklärend dargestellt sind, entfällt die Sektion. ^p0187

#### Was nicht in das Dokument gehört

- Konkrete Coverage-Zahlen, Datensatzgrößen, Verteilungs-Statistiken. Diese liegen in der Anwendung und im Meta-Block der Datendatei, nicht im Dokument. ^p0188
- Pipeline-Implementation. Wie der Workflow gebaut ist, gehört in `architecture.md`. ^p0189
- UI-Logik. Wie die Daten angezeigt werden, gehört in `specification.md` oder `design.md`. ^p0190
- Forschungsergebnisse. Was die Daten inhaltlich zeigen, ist Sache der Veröffentlichungen, nicht der Datengrundlage. ^p0191

#### Vorlage zum Befüllen

Der folgende Block ist als Template gedacht. Optionale Sektionen, die nicht zutreffen, werden vor dem Commit gelöscht, nicht leer gelassen. ^p0192

````markdown
---
title: Daten
project:
  name: [Projektname]
  repository: [Repository-URL]
status: complete
language: [de | en]
version: [Repo-Schema-Version]
created: [YYYY-MM-DD]
updated: [YYYY-MM-DD]
authors: [Autor 1, Autor 2]
generated-with: [Harness (LLM), falls relevant]
method:
  name: Promptotyping
  url: https://lisa.gerda-henkel-stiftung.de/digitale_geschichte_pollin
template:
  name: Vorlage Datengrundlage
  version: 0.3
  url: https://dhcraft.org/Promptotyping/promptotyping-document/data
  alias: https://dhcraft.org/Promptotyping/#promptotyping-document-data
topics: ["[[Data Modelling]]", "[[Normdata]]", "[[Controlled Vocabularies]]"]
knowledge-sources:
  institutions:
    [Institution]: [URI]
  standards:
    [Standard]: [URI]
related: [project, architecture, specification]
---

#### Gegenstand

<!-- Eine bis drei Sätze. Was beschreibt das Material inhaltlich. Historisch-wissenschaftlicher Gegenstand, nicht Format. Keine Zahlen. -->

[...]

#### Quellen

<!-- Pro Quelle: Herkunft, Erfassungslogik, Lizenz, Provenienz, Erfassungszeitraum. Bei mehreren Quellen die Beziehung zwischen ihnen. Personen in Institutionen-Sprache. -->

[...]

#### Modell

<!-- Hauptentitäten, Relationen, Annotationsebenen oder gelieferte Struktur. Verweis auf Schema-Datei als Source of Truth, paraphrasieren statt ersetzen. -->

[...]

#### Grenzen

<!-- Was nicht abgedeckt ist und warum. Strukturelle Auslassungen, geschlossene Bestände, bewusste Selektion. Qualitativ, keine Prozentzahlen. -->

[...]

<!-- ============================================================ -->
<!-- OPTIONALE SEKTIONEN: vor dem Commit nicht zutreffende löschen -->
<!-- ============================================================ -->

#### Normdaten und Anschlüsse

<!-- Trigger: externe Identifier verwendet (GND, Wikidata, GeoNames, AGRELON, VIAF, ORCID, IIIF). -->

[...]

#### Verzerrungen

<!-- Trigger: Material trägt systematische Schiefen, die interpretationsrelevant sind. Zwei bis fünf, je mit Begründung. -->

- [Verzerrung]: [Begründung].

#### Provenance pro Wert

<!-- Trigger: Werte entstehen mehrstufig (regex, LLM, manuell, KI-korrigiert). Pro Feldgruppe die Extraktionsmethode. Verweis auf Quality-Report. -->

[...]

#### Verhältnis zur externen Datenquelle

<!-- Trigger: Daten werden geliefert, nicht erzeugt. In welcher Form geliefert, was nicht getan wird, wo die Source of Truth bleibt. -->

[...]

#### Workflow

<!-- Trigger: Pipeline transformiert Quelle zu Anwendungsdatei. Knapp die Stufen, Verweis auf Skripte. Implementation gehört in architecture.md. -->

[...]

#### Beispiele

<!-- Trigger: Datenmodell ist ohne konkretes Beispiel schwer greifbar. Ein bis drei reale Records im Codeblock. -->

```json
[...] ^p0193
```
````

#### Anwendung als Prompt-Template

Strukturanker beim Aufsetzen der Datengrundlage. Der Agent erhält den Template-Block und befüllt ihn iterativ aus den Quelldokumenten (Lizenztexte, Schema-Dateien, README der Datenherkunft). Vor dem ersten Befüllen entscheidet der Agent pro optionaler Sektion anhand des Triggers, ob sie trägt; nicht zutreffende werden gelöscht. Die Sektion `Verzerrungen`, falls sie trägt, verlangt Domänenexpertise und sollte vom Critical Expert verifiziert werden (siehe Glossar-Eintrag Critical-Expert-in-the-Loop). ^p0194

Review-Folie für eine bestehende Datengrundlage. Ein vorhandenes `data.md` wird gegen die Vorlage gehalten, um zu prüfen, ob die vier Pflichtsektionen tragen, ob `knowledge-sources:` im Frontmatter gepflegt ist, ob keine konkreten Zahlen aus der Anwendung dupliziert werden, ob optionale Sektionen ihren Trigger erfüllen und Sektionen ohne Trigger nicht aus Reflex mitgeschleppt werden. ^p0195

#### Genrebeispiele aus der Praxis

HerData (eigene Datenproduktion mit Normdaten-Anbindung). Trägt: Gegenstand, Quellen, Modell, Grenzen, Normdaten und Anschlüsse, Verzerrungen, Provenance pro Wert, Workflow, Beispiele. Charakteristisch ist die explizite Map-Bias-Sektion, die in der Anwendung selbst (Onboarding-Schritt MapBias) sichtbar gemacht wird. `knowledge-sources` führt Goethe- und Schiller-Archiv und PROPYLÄEN als Institutionen, CMIF, GND, GeoNames und AGRELON als Standards. ^p0196

notker-edition / sugw-Edition (standardgebundene Editionsdaten). Trägt: Gegenstand, Quellen, Modell (mit Annotationsebenen und Schema-Constraints im Modell-Abschnitt), Grenzen, Normdaten und Anschlüsse (IIIF, GND), Beispiele. `Verhältnis zur externen Datenquelle` und `Provenance pro Wert` entfallen, es gibt eine eigene editorische Datenproduktion. ^p0197

vetmed-berichtswesen / objekt-bestimmung-workshop (externe Datenquelle als Input). Trägt: Gegenstand, Quellen, Modell (gelieferte Struktur), Grenzen, Verhältnis zur externen Datenquelle, Workflow, Beispiele. `Normdaten und Anschlüsse` und `Verzerrungen` entfallen typischerweise. ^p0198

klawiter-rescue (mehrstufige Daten-Rekonstruktion). Trägt: alle vier Pflichtsektionen, dazu Normdaten und Anschlüsse, Verzerrungen, Provenance pro Wert, Workflow, Beispiele. Das volle Programm: `Provenance pro Wert` ist hier zentral, weil Werte aus Regex, LLM und Wikidata-Reconciliation kombiniert sind. ^p0199

#### Begriffe

- Material: das verarbeitete oder produzierte Substrat eines Promptotyping-Projekts. Daten, Korpus, Dokumentensammlung, Bildbestand. ^p0200
- Grenzen: was das Material strukturell nicht abdeckt, also geschlossene Bestände, nicht digitalisierte Teile, bewusste Selektion. ^p0201
- Verzerrung: systematische Schiefe innerhalb des erfassten Materials, die durch die Erfassungs- oder Auswahllogik der Quelle bedingt ist. ^p0202
- Provenienz: Herkunfts- und Bearbeitungsgeschichte einer Datenquelle, einschließlich der Institutionen und Personen, die sie produziert haben. ^p0203
- Provenance pro Wert: feinkörnige Extraktionsspur pro Datenfeld, die festhält, durch welche Methode (regex, LLM, manuell, KI-korrigiert) ein Wert in das Datenset gelangt ist. ^p0204

## Template `domain-knowledge.md`: Vorlage Domänenwissen

Source file `_content/promptotyping-document/domain-knowledge.md`, template version 0.3. ^p0205


### Vorlage Domänenwissen

Diese Vorlage strukturiert das Domain-Knowledge-Dokument einer Promptotyping-Wissensbasis. Der Dateiname folgt `<subject>-<function>.md`, etwa `editorial-guidelines.md`, `tei-mapping.md`, `domain-ontology.md`, `research-methodology.md` oder `research-framework.md`. Das Dokument liegt im `knowledge/`-Ordner und trägt fachmethodische Regeln sowie deren Begründung. Der erste Absatz bestätigt die über den Dateinamen geroutete Funktion; ein eigenes `zweck:`- oder `function:`-Feld entsteht nicht. ^p0206

#### Geltungsbereich

Die Funktion trägt, sobald ein Projekt eine fachmethodische Vorgabe macht, die nicht aus dem Material und nicht aus der Softwareanforderung ableitbar ist, sondern eine eigene wissenschaftliche Setzung darstellt. Triggerkriterium: Es existiert eine Regel, ein Mapping, eine Berechnungslogik, ein Vokabular oder eine theoretische Rahmung, die ein Fachexperte verantwortet und die man kennen muss, um das Output korrekt zu interpretieren oder zu erweitern. Das ist der Fall bei Editionsrichtlinien, TEI-Mappings, Kodiermanualen, Ontologie-Definitionen, Berechnungslogiken (etwa CER-Methodik, Score-Formeln, Klassifikationsregeln) und bei expliziten Forschungsrahmen, Methodik-Kapiteln oder forschungsgestützten Designbegründungen. ^p0207

Die Funktion trägt nicht für triviale Tool- oder Bibliotheks-Repos ohne eigene fachmethodische Setzung; dort genügt eine kurze Methodensektion im Charter-Dokument. Sie trägt nicht für reine Anleitung an den Agenten (das ist Action-Layer, `CLAUDE.md`) und nicht für Forschungsergebnisse als Aussagen über den Gegenstand (die gehören in Veröffentlichungen, nicht in die Wissensbasis). Zwei Untertypen werden unterschieden, weil sie unterschiedliche Lesergruppen und Strukturen tragen, im selben Repo aber nebeneinander vorkommen: ^p0208

- (a) Methoden- und Begründungsschicht: das Warum. Theoretischer Rahmen, Forschungsfragen, methodische Entscheidungen mit akademischen Quellen. Typische Träger sind `research-framework.md`, `research-methodology.md` und `<subject>-methodology.md`. ^p0209
- (b) Domänenspezifisches Regelwerk: das Wie der Auszeichnung. Editionsrichtlinien, TEI-Mapping, Kodiermanual, Ontologie, Berechnungslogik, normativ und auszeichnungsnah. Typische Träger `editorial-guidelines.md`, `tei-mapping.md`, `ontology.md`. ^p0210

Ein Projekt kann beide Untertypen in getrennten Dateien führen (notker-edition trennt die Theorie nicht aus, agentic-edition-pipeline führt Regelwerk in `03_CONTEXT.md` und `04_TEI_MAPPING.md`), oder das Regelwerk trägt eine knappe Begründungssektion am Kopf und bleibt eine Datei. Die Spaltung folgt derselben Rhythmus-Logik wie in [Vorlage Architecture](#promptotyping-document-architecture): getrennt, sobald Begründung und Regelwerk eigene Aktualisierungsrhythmen und Lesergruppen entwickeln. Diese Spaltung ist zugleich die Destillat-Grenze der Funktion; wächst ein Regelwerk über die Lesbarkeit, wird nach Phänomengruppen oder Untertypen in Themendateien geteilt, nie in ein Sammelsurium verlängert. ^p0211

Lebenszyklus: das Regelwerk (b) entsteht mit der ersten Probeauszeichnung und wird bei jeder neuen Regel und jedem geklärten Phänomen nachgezogen; geklärte Punkte wandern aus der Sektion Ungeklärte Phänomene in die Phänomen-Regeln. Die Begründungsschicht (a) entsteht früh und ändert sich danach selten. Das teuerste Verfallsmuster der Funktion ist das schematisch veraltete Regelwerk, das ein abgelöstes Schema weiter als geltend beschreibt, während das operative Team damit arbeitet; eine Schemaänderung zieht das Regelwerk im selben Arbeitsgang nach. ^p0212

#### Funktion des Dokuments

Das Dokument beantwortet, je nach Untertyp, zwei verschränkte Fragen. Untertyp (a): nach welchem theoretischen und methodischen Rahmen arbeitet das Projekt, welche Forschungsfragen leitet es, welche Literatur und welche disziplinären Standards begründen die Entscheidungen. Untertyp (b): nach welchen Regeln wird das Material ausgezeichnet, gemappt oder berechnet, wie wird jedes relevante Phänomen behandelt, und welche Phänomene sind noch ungeklärt. ^p0213

Adressiert sind drei Lesergruppen. Ein Fachexperte (Editor, Domänenwissenschaftler, Förderreferent) prüft die methodische Tragfähigkeit und nutzt das Regelwerk als Referenz für die manuelle Nachbearbeitung und für die Kommunikation mit dem Auftraggeber. Ein Reviewer beurteilt, ob die Entscheidungen begründet und konsistent sind. Ein Coding-Agent liest das Dokument, bevor er Auszeichnungs- oder Berechnungscode generiert; bei Untertyp (b) sind die Mapping-Regeln die direkte Vorgabe für den Annotations- oder Transformationsschritt, bei Untertyp (a) verorten Theorie und Quellen den Agenten im richtigen Wissensfeld. Eine vage Regelschicht führt zu Auszeichnungen, die die intendierte Semantik verfehlen. ^p0214

#### Strukturprinzipien

Drei Prinzipien tragen das Dokument. ^p0215

Erstens trennt es Vorgabe von Material und Specification. Was die Daten sind und woher sie kommen, gehört in `data.md` ([Vorlage Datengrundlage](#promptotyping-document-data)); das Material ist der Gegenstand. Was das System tun soll, gehört in `specification.md` ([Vorlage Specification](#promptotyping-document-specification)); die Spezifikation ist die Substanz. Nach welcher fachlichen Regel das Material ausgezeichnet oder das Ergebnis begründet wird, gehört hier hin. Diese Trennung ist die Existenzberechtigung der Funktion: das Regelwerk ist weder Gegenstand noch Funktionsumfang, sondern die wissenschaftliche Setzung dazwischen. ^p0216

Zweitens macht es jede Setzung begründet und jede Lücke explizit. Bei Untertyp (a) trägt jede methodische Entscheidung ihre Quelle und ihre Auswirkung; eine Forschungsentscheidung ohne Begründung ist eine Behauptung. Bei Untertyp (b) trägt jede Kodierungsregel ihre Begründung (warum dieses Element, nicht jenes) und ihre Abgrenzung (welche Grenzfälle wie behandelt werden); ungeklärte Phänomene werden in einer eigenen offenen Sektion benannt, nicht stillschweigend übergangen. Was noch mit dem Auftraggeber zu klären ist, steht als offene Frage im Dokument. ^p0217

Drittens verweist es auf die maschinenlesbare Quelle statt sie zu duplizieren. Wo ein Schema die formale Wahrheit trägt (RelaxNG-Schema, ODD, JSON-Schema, OWL-Ontologie, Vokabulardatei), paraphrasiert das Dokument das Schema und verlinkt die Schema-Datei im Repo als Source of Truth. Die Regelbeschreibung ist die lesbare Schicht, das Schema die prüfbare; sie laufen nicht auseinander, weil das Dokument das Schema nicht nacherzählt, sondern interpretiert. ^p0218

#### Frontmatter-Schema

Das Dokument folgt dem reduzierten Frontmatter-Pflichtkern aus der [Konvention Promptotyping Documents](#konvention-v0.1) (Stand 2026-06-13): `title`, `project` (Objekt mit `name` und `repository`), `method` (Objekt mit `name` und `url`), `status`, `created`, `updated`. Der Zweck lebt als erster Absatz unter der H1. `status` meint die Dokument-Maturity (`idea`, `draft`, `stub`, `complete`, `reviewed`, `archived`; seit 2026-07-19 auch `active` für fortlaufende Prozessdokumente und `snapshot` für Stichtagsdokumente), nicht den operativen Projektstatus. Empfohlen sind `template` (als Block mit `name`, `version`, `url`, `alias`, wo diese Vorlage angewandt wurde), `language`, `version` (repoweit konsistent), `authors` beziehungsweise `generated-with`, `topics` und `related`. `authors` trägt ausschließlich Menschen, auch wenn ein LLM den Text erzeugt hat; `generated-with` nennt Harness und LLM im Format `Harness (LLM)`, etwa `Claude Code (Claude Opus 5)`, siehe Sektion *Provenienz im Frontmatter* der Konvention. Spezifisch für Domänenwissen: ^p0219

- `topics:` verortet den Agenten im fachlichen Wissensfeld und ist hier besonders tragend. Bei Untertyp (b) typisch `[[TEI]]`, `[[Editorial Guidelines]]`, `[[Critical Apparatus]]`, je nach Sprache und Korpus zusätzlich Sprach- oder Periodenkonzepte (`[[Old High German]]`). Bei Ontologie-Projekten `[[RDF]]`, `[[OWL]]`, das eingesetzte Vokabular (`[[RiC-O]]`, `[[CIDOC CRM]]`). Bei Untertyp (a) die Theoriefelder (`[[Mobility Studies]]`, `[[Explainable AI]]`, `[[Historical Information]]`). ^p0220
- `knowledge-sources:` ist hier zentral und sollte gepflegt sein. Mindestens `standards:` (eingesetzte Standards, Schemata, Guidelines mit URI: TEI P5, ISO-Codes, WCAG, fachliche Editionsrichtlinien) und, wo zutreffend, `vocabularies:` (kontrollierte Vokabulare, Normdaten-Autoritäten) sowie `datasets:` oder `institutions:` für referenzierte Referenzprojekte. Bei Untertyp (a) tragen die akademischen Primärquellen entweder hier als `standards:`-Anschlüsse oder, sprechender, in der Dokumentsektion `Quellen`. ^p0221
- `related:` typischerweise `data`, `specification`, `design`; die Dokumente, die auf dem Regelwerk aufsetzen oder es verwenden. ^p0222

Sonderfall Vault-Atom-Struktur. Methoden- und Theoriedokumente vom Untertyp (a), die als atomare Wissenseinheit lesbar bleiben sollen, folgen oft nicht dem Promptotyping-Frontmatter, sondern der Vault-Atom-Struktur aus CLAUDE §3 und §4: `type: knowledge`, `created`, `tags`, `status`, und im Korpus `## Summary`, `## Sources`, `## Related` statt `knowledge-sources:` im Frontmatter. Das ist kein Fehler, sondern die angemessene Form, wenn das Dokument primär als Wissensatom und weniger als Agenten-Kontext im Repo gelesen wird (hist-info-model führt seine Theorie-Dokumente so). Welche der beiden Frontmatter-Formen trägt, entscheidet die primäre Lesergruppe: Agent-zentrierter Repo-Kontext nimmt das Promptotyping-Frontmatter, atomares Wissensdokument nimmt die Vault-Atom-Struktur. ^p0223

#### Abschnitte im Detail

Die Sektionsstruktur unterscheidet sich nach Untertyp. Gemeinsam ist der Lead-Absatz (der Zweck-Satz). Optionale Sektionen, die nicht zutreffen, werden weggelassen, nicht leer geführt. ^p0224

##### Lead (beide Untertypen, Pflicht)

Funktion: in einem Satz den Zweck des Dokuments tragen, dann in einem bis drei Sätzen den Geltungsbereich der Regeln beziehungsweise des Rahmens. Inhalt: was das Dokument festlegt oder begründet, für welches Korpus oder welche Pipeline-Stufe es gilt, wozu es als Referenz dient (manuelle Nachbearbeitung, Skalierung auf den Gesamtbestand, Kommunikation mit dem Auftraggeber). ^p0225

##### Untertyp (a): Methoden- und Begründungsschicht

`## Theoretischer Rahmen`. Funktion: das Projekt im disziplinären Feld verorten. Inhalt: die tragenden Theorien und ihre Vertreter mit Kurzbeleg, der Forschungsstand (verwandte Projekte, Vorläufer), die Lücke, die das Projekt schließt. Eine bis fünf benannte Bezüge, jeder mit einem Satz, warum er trägt. ^p0226

`## Forschungsfragen`. Funktion: die leitenden Fragen explizit machen. Inhalt: nummerierte Forschungsfragen, gegebenenfalls eine Hypothese und ein Machbarkeitsziel. Trägt nur, wo das Projekt eine Forschungsstudie ist; reine Methodik-Dokumente ohne eigene Fragestellung lassen die Sektion weg. ^p0227

`## Forschungsgestützte Entscheidungen`. Funktion: jede methodische oder Design-Entscheidung an ihre Quelle und Auswirkung binden. Inhalt: pro Erkenntnis ein Dreischritt aus Erkenntnis (was die Literatur zeigt), Quelle (Primärbeleg mit DOI oder URL) und Auswirkung (was im Projekt deshalb konkret so gebaut wird). Eine abschließende Übersichtstabelle Entscheidung gegen Forschungsgrundlage verdichtet die Sektion. Das ist die tragende Struktur des Untertyps (a): sie verbindet Theorie nachprüfbar mit Praxis. ^p0228

`## Forschungskontext`. Funktion: den konkreten Gegenstandsraum benennen, in dem die Methodik operiert. Inhalt: Fallbeispiel, institutioneller oder historischer Rahmen, einschlägige Literatur, benannte Forschungslücken. Optional; trägt, wo der Kontext nicht schon im Charter-Dokument steht. ^p0229

`## Quellen` beziehungsweise `## Sources`. Funktion: die zitierte Literatur vollständig nachweisen. Inhalt: akademische Referenzen mit Autor, Jahr, Titel, DOI oder URL. Bei Vault-Atom-Struktur ist diese Sektion Pflicht und ersetzt `knowledge-sources:` im Frontmatter. ^p0230

##### Untertyp (b): Domänenspezifisches Regelwerk

`## Begründung` (optional). Funktion: die fachliche Grundentscheidung tragen, falls der Untertyp (a) nicht als eigene Datei existiert. Inhalt: zwei bis fünf Sätze zur Wahl der Auszeichnungs- oder Berechnungslogik mit Verweis auf das einschlägige Vorbild oder die Referenzedition. Entfällt, wenn `research-framework.md` oder `research-methodology.md` die Begründung trägt. ^p0231

`## Phänomene und ihre Behandlung` (Kern). Funktion: für jedes relevante Phänomen die Regel festlegen. Inhalt: pro Phänomen eine Beschreibung, die normative Kodierung oder Berechnung (Codeblock mit dem konkreten Element, Attribut oder der Formel), die Begründung der Wahl und die Abgrenzung der Grenzfälle. Bei Editionsprojekten ist das die Auszeichnung der Textschichten, Sprachwechsel, Glossen, Apparate, Fußnoten; bei Berechnungslogiken die Formel pro Metrik mit Bedingungen. Das ist der voluminöseste Teil und wird nach Phänomengruppen gegliedert. ^p0232

`## Mapping-Tabellen`. Funktion: die Zuordnung von Quellstruktur zu Zielstruktur kompakt führen. Inhalt: Tabellen Quellelement gegen Zielelement gegen Regel (etwa Absatz gegen `<p>` gegen Trennregel; Metadatenfeld gegen TEI-Header-Element gegen Quelle). Bei TEI-Projekten Header-Mapping und Body-Mapping getrennt. Trägt überall, wo eine systematische Eins-zu-eins- oder Eins-zu-viele-Zuordnung besteht. ^p0233

`## Header- und Schema-Deklarationen`. Funktion: die formalen Setzungen im Schema benennen, die das Regelwerk voraussetzt. Inhalt: Taxonomien, Klassendeklarationen, kontrollierte ID-Listen (Textzeugen, Quellen, Vokabular-IDs), Schemaprofil und Variantenkodierung. Verweis auf die Schema-Datei im Repo als Source of Truth; das Dokument paraphrasiert, ersetzt sie nicht. ^p0234

`## Ungeklärte Phänomene` (Pflicht, wenn welche bestehen). Funktion: offene Punkte explizit machen, die das Regelwerk noch nicht entscheidet. Inhalt: Tabelle Phänomen gegen Status gegen Auswirkung auf die Kodierung, jeweils mit der zu klärenden Instanz (typischerweise dem Auftraggeber). Eine bewusst nicht entschiedene Frage steht hier, nicht in einer Fußnote. ^p0235

`## Konventionen für das Gesamtprojekt` (optional). Funktion: die Skalierung der für ein Pilot- oder Probesegment entwickelten Regeln auf den Gesamtbestand vorbereiten. Inhalt: wie die Kodierung auf weitere Einheiten erweitert wird, Referenzprojekte, Code-Tabellen (Sprach-Codes, Sigel-Systeme). Trägt, wo ein Prototyp auf einen größeren Bestand skaliert. ^p0236

#### Was nicht reingehört

- Material und Datenherkunft. Was die Daten sind, woher sie kommen, wie groß der Bestand ist, gehört in `data.md` ([Vorlage Datengrundlage](#promptotyping-document-data)). Das Domänenwissen verlinkt die Datengrundlage für die empirische Basis (etwa die konkreten Sigel-Bedeutungen), führt sie aber nicht selbst. ^p0237
- Funktionsumfang und Akzeptanzkriterien. Was das System leisten soll, gehört in `specification.md` ([Vorlage Specification](#promptotyping-document-specification)). Das Regelwerk sagt, nach welcher fachlichen Logik ausgezeichnet wird, nicht welche Features das Frontend hat. ^p0238
- Technische Realisierung. Mit welchem Skript das Mapping ausgeführt wird, welcher Stack die Pipeline trägt, gehört in `architecture.md` ([Vorlage Architecture](#promptotyping-document-architecture)). Das Regelwerk nennt die Funktion (`chain_cross_verse_hyphens()` setzt die Cross-Verse-Verkettung um), nicht ihre Implementation. ^p0239
- Imperative Agenten-Anweisung. Wie der Agent sich verhalten soll, gehört in den Action-Layer (`CLAUDE.md`, [Vorlage Action-Layer](#promptotyping-document-action-layer)). Das Regelwerk ist deklaratives Knowledge; der Action-Layer verweist darauf. ^p0240
- Forschungsergebnisse als Aussagen über den Gegenstand. Was die Edition oder die Auswertung inhaltlich zeigt, ist Sache der Veröffentlichungen, nicht des Domänenwissens. Das Dokument trägt die Regel und ihre Begründung, nicht das Resultat ihrer Anwendung. Werden aus der Anwendung der Regeln empirische Befunde oder Neuheitsansprüche außenwirksam erhoben, prüft sie das `verification.md` des Projekts ([Vorlage Verification](#promptotyping-document-verification)). ^p0241

#### Vorlage zum Befüllen

Zwei Blöcke, einer pro Untertyp. Der erste deckt das domänenspezifische Regelwerk (b) ab, der zweite die Methoden- und Begründungsschicht (a) im Promptotyping-Frontmatter; eine Variante des zweiten Blocks zeigt die Vault-Atom-Struktur für den Fall, dass das Dokument primär als Wissensatom gelesen wird. Optionale Sektionen, die nicht zutreffen, werden vor dem Commit gelöscht, nicht leer gelassen. Der erste Absatz trägt den Zweck. ^p0242

##### Untertyp (b): Regelwerk

````markdown
---
title: [Editionsrichtlinien | TEI-Mapping | Ontologie | Kodiermanual]
project:
  name: [Projektname]
  repository: [Repository-URL]
method:
  name: Promptotyping
  url: https://lisa.gerda-henkel-stiftung.de/digitale_geschichte_pollin
status: draft
created: [YYYY-MM-DD]
updated: [YYYY-MM-DD]
template:
  name: Vorlage Domänenwissen
  version: 0.3
  url: https://dhcraft.org/Promptotyping/promptotyping-document/domain-knowledge
  alias: https://dhcraft.org/Promptotyping/#promptotyping-document-domain-knowledge
language: [de | en]
version: [Repo-Schema-Version]
authors: [Autor 1, Autor 2]
generated-with: [Harness (LLM), falls relevant]
topics: ["[[TEI]]", "[[Editorial Guidelines]]"]
knowledge-sources:
  standards:
    [Standard, etwa TEI P5 Guidelines]: [URI]
  vocabularies:
    [Vokabular oder Normdaten-Autorität]: [URI]
related: [data, specification, design]
---

### [Titel]

<!-- Lead: erster Satz trägt den Zweck. Dann ein bis drei Sätze Geltungsbereich: welches Korpus, welche Pipeline-Stufe, wozu Referenz. -->

[Zweck-Satz und Geltungsbereich]

#### Begründung

<!-- Optional. Entfällt, wenn ein eigenes research-framework.md die Begründung trägt. Warum diese Auszeichnungs- oder Berechnungslogik, mit Vorbild oder Referenzedition. -->

[...]

#### Phänomene und ihre Behandlung

<!-- Kern. Pro Phänomen: Beschreibung, normative Kodierung im Codeblock, Begründung, Abgrenzung der Grenzfälle. Nach Phänomengruppen gliedern. -->

##### [Phänomengruppe]

[Beschreibung]

```xml
[konkretes Element/Attribut] ^p0243
```

- [Attribut/Regel]: [Bedeutung]

**Abgrenzung:** [Grenzfälle und ihre Behandlung]

#### Mapping-Tabellen

<!-- Zuordnung Quellstruktur zu Zielstruktur. Bei TEI Header- und Body-Mapping getrennt. -->

| Quellelement | Zielelement | Regel |
|---|---|---|
| [Quellelement] | [Zielelement] | [Regel] |

#### Header- und Schema-Deklarationen

<!-- Taxonomien, kontrollierte ID-Listen, Schemaprofil. Verweis auf die Schema-Datei als Source of Truth. -->

[...]

#### Ungeklärte Phänomene

<!-- Pflicht, wenn welche bestehen. Phänomen, Status, Auswirkung auf die Kodierung, zu klärende Instanz. -->

| Phänomen | Status | Auswirkung auf Kodierung |
|---|---|---|
| [Phänomen] | [zu klären mit ...] | [Auswirkung] |

#### Konventionen für das Gesamtprojekt

<!-- Optional. Skalierung des Prototyp-Regelwerks auf den Gesamtbestand, Referenzprojekte, Code-Tabellen. -->

[...]
````

##### Untertyp (a): Methoden- und Begründungsschicht

````markdown
---
title: [Forschungsrahmen | Methodik | Forschungsgrundlagen]
project:
  name: [Projektname]
  repository: [Repository-URL]
method:
  name: Promptotyping
  url: https://lisa.gerda-henkel-stiftung.de/digitale_geschichte_pollin
status: draft
created: [YYYY-MM-DD]
updated: [YYYY-MM-DD]
template:
  name: Vorlage Domänenwissen
  version: 0.3
  url: https://dhcraft.org/Promptotyping/promptotyping-document/domain-knowledge
  alias: https://dhcraft.org/Promptotyping/#promptotyping-document-domain-knowledge
language: [de | en]
version: [Repo-Schema-Version]
authors: [Autor 1, Autor 2]
generated-with: [Harness (LLM), falls relevant]
topics: ["[[Mobility Studies]]", "[[Explainable AI]]"]
related: [project, data, specification]
---

### [Titel]

<!-- Lead: erster Satz trägt den Zweck. Dann ein bis drei Sätze: welcher Rahmen, wofür er trägt. -->

[Zweck-Satz und Rahmung]

#### Theoretischer Rahmen

<!-- Tragende Theorien mit Vertreter und Kurzbeleg, Forschungsstand, Lücke. Pro Bezug ein Satz, warum er trägt. -->

[...]

#### Forschungsfragen

<!-- Optional. Nummerierte Fragen, ggf. Hypothese und Machbarkeitsziel. Entfällt bei reinen Methodik-Dokumenten ohne eigene Fragestellung. -->

**FF1.** [...]

**Hypothese.** [...]

#### Forschungsgestützte Entscheidungen

<!-- Kern. Pro Erkenntnis: Erkenntnis, Quelle (DOI/URL), Auwirkung (was deshalb konkret so gebaut wird). Abschluss: Übersichtstabelle. -->

##### [Nr.] [Erkenntnis in einem Titel]

**Erkenntnis:** [...]

**Quelle:** [Autor, Jahr, Titel, DOI/URL]

**Auswirkung:** [Was im Projekt deshalb konkret so gebaut wird]

---

| Design-Entscheidung | Forschungsgrundlage |
|---|---|
| [Entscheidung] | [Quelle] |

#### Forschungskontext

<!-- Optional. Fallbeispiel, institutioneller/historischer Rahmen, einschlägige Literatur, benannte Forschungslücken. -->

[...]

#### Quellen

<!-- Akademische Referenzen mit Autor, Jahr, Titel, DOI/URL. -->

[...]
````

##### Variante: Vault-Atom-Struktur (für Untertyp a, wenn primär Wissensatom)

````markdown
---
type: knowledge
created: [YYYY-MM-DD]
tags: [2 bis 4 tags, lowercase-hyphenated]
status: draft
---

### [Titel]

#### Summary

<!-- Zwei bis drei Absätze. Erster Satz trägt den Zweck. -->

[...]

#### [Theoretischer Rahmen | Kernbegriffe | Methodische Setzung]

[...]

#### Sources

[Autor, Jahr, Titel. DOI/URL.]

#### Related

- [[Verwandtes Atom]] — [Beziehung in einem Halbsatz]
````

#### Anwendung als Prompt-Template

Strukturanker beim Aufsetzen des Domänenwissens. Zuerst entscheidet der Agent (oder der Fachexperte), welcher Untertyp trägt und ob beide getrennt geführt werden. Den passenden Template-Block in eine neue Datei im `knowledge/`-Ordner kopieren und iterativ befüllen. Untertyp (b) wird aus dem real existierenden Quellmaterial befüllt (Probeseite, DOCX, Schema-Datei, bestehende Referenzedition): pro Phänomen wird die Regel aus einem realen Beleg abgeleitet, nicht erfunden. Untertyp (a) wird aus der Literatur befüllt; jede Erkenntnis braucht eine prüfbare Primärquelle mit DOI oder URL. Da diese Schicht fachwissenschaftliche Setzung trägt, ist sie der Teil der Wissensbasis, der am dringendsten vom Critical Expert verifiziert werden muss (Critical Expert in the Loop); Grenzfälle und ungeklärte Phänomene werden nicht weggeglättet, sondern als offene Frage an den Auftraggeber stehen gelassen. Recherchequellen werden gegen das Verbot von Grokipedia geprüft. ^p0244

Review-Folie für ein bestehendes Domain-Knowledge-Dokument. Ein vorhandenes `editorial-guidelines.md`, `tei-mapping.md`, `research-framework.md` oder `research-methodology.md` wird gegen Naming Contract, Lead, Begründungen, Quellen und Auswirkungen geprüft. Das Review kontrolliert außerdem die Abgrenzung zu `data.md` und `specification.md` sowie den Verweis auf eine autoritative Schema-Datei. ^p0245

#### Beispiel

Domänenspezifisches Regelwerk, voll ausgereizt (Untertyp b): notker-edition führt `editorial-guidelines.md` als TEI-Kodierungsrichtlinien für Notkers Psalmenkommentar. Der Lead trägt den Zweck in einem Satz und nennt die drei Verwendungen (manuelle Nachbearbeitung, Erweiterung auf alle 150 Psalmen, Kommunikation mit dem Auftraggeber). Der Kern gliedert die Textphänomene: Notkers drei funktionale Textschichten (Psalmzitation, Übersetzung, Kommentar) werden je als `<seg type="..." ana="...">` mit konkretem Codeblock kodiert, der Sprachwechsel als `<foreign xml:lang="...">`, Interlinearglossen als `<ab>` mit `<gloss>`. Jede Regel trägt ihre Begründung (etwa "`<seg>` statt `<quote>`, weil Notker paraphrasiert") und ihre Abgrenzung (Lehnwörter werden getaggt, Eigennamen nicht). Die Sektion Header-Deklarationen führt die Textfunktions-Taxonomie und die kontrollierten ID-Listen für Textzeugen (`wit-G`, `wit-R`, `wit-H`) und Kommentarquellen (`src-A`, `src-C`), mit Verweis auf das RelaxNG-Schema (`data/schema/tei_all.rng`) als formale Source of Truth. Eine eigene Sektion Ungeklärte Phänomene führt die offenen Punkte (Semantik der Siglen G und R in der Haupttext-Spalte, Versgrenze 12/13) als Tabelle mit der Auflösung "mit Auftraggeber klären". Eine Theorie- oder Begründungssektion vom Untertyp (a) ist hier nicht separat ausgelagert; die Begründungen sitzen jeweils an der einzelnen Regel. ^p0246

Regelwerk in Skelettform (Untertyp b, frühe Phase): agentic-edition-pipeline spaltet das Regelwerk in `03_CONTEXT.md` (Editionsrichtlinien: Transkriptionskonventionen, Normalisierungen, Annotationstypen, Normdaten) und `04_TEI_MAPPING.md` (TEI-Profil DTABf mit Verweis auf `schemas/dtabf.json`, Header-Mapping- und Body-Mapping-Tabelle Quellelement gegen TEI-Element gegen Regel, Annotationsregeln, Register). Beide Dokumente sind als ausfüllbares Skelett mit `[TODO]`-Markern angelegt und zeigen die Mapping-Tabellen-Struktur in Reinform; sie belegen, dass die Regelwerk-Funktion auch als Vorab-Gerüst vor dem Befüllen trägt. ^p0247

Methoden- und Begründungsschicht mit akademischen Quellen (Untertyp a): dia-xai führt `RESEARCH.md` als Forschungsgrundlagen. Der Lead trägt den Zweck ("destillierte Erkenntnisse aus der Forschungsliteratur, die unsere Designentscheidungen begründen") und das Strukturversprechen (jede Erkenntnis mit Primärquelle und konkreter Auswirkung). Jede der elf Sektionen folgt dem Dreischritt Erkenntnis, Quelle, Auswirkung: etwa der Anchoring-Bias bei Pre-Annotation (Berzak et al., EMNLP 2016) führt zur Designentscheidung "Rohtext in der Verify-Ansicht immer sichtbar". Eine abschließende Tabelle Design-Entscheidung gegen Forschungsgrundlage verdichtet die elf Erkenntnisse. Das ist die Reinform des Untertyps (a): nachprüfbare Bindung jeder Praxisentscheidung an eine Primärquelle. ^p0248

Ein Forschungsrahmen einer Studie wird als `research-framework.md` geführt. Er trägt den theoretischen Rahmen, relevante Vorarbeiten, Forschungslücken und Forschungsfragen mit Quellen in einer eigenen Sektion. ^p0249

Vault-Atom-Variante (Untertyp a als Wissensatom): hist-info-model führt seine Theorie-Dokumente im Ordner `knowledge/01-theory/` nicht im Promptotyping-Frontmatter, sondern in der Vault-Atom-Struktur. `Historical-Information.md` trägt `type: knowledge` plus `tags` und `status: draft` im Frontmatter und im Korpus `## Summary`, dann die fachliche Setzung (fünf Eigenschaften, drei Primitive, offene Frage nach ihrer Beziehung), dann `## Sources` (Pollin, Thaller, Koselleck, Langefors) und `## Related` mit erläuterten Wikilinks. Das belegt den Sonderfall: ein Methoden- und Theoriedokument, das primär als atomare Wissenseinheit gelesen wird, folgt der Vault-Struktur statt dem Promptotyping-Frontmatter. ^p0250

#### Begriffe

- Domänenwissen: die fachmethodische Vorgabe- und Theorieschicht eines Projekts; die Regeln, nach denen Material ausgezeichnet oder berechnet wird, und ihre wissenschaftliche Begründung. Weder Material (Gegenstand) noch Specification (Funktionsumfang). ^p0251
- Methoden- und Begründungsschicht (Untertyp a): der theoretische Rahmen und die forschungsgestützte Begründung der Projektentscheidungen, mit akademischen Quellen. Beantwortet das Warum. ^p0252
- Domänenspezifisches Regelwerk (Untertyp b): die normative, auszeichnungsnahe Vorgabe (Editionsrichtlinien, TEI-Mapping, Kodiermanual, Ontologie, Berechnungslogik). Beantwortet das Wie der Auszeichnung. ^p0253
- Mapping: die systematische Zuordnung von Quellstruktur zu Zielstruktur (Quellelement zu TEI-Element, Metadatenfeld zu Header-Element), Kern des Untertyps (b). ^p0254
- Ungeklärtes Phänomen: ein Fall, für den das Regelwerk noch keine Entscheidung trägt und der explizit als offene, mit dem Auftraggeber zu klärende Frage benannt wird, statt stillschweigend übergangen zu werden. ^p0255
- Source of Truth (für Schemata): die maschinenlesbare Datei (RelaxNG-Schema, ODD, JSON-Schema, OWL-Ontologie), die die formale Wahrheit trägt; das Domänenwissen-Dokument paraphrasiert und verlinkt sie, ersetzt sie nicht. ^p0256

#### Versionshistorie

- 0.3 (2026-08-21): Naming Contract übernommen. Fachliche Präfixe und Funktionsnamen sind englisch; Spezialisierungen folgen `<subject>-<function>.md`. ^p0257
- 0.2 (2026-07-19): Freigabe (status complete), englisches Funktionsvokabular (Domain Knowledge), Status-Vokabular auf den Stand der Konvention, `knowledge-sources`-Platzhalter auf die kanonische Map-Form, Lebenszyklus und Destillat-Grenze, Verification-Verweis. Die drei Template-Blöcke (Regelwerk, Begründungsschicht, Vault-Atom-Variante) sind geprüft und bleiben als echte Genres bestehen. Keine Migrationspflicht für bestehende Repos. ^p0258
- 0.1 (2026-06-13): Erstfassung, empirisch aus notker-edition, agentic-edition-pipeline, dia-xai, m3gim und hist-info-model. ^p0259

#### Related

- [Konvention Promptotyping Documents](#konvention-v0.1) ^p0260
- [Vorlage Datengrundlage](#promptotyping-document-data) ^p0261
- [Vorlage Specification](#promptotyping-document-specification) ^p0262
- [Vorlage Architecture](#promptotyping-document-architecture) ^p0263

## Template `user-stories.md`: Vorlage User Stories

Source file `_content/promptotyping-document/user-stories.md`, template version 0.2. ^p0264


### Vorlage User Stories

Diese Vorlage strukturiert das User-Stories-Dokument einer Promptotyping-Wissensbasis für den Ausnahmefall der ausgelagerten Datei. Seit der Konventionsänderung 2026-05-30 ist der Default, Epics und User Stories als eigene Sektion in `specification.md` zu führen ([Vorlage Specification](#promptotyping-document-specification), ab Vorlagen-Version 0.2); die Strukturprinzipien dieser Vorlage gelten dort unverändert. Eine separate Datei (typischerweise `user-stories.md`, alternativ `scholar-user-stories.md` bei Forschungsprojekten) ist die dokumentierte Ausnahme für große Projekte, deren Substanz-Funktion gespalten wird. ^p0265

#### Geltungsbereich

Die Vorlage trägt als separate Datei nur, wenn die Substanz-Funktion des Projekts gespalten wird, typischerweise bei großen Editionsprojekten, deren `specification.md` sonst unlesbar würde (dokumentierte Ausnahme, Konventionsänderung 2026-05-30). Default ist die Sektion Epics und User Stories in `specification.md`. Inhaltliche Voraussetzung bleibt in beiden Formen: Das Projekt hat eine UI und mehrere Nutzer-Personas oder Forschungsoperationen sind unterscheidbar; bei reinen Pipeline- oder Tool-Repos entfällt die Funktion, weil dort kein Anwendungsszenario im Sinne von Forschungsoperationen existiert. Sie trägt nicht für Personas oder Empathy Maps; diese sind eigene UX-Artefakte und gehören gegebenenfalls in eine `personas.md`. Sie trägt auch nicht für formale funktionale Anforderungen; diese gehören in `specification.md`. ^p0266

#### Funktion des Dokuments

Das Dokument beantwortet "wer benutzt das System wie und warum". Es übersetzt die formalen Anforderungen aus `specification.md` in narrative Anwendungsszenarien, Sätze im Format „Als [Rolle] möchte ich [Ziel], damit [Nutzen]". Adressiert sind drei Lesergruppen: ein Forschender oder Anwender, der prüfen will, ob das System sein Anliegen unterstützt; ein UX-Designer, der die Interaktion gegen Szenarien testet; ein Coding-Agent, der eine neue Funktion baut und prüfen muss, welche Szenarien sie betrifft. ^p0267

Im Promptotyping-Kontext sind User Stories die Brücke zwischen Scholar-Centered Design (siehe Glossar) und Implementation. Sie entstehen typischerweise in der Preparation- oder Exploration-Phase aus Sessions mit Domänenexperten und werden iterativ verfeinert. ^p0268

#### Strukturprinzipien

Vier Prinzipien tragen das Dokument. ^p0269

Erstens trennt es Anwender-Perspektive von System-Perspektive. Eine User Story sagt, was eine Anwenderin will und warum, nicht was das System leistet. Was das System leistet, gehört in `specification.md`. Diese Trennung verhindert, dass User Stories zu verklausulierten Feature-Listen werden. ^p0270

Zweitens ist jede Story dreigliedrig: Rolle, Ziel, Nutzen. Eine Story ohne Nutzen ist eine Funktionswunschäußerung; eine Story ohne Rolle ist eine generische Anforderung. Das Dreigliedrige macht Stories untereinander vergleichbar und gegen formale Anforderungen abprüfbar. ^p0271

Drittens trägt jede Story eine Ableitung. Welche Anforderung in `specification.md` realisiert das Szenario, welche Komponente in `architecture.md` oder `design.md` ist beteiligt, welche Begriffe aus dem INDEX-Glossar werden vorausgesetzt. Diese Ableitung ist die Verlinkung der Story in die Wissensbasis und macht sie maschinenlesbar. ^p0272

Viertens führt jede Story ihren epistemischen Status. Eine Story ist eine Hypothese über den Anwender, bis der benannte Anwender sie bestätigt hat. Sie ist entweder als validiert markiert (durch wen, wann) oder als Annahme mit Beobachtungspunkt nach dem Muster "Effekt: to be observed", inklusive des Ereignisses, an dem er aufgelöst wird. Stories von Proxies sind als solche gekennzeichnet. Die Begründung geht auf den FemPrompt-Fall zurück (siehe Praxis-Sektion, [Epistemischer Status von User Stories](#praxis-the-epistemic-status-of-user-stories)); die Prüfkriterien stehen im folgenden Abschnitt. ^p0273

#### Prüfkriterien

Die Kriterien für ein User-Stories-Dokument stammen aus dem Quality-User-Story-Framework (Lucassen et al. 2016), ergänzt um Punkte aus dem agentischen Setting. Die Trennlinie zieht die Quelle selbst, weil ihr Werkzeug AQUSA die Kriterien prüft, über die eine Regel entscheidet, und die ausschließt, die Verständnis des Inhalts verlangen. Alle QUS-Kriterien beurteilen die intrinsische Qualität des Story-Textes; ob die Story für den Nutzer zutrifft, den sie benennt, liegt außerhalb von ihnen und ist der Grund für die Ergänzungen. ^p0274

##### Was ein Skript entscheidet

Die Kriterien, für die AQUSA einen Analyzer implementiert, dazu zwei Ergänzungen dieser Site. ^p0275

- **Well-formed.** Die Story enthält mindestens Rolle und Mittel. ^p0276
- **Atomic.** Die Story formuliert die Anforderung an genau ein Feature. ^p0277
- **Minimal.** Die Story enthält nichts außer Rolle, Mittel und Zweck. ^p0278
- **Unique.** Jede Story ist einmalig, Dubletten werden vermieden (am Story-Satz zu prüfen). ^p0279
- **Uniform.** Alle Stories eines Dokuments verwenden dieselbe Schablone (am Story-Satz zu prüfen). ^p0280
- **Story-ID** (Ergänzung dieser Site). Jede Story trägt eine stabile Kennung, auf die Akzeptanzkriterien, Tests und Journaleinträge verweisen können. ^p0281
- **Validierungsstatus** (Ergänzung dieser Site). Jede Story trägt ein Feld für den Status, im Fall der Annahme samt Beobachtungspunkt. Ein Skript prüft die Präsenz des Feldes und nicht die Wahrheit seiner Angabe. ^p0282

##### Was der Mensch einlöst

Die übrigen QUS-Kriterien, dazu eine dritte Ergänzung dieser Site. Die Quelle nimmt die semantischen aus ihrem Werkzeug aus, weil sie Verständnis des Inhalts verlangen; bei Full sentence liegt der Grund allein darin, dass die berichtete Werkzeugversion dafür keinen Analyzer führt. ^p0283

- **Conceptually sound.** Das Mittel benennt ein Feature und der Zweck eine Begründung. ^p0284
- **Problem-oriented.** Die Story benennt allein das Problem; die Lösung dafür bleibt draußen. ^p0285
- **Unambiguous.** Die Story vermeidet Begriffe und Abstraktionen, die mehrere Lesarten zulassen. ^p0286
- **Full sentence.** Die Story ist ein wohlgeformter vollständiger Satz. ^p0287
- **Estimatable.** Die Story bezeichnet keine grobkörnige Anforderung, die sich schwer planen und priorisieren lässt. ^p0288
- **Conflict-free.** Keine Story steht im Widerspruch zu einer anderen (am Story-Satz zu prüfen). ^p0289
- **Complete.** Die Umsetzung des Story-Satzes ergibt eine funktional vollständige Anwendung, ohne fehlende Schritte (am Story-Satz zu prüfen). ^p0290
- **Independent.** Die Story ist in sich geschlossen und hängt an keiner anderen (am Story-Satz zu prüfen). Die Quelle hält fest, dass sich das praktisch nie durchhalten lässt, und empfiehlt für den unvermeidbaren Fall, die Abhängigkeit ausdrücklich zu deklarieren. ^p0291
- **Validierung durch den benannten Nutzer** (Ergänzung dieser Site). Die Story ist von der Rolle bestätigt, die sie benennt, mit Angabe von wem und wann. ^p0292

#### Frontmatter-Schema

Das Dokument folgt dem Frontmatter-Schema aus der [Konvention Promptotyping Documents](#konvention-v0.1) (Pflichtkern: `title, project, method, status, created, updated`). Spezifisch für User Stories: ^p0293

- `topics:` typisch sind Scholar-Centered Design und User Stories. Bei Forschungsprojekten zusätzlich das Forschungsfeld als drittes Topic, soweit es das Befüllen leitet. ^p0294
- `knowledge-sources:` selten genutzt; User Stories tragen projekt-internes Wissen, nicht externe Anschlüsse. ^p0295
- `related:` typischerweise `specification`, `design` und gegebenenfalls `architecture`. User Stories sind das Bindeglied dieser drei. ^p0296

#### Abschnitte im Detail

##### Lead

Funktion: in zwei bis drei Sätzen den Charakter der Stories und ihre Adressaten benennen. Inhalt: typischerweise „Nutzungsszenarien aus Forscherinnen-Perspektive im Format `Als [Rolle], die …, will ich …, damit …`. Stories sind nach Forschungsoperationen, wissenschaftlicher Absicherung und begrifflicher Orientierung sortiert." Der Lead orientiert den Leser über das Story-Format und die Sortierung. ^p0297

##### Gruppen

Funktion: Stories nach Anliegen-Klassen ordnen. Inhalt: drei bis fünf Gruppen, die das Anliegen-Spektrum strukturieren. Bei Forschungsprojekten typischerweise „Zentrale Forschungsoperationen" (was das System tun soll), „Wissenschaftliche Absicherung" (Zitierbarkeit, Provenienz, Reproduzierbarkeit), „Begriffliche Orientierung" (Tooltip, Glossar-Zugang). Bei Editionsprojekten zusätzlich „Redaktionelle Arbeitsabläufe". Innerhalb jeder Gruppe Stories nach Häufigkeit oder Wichtigkeit sortiert. ^p0298

##### User Stories

Funktion: einzelne Anwendungsszenarien dokumentieren. Inhalt: pro Story eine Überschrift mit kurzem Titel, darunter die Story im Format „Als [Rolle], die [Kontext], will ich [Ziel], damit [Nutzen]." Anschließend die Ableitung als Liste: welche Anforderung, welche Komponente, welche Begriffe. ^p0299

Pro Story: ^p0300

- Titel als Überschrift (`### [Operation]`). ^p0301
- Story im Format „Als [Rolle], die …, will ich …, damit …", in einem Satz oder einem kurzen Absatz. ^p0302
- Ableitung als Bullet-Liste: Anforderung in `specification.md`, Komponente in `architecture.md` oder `design.md`, Begriffe aus `INDEX.md`. ^p0303

Die Stories sind nicht durchnummeriert; sie sind nicht IDs, sondern Beschreibungen. Sortierung innerhalb der Gruppen erfolgt nach inhaltlicher Logik, nicht nach Nummer. ^p0304

#### Was nicht reingehört

- Formale funktionale Anforderungen mit FR-IDs und Akzeptanzkriterien. Diese gehören in `specification.md`, Sektion Anforderungen. ^p0305
- Personas oder Empathy Maps. Diese sind eigene UX-Artefakte mit eigener Methodik. ^p0306
- Use Cases mit Schritt-für-Schritt-Abläufen. Use Cases sind detaillierter als User Stories; bei Bedarf werden sie als eigene `use-cases.md` geführt. ^p0307
- Implementations-Details. Wie die Story technisch realisiert ist, gehört in den Code oder in `architecture.md`. ^p0308

#### Vorlage zum Befüllen

Der folgende Block ist als Template gedacht. ^p0309

````markdown
---
title: User Stories
project:
  name: [Projektname]
  repository: [Repository-URL]
status: complete
language: [de | en]
version: [Repo-Schema-Version]
created: [YYYY-MM-DD]
updated: [YYYY-MM-DD]
authors: [Autor 1, Autor 2]
generated-with: [Harness (LLM), falls relevant]
method:
  name: Promptotyping
  url: https://lisa.gerda-henkel-stiftung.de/digitale_geschichte_pollin
template:
  name: Vorlage User Stories
  version: 0.1
  url: https://dhcraft.org/Promptotyping/promptotyping-document/user-stories
  alias: https://dhcraft.org/Promptotyping/#promptotyping-document-user-stories
topics: ["[[Scholar-Centered Design]]", "[[User Stories]]"]
related: [specification, design, architecture]
---

<!-- Lead: zwei bis drei Sätze. Story-Format und Sortierungs-Gruppen erklären. -->

[Lead-Absatz]

#### [Gruppe 1: zum Beispiel Zentrale Forschungsoperationen]

##### [Story-Titel]

*Als [Rolle], die [Kontext], will ich [Ziel], damit [Nutzen].*

Validierung: [validiert durch Rolle/Person am YYYY-MM-DD | Annahme (Proxy: wer), Effekt: to be observed, Auflösung: Ereignis]

Ableitung:
- Anforderung [[specification#Anforderung]]
- Komponente [[design#Komponente]] (oder [[architecture#Komponente]])
- Begriffe [[INDEX#Begriff A]], [[INDEX#Begriff B]]

##### [Nächster Story-Titel]

[...]

#### [Gruppe 2: zum Beispiel Wissenschaftliche Absicherung]

##### [Story-Titel]

[...]

#### [Gruppe 3: zum Beispiel Begriffliche Orientierung]

##### [Story-Titel]

[...]
````

#### Anwendung als Prompt-Template

Strukturanker beim Aufsetzen der User Stories. Stories entstehen aus Scholar-Centered-Design-Sessions, Domänen-Workshops oder Requirements-Engineering. Der Agent erhält Sitzungsnotizen oder Forschungsfragen und überführt sie in das dreigliedrige Format. Die Ableitung wird typischerweise nachträglich ergänzt, sobald `specification.md` und `architecture.md` Stand haben. ^p0310

Review-Folie für eine bestehende User-Stories-Datei. Eine vorhandene Datei wird gegen die Vorlage gehalten, um zu prüfen, ob jede Story dreigliedrig ist (Rolle, Ziel, Nutzen), ob die Ableitung gepflegt ist, und ob die Sortierungs-Gruppen das Anliegen-Spektrum sinnvoll strukturieren. ^p0311

#### Beispiel

sugw-Edition führt `scholar-user-stories.md` mit drei Gruppen (Zentrale Forschungsoperationen, Wissenschaftliche Absicherung, Begriffliche Orientierung). Charakteristisch ist die Ableitungsform unter jeder Story: drei Bullet-Punkte, die Anforderung (`requirements#…`), Komponente (`ui-design#…`) und Begriffe (`glossar#…`) als Wikilinks führen. Diese Ableitung ist die Verlinkung der Story in die Wissensbasis und macht das Dokument zur Brücke zwischen Anwender-Perspektive und System-Perspektive. ^p0312

Beispielstory aus sugw-Edition: ^p0313

```markdown
##### Verteilung einer Kategorie überblicken

*Als Forscherin, die Häufigkeitsstrukturen in einer Kategorie untersucht, will ich
jederzeit zwischen Gesamtnennung und Individueller Person umschalten, damit ich
Frequenz und Breite sauber voneinander trennen kann.*

Ableitung:
- Anforderung [[requirements#Umschaltbarkeit der Zählebenen]]
- Komponente [[ui-design#Zählebenen-Umschalter]]
- Begriffe [[glossar#Gesamtnennung]], [[glossar#Individuelle Person]]
```

#### Begriffe

- User Story: Anwendungsszenario im Format „Als [Rolle], die [Kontext], will ich [Ziel], damit [Nutzen]." Die kanonische Form aus dem agilen Requirements Engineering, hier auf Forschungsoperationen angewandt. ^p0314
- Rolle: die nutzende Person in einer typisierten Funktion, etwa Forscherin, Editor*in, Reviewer. Nicht ein konkreter Mensch. ^p0315
- Ableitung: die Verlinkung einer Story in die Wissensbasis. Bestimmt, welche Anforderung, Komponente und Begriffe das Szenario adressiert. ^p0316
- Anliegen-Gruppe: thematische Sortierung der Stories nach Forschungsoperation, wissenschaftlicher Absicherung oder begrifflicher Orientierung. ^p0317

#### Related

- [Vorlage Specification](#promptotyping-document-specification) ^p0318
- [Vorlage Design](#promptotyping-document-design) ^p0319
- [Vorlage Index](#promptotyping-document-index) ^p0320
- [Konvention Promptotyping Documents](#konvention-v0.1) ^p0321

## Template `specification.md`: Vorlage Specification

Source file `_content/promptotyping-document/specification.md`, template version 0.3. ^p0322


### Vorlage Specification

Diese Vorlage strukturiert das Substanz-Dokument einer Promptotyping-Wissensbasis. Das resultierende Dokument heißt typischerweise `specification.md` und liegt im `knowledge/`-Ordner des Repos. Es konsolidiert Anforderungen, Epics und User Stories, Funktionsumfang und Entscheidungen zu einer zentralen Datei und beantwortet die Was-und-Warum-Frage des Projekts am Stück. Seit Vorlagen-Version 0.2 (Konventionsänderung 2026-05-30) trägt es auch die narrativen Anwendungsszenarien, die zuvor per Default in einer separaten `user-stories.md` lagen. ^p0323

#### Geltungsbereich

Die Vorlage trägt für jedes Promptotyping-Repo, weil die Substanz-Funktion in der [Konvention Promptotyping Documents](#konvention-v0.1) als immer-relevant geführt wird. Bei sehr kleinen Projekten kann sie in `project.md` integriert werden. ^p0324

Spaltung als Norm. Größere Projekte teilen die Specification-Funktion regelmäßig in spezialisierte Träger wie `system-specification.md`, `feature-specification.md` und `architecture-decisions.md`. Eigenständige Forschungsfragen erhalten gegenstandsbezogene Funktionen wie `research-analysis.md` oder `research-exploration.md`. Die Teilung folgt eigenständigen Routing Questions oder Aktualisierungszyklen. Diese Vorlage beschreibt den konsolidierten Einzelträger `specification.md`; Strukturprinzipien und Frontmatter-Schema gelten bei einer Spaltung pro Datei. ^p0325

Anwendungsszenarien sind integriert. User Stories aus Anwender-Perspektive im Format „Als [Rolle], die …, will ich …, damit …" gehören seit der Konventionsänderung 2026-05-30 als eigene Sektion (Epics plus User Stories) in `specification.md`. Eine separate `user-stories.md` (siehe [Vorlage User Stories](#promptotyping-document-user-stories)) ist die dokumentierte Ausnahme für große Projekte (typischerweise Editionsprojekte), deren Substanz-Funktion ohnehin gespalten wird; in dem Fall gelten die Strukturprinzipien der Vorlage User Stories für die ausgelagerte Datei. ^p0326

#### Funktion des Dokuments

Das Dokument beantwortet vier verbundene Fragen am Stück: was soll das System leisten (Anforderungen), wer nutzt es wie und warum (Epics und User Stories), welche Features stellt es konkret bereit (Funktionsumfang), warum haben wir es so und nicht anders gebaut (Entscheidungen). Diese Fragen werden in einem Dokument geführt, weil ihre Antworten miteinander verzahnt sind: eine Story motiviert eine Anforderung, ein Feature implementiert sie, eine Entscheidung begründet, warum dieses Feature so umgesetzt ist und nicht anders. Wer die Schichten getrennt führt, läuft Gefahr, dass eine Änderung in einer Schicht die anderen unbemerkt veraltet. ^p0327

Adressiert sind drei Lesergruppen: ein Reviewer, der prüft, ob die Anforderungen umgesetzt sind; ein neuer Mitarbeiter, der den Funktionsumfang verstehen will; ein Coding-Agent, der eine Funktion erweitern oder eine Entscheidung respektieren soll. ^p0328

#### Strukturprinzipien

Drei Prinzipien tragen das Dokument. ^p0329

Erstens trennen die Sektionen nach Aktualisierungsrhythmus. Anforderungen sind statisch und werden selten umgeschrieben; sie halten fest, was ursprünglich gewollt war. Epics und User Stories teilen diesen langsamen Rhythmus; fortgeschrieben wird nur ihr Validierungsstatus (Hypothese → validiert). Funktionsumfang wird refaktoriert pro Release; er beschreibt die aktuelle Gestalt des Systems. Entscheidungen wachsen monoton; sie werden ergänzt, nie überschrieben. Diese Rhythmen können nur in einer Datei koexistieren, wenn sie als getrennte Sektionen geführt werden. ^p0330

Zweitens ist jede Entscheidung viergliedrig: Kontext, Wahl, Begründung, Effekt. Eine Entscheidung ohne Begründung ist eine Annahme; eine ohne Effekt-Beobachtung ist eine Behauptung. Das ADR-Format (Architecture Decision Record) ist die etablierte Form für diese Viergliedrigkeit; sie wird hier auf alle Decisions angewandt, nicht nur auf Architekturentscheidungen. ^p0331

Drittens werden Decisions nicht überschrieben. Wenn eine Entscheidung revidiert wird, bekommt sie einen neuen Eintrag, der auf die alte verweist. Die alte bleibt sichtbar, weil ihr Kontext und ihre Begründung weiterhin Teil der Projektgeschichte sind. Diese Regel teilt sich das Dokument mit dem Journal: beide tragen historische Stände, statt sie zu ersetzen. ^p0332

#### Frontmatter-Schema

Das Dokument folgt dem Frontmatter-Schema aus der [Konvention Promptotyping Documents](#konvention-v0.1) (Pflichtkern: `title, project, method, status, created, updated`). Spezifisch für Specification: ^p0333

- `topics:` typisch sind Verweise auf Requirements Engineering, Decision Records (oder ADR) und User Stories. Sie verorten den Agenten in den methodischen Wissensfeldern, die formale Anforderungen, Anwendungsszenarien und Entscheidungsdokumentation tragen. ^p0334
- `knowledge-sources:` selten genutzt; Specification trägt projekt-internes Wissen, nicht externe Anschlüsse. ^p0335
- `related:` typischerweise `project`, `data`, `architecture`, `design`; bei ausgelagerten Stories zusätzlich `user-stories`. Specification ist das Hub-Dokument der Substanz und referenziert in beide Richtungen. ^p0336

#### Abschnitte im Detail

##### Lead

Funktion: in zwei bis drei Sätzen den Charakter des Dokuments und seinen Aufbau benennen. Inhalt: Hinweis auf die Dreiteilung Anforderungen/Funktionsumfang/Entscheidungen, Erläuterung der unterschiedlichen Aktualisierungsrhythmen. Der Lead orientiert den Leser, der sonst zwischen den drei Schichten verloren geht. ^p0337

##### Anforderungen

Funktion: festhalten, was das System leisten soll und für wen. Inhalt: funktionale und nicht-funktionale Anforderungen in formaler Sprache, mit Akzeptanzkriterien soweit operationalisierbar, durchnummeriert (FR-NN, NFR-NN). Format pro Anforderung: ein Satz, der das Verhalten beschreibt, plus Akzeptanzkriterium. Nicht-funktionale Anforderungen (Barrierefreiheit, Performance, Datenschutz) werden separat ausgewiesen, gegebenenfalls als eigene Unterüberschrift. Diese Sektion wird selten umgeschrieben. ^p0338

Diese Sektion trägt formale Anforderungen, nicht narrative Szenarien. Anwendungsszenarien aus Forscherinnen- oder Anwender-Perspektive gehören in die Sektion Epics und User Stories desselben Dokuments. Der Grund für die getrennten Sektionen: Anforderungen sind formal-prüfbar (Reviewer-Sicht), Stories sind narrativ-anwendungsorientiert (Anwender-Sicht); beide gehören zur Substanz-Funktion, tragen aber unterschiedliche Sprachen und Adressaten. ^p0339

##### Epics und User Stories

Funktion: dokumentieren, wer das System wie und warum nutzt. Inhalt: Epics als thematische Bündel verwandter Szenarien (typischerweise drei bis fünf, etwa Zentrale Forschungsoperationen, Wissenschaftliche Absicherung, Begriffliche Orientierung), darunter die einzelnen Stories im Format „Als [Rolle], die [Kontext], will ich [Ziel], damit [Nutzen]." Jede Story führt ihren epistemischen Status (validiert durch wen und wann, oder Annahme mit Beobachtungspunkt „Effekt: to be observed" plus auflösendem Ereignis) und eine Ableitung als Verlinkung in die Wissensbasis: welche Anforderung (FR-NN), welche Komponente in `architecture.md` oder `design.md`, welche Begriffe aus `INDEX.md`. Die vollständigen Strukturprinzipien (Dreigliedrigkeit, Trennung Anwender- von System-Perspektive, Ableitungspflicht, epistemischer Status) stehen in der [Vorlage User Stories](#promptotyping-document-user-stories) und gelten für diese Sektion unverändert. Wird die Sektion bei großen Editionsprojekten als separate `user-stories.md` ausgelagert (dokumentierte Ausnahme), verbleibt hier ein Verweis. ^p0340

##### Funktionsumfang

Funktion: die aktuelle Gestalt des Systems beschreiben. Inhalt: pro Ansicht oder Modul Zweck, Datengrundlage, Interaktion, Grenzen, vier Felder, die jedes Feature in derselben Form vergleichbar machen. Reihenfolge der Features folgt der Anwendungslogik (Einstieg, Hauptansichten, Detailansichten, Sonderansichten), nicht alphabetisch. Diese Sektion wird pro Release refaktoriert. ^p0341

##### Entscheidungen

Funktion: die Designentscheidungen mit Kontext, Wahl, Begründung, Effekt festhalten. Inhalt: ADR-artige Einträge, monoton wachsend, neueste oben oder neueste unten; entscheidend ist Konsistenz innerhalb des Dokuments. Pro Eintrag eine Überschrift mit Identifier (`### ADR-007 Akzent-Farbe von Forest Green auf Academic Blue`) und vier Felder. Bei Revision wird ein neuer Eintrag mit Verweis angelegt; der alte bleibt stehen. ^p0342

Pro Entscheidung: ^p0343

- Kontext: was war die Ausgangslage, welche Spannung war zu lösen. ^p0344
- Wahl: was wurde entschieden, in einem Satz. ^p0345
- Begründung: warum diese Wahl und nicht eine andere. ^p0346
- Effekt: was wurde seitdem beobachtet. ^p0347

#### Was nicht reingehört

- Architekturdetails. Stack, Datenfluss, Modulgrenzen gehören in `architecture.md`. Specification kann auf eine Architekturentscheidung verweisen, beschreibt sie aber nicht selbst. ^p0348
- Designtokens, UI-Patterns. Wie etwas aussieht, gehört in `design.md`. ^p0349
- Datenmodell. Welche Entitäten und Relationen die Daten tragen, gehört in `data.md`. Specification beschreibt, was mit den Daten getan wird, nicht was sie sind. ^p0350
- Implementierungs-Details. Wie eine Funktion technisch realisiert ist, gehört in den Code; Specification beschreibt das Verhalten. ^p0351

#### Vorlage zum Befüllen

Der folgende Block ist als Template gedacht. ^p0352

````markdown
---
title: Specification
project:
  name: [Projektname]
  repository: [Repository-URL]
status: complete
language: [de | en]
version: [Repo-Schema-Version]
created: [YYYY-MM-DD]
updated: [YYYY-MM-DD]
authors: [Autor 1, Autor 2]
generated-with: [Harness (LLM), falls relevant]
method:
  name: Promptotyping
  url: https://lisa.gerda-henkel-stiftung.de/digitale_geschichte_pollin
template:
  name: Vorlage Specification
  version: 0.2
  url: https://dhcraft.org/Promptotyping/promptotyping-document/specification
  alias: https://dhcraft.org/Promptotyping/#promptotyping-document-specification
topics: ["[[Requirements Engineering]]", "[[Decision Records]]", "[[User Stories]]"]
related: [project, data, architecture, design]
---

<!-- Lead: zwei bis drei Sätze. Sektionen Anforderungen / Epics und User Stories / Funktionsumfang / Entscheidungen erwähnen, unterschiedliche Aktualisierungsrhythmen erklären. -->

[Lead-Absatz]

#### Anforderungen

<!-- Formale Anforderungen, statisch. Narrative Anwendungsszenarien gehören in die Sektion Epics und User Stories. -->

##### Funktionale Anforderungen

- FR-01: [Verhalten in einem Satz]. Akzeptanzkriterium: [...]
- FR-02: [...]

##### Nicht-funktionale Anforderungen

- NFR-01: [Anforderung]. Maßstab: [...]
- NFR-02: [...]

#### Epics und User Stories

<!-- Epics als thematische Bündel, darunter Stories. Pro Story: Dreigliedrigkeit, Validierungsstatus, Ableitung. Bei ausgelagerter user-stories.md (Ausnahme großer Editionsprojekte) hier nur Verweis. -->

##### [Epic 1: zum Beispiel Zentrale Forschungsoperationen]

###### [Story-Titel]

*Als [Rolle], die [Kontext], will ich [Ziel], damit [Nutzen].*

Validierung: [validiert durch Rolle/Person am YYYY-MM-DD | Annahme (Proxy: wer), Effekt: to be observed, Auflösung: Ereignis]

Ableitung:
- Anforderung FR-NN
- Komponente [[design#Komponente]] (oder [[architecture#Komponente]])
- Begriffe [[INDEX#Begriff A]], [[INDEX#Begriff B]]

##### [Epic 2: zum Beispiel Wissenschaftliche Absicherung]

###### [Story-Titel]

[...]

#### Funktionsumfang

<!-- Pro Ansicht oder Modul: Zweck, Datengrundlage, Interaktion, Grenzen. Reihenfolge folgt Anwendungslogik. -->

##### [Name der Ansicht]

Zweck. [Was leistet diese Ansicht.]

Datengrundlage. [Welche Daten werden gezeigt, mit Verweis auf data.md.]

Interaktion. [Wie agiert der Nutzer mit der Ansicht.]

Grenzen. [Was leistet sie nicht.]

##### [Name der nächsten Ansicht]

[...]

#### Entscheidungen

<!-- ADR-artig, monoton wachsend. Pro Eintrag: Kontext, Wahl, Begründung, Effekt. Bei Revision neuen Eintrag mit Verweis anlegen, alten stehen lassen. -->

##### ADR-NNN Titel der Entscheidung

Kontext. [Ausgangslage, Spannung.]

Wahl. [Was wurde entschieden.]

Begründung. [Warum diese Wahl.]

Effekt. [Was wurde seitdem beobachtet.]

##### ADR-NNN+1 Titel der nächsten Entscheidung

[...]
````

#### Anwendung als Prompt-Template

Strukturanker beim Aufsetzen der Substanz-Dokumentation. Anforderungen entstehen früh, typischerweise in der Preparation- und Exploration-Phase aus Scholar-Centered-Design-Sessions oder Requirements-Engineering. Funktionsumfang füllt sich iterativ während der Implementation. Entscheidungen werden in dem Moment eingetragen, in dem sie getroffen werden, nicht nachträglich rekonstruiert (siehe Glossar-Eintrag Critical-Expert-in-the-Loop). ^p0353

Review-Folie für eine bestehende Specification. Ein vorhandenes `specification.md` oder spezialisierte Träger wie `system-specification.md`, `feature-specification.md` und `architecture-decisions.md` werden gegen die Vorlage gehalten. Geprüft werden Sektionstrennung, viergliedrige Entscheidungen, nachvollziehbare Revisionen und die Abgrenzung zu Architektur- und Designdetails. ^p0354

#### Beispiel

HerData hat die früher getrennten Dateien `features.md` und `decisions.md` in eine konsolidierte `specification.md` überführt, mit Drift zwischen den Dateien als dokumentiertem Grund. Die Entscheidungs-Sektion arbeitet mit dem viergliedrigen Schema "Kontext, Wahl, Begründung, Effekt"; ein Beispiel ist die Akzent-Farbe-Entscheidung, die als ADR den Wechsel von Forest Green auf Academic Blue mit Konflikt-Begründung dokumentiert. HerData ist damit der Referenzfall der Konsolidierungs-Norm. ^p0355

sugw-Edition hat das frühere `requirements.md` ebenfalls in `specification.md` aufgehen lassen, führt aber die Anwendungsszenarien weiterhin als separate `knowledge/user-stories.md` mit Ableitung, der Referenzfall für die dokumentierte Ausnahme der ausgelagerten Story-Datei (siehe [Vorlage User Stories](#promptotyping-document-user-stories), Konventionsänderung 2026-05-30). Beide Beispiele gegen die Repos verifiziert am 2026-06-09. ^p0356

#### Begriffe

- Anforderung: festgehaltene Erwartung an das System in formaler, prüfbarer Sprache (FR-NN/NFR-NN) mit Akzeptanzkriterium; die narrative Anwender-Form ist die User Story in der Sektion Epics und User Stories. ^p0357
- Feature: konkrete Funktion oder Ansicht, die das System bereitstellt; setzt typischerweise eine oder mehrere Anforderungen um. ^p0358
- ADR: Architecture Decision Record, viergliedriges Format (Kontext, Wahl, Begründung, Effekt) für eine dokumentierte Designentscheidung. ^p0359
- Aktualisierungsrhythmus: die typische Häufigkeit, mit der eine Sektion eines Dokuments verändert wird; bei Specification unterscheiden sich die drei Sektionen erheblich. ^p0360

## Template `architecture.md`: Vorlage Architecture

Source file `_content/promptotyping-document/architecture.md`, template version 0.4. ^p0361


### Vorlage Architecture

Diese Vorlage strukturiert das Architecture-Dokument einer Promptotyping-Wissensbasis. Ein einzelner Träger heißt `architecture.md`; Spezialisierungen folgen `<subject>-architecture.md`. Das Dokument liegt im `knowledge/`-Ordner und trägt die technische Realisierung des Systems. ^p0362

#### Geltungsbereich

Die Vorlage trägt, sobald das System mehr als ein triviales Frontend ist, sobald also Pipeline-Stufen, Modulgrenzen, Datenflüsse oder Sicherheitsannahmen dokumentiert werden müssen. Bei einseitigen Static-Site-Repos ohne Build-Schritt entfällt sie; eine knappe Architektur-Sektion in `specification.md` reicht dann. Sie trägt nicht für Code-Dokumentation auf Funktions- oder Klassenebene; diese liegt im Code (Docstrings, Kommentare, JSDoc). ^p0363

Architektur bleibt im Regelfall ein Dokument. Eine Auslagerung entsteht, sobald ein Aspekt eine eigene Routing Question oder einen eigenen Aktualisierungszyklus entwickelt. Die Dateinamen folgen dann `<subject>-architecture.md`, etwa `pipeline-architecture.md`, `model-services-architecture.md` oder `deployment-architecture.md`. Strukturprinzipien und Frontmatter-Schema dieser Vorlage gelten pro Datei, und `INDEX.md` registriert jede Spezialisierung. ^p0364

#### Funktion des Dokuments

Das Dokument beantwortet "wie ist das System gebaut: welcher Stack, welche Komponenten, welcher Datenfluss, welche externen Modelle und Services, welche Sicherheits- und Barrierefreiheits-Maßnahmen". Adressiert sind drei Lesergruppen: ein neuer Entwickler, der den Code-Aufbau verstehen muss; ein Reviewer, der die Architekturentscheidungen prüft; ein Coding-Agent, der Komponenten erweitert oder umbaut. Im Promptotyping-Kontext ist die dritte Lesergruppe besonders bedeutsam: der Agent liest dieses Dokument, bevor er Code generiert, und seine Modulgrenz-Beschreibungen geben dem Agenten Halt bei der Implementation. Eine zu vage Architekturbeschreibung führt zu Code, der die intendierten Schichten ignoriert. ^p0365

#### Strukturprinzipien

Drei Prinzipien tragen das Dokument. ^p0366

Erstens trennt es Wie von Was und Aussehen. Welche Anforderungen das System erfüllt, gehört in `specification.md`. Wie die UI gestaltet ist, gehört in `design.md`. Wie es technisch realisiert ist, gehört hier hin. Diese Trennung verhindert, dass eine Architekturänderung auch eine Spec- und Design-Anpassung erzwingt. ^p0367

Zweitens beschreibt es Modulgrenzen, nicht Implementationen. Was eine Komponente leistet und woran sie aufhört, ist Architektur; wie sie intern arbeitet, ist Code. Eine Beschreibung, die in den Code hineingreift, veraltet schneller als sie nutzt. Im Promptotyping-Kontext ist die Modulgrenze die Stelle, an der der Coding-Agent Hilfe braucht; sie zu beschreiben heißt, dem Agenten zu sagen, wo er aufhören soll, weiterzubauen. ^p0368

Drittens trägt es Sicherheit und Barrierefreiheit als Hauptbestandteile, nicht als Anhang. Sicherheitsannahmen und Barrierefreiheits-Maßnahmen sind Architekturentscheidungen, nicht nachträgliche Compliance-Sektionen. Sie stehen im Hauptteil oder gar nicht. ^p0369

#### Frontmatter-Schema

Das Dokument folgt dem Frontmatter-Schema aus der [Konvention Promptotyping Documents](#konvention-v0.1) (Pflichtkern: `title, project, method, status, created, updated`). Spezifisch für Architecture: ^p0370

- `topics:` projektabhängig. Typisch sind Verweise auf Wissensfelder wie Software Architecture, Pipeline Design, Web Architecture, je nach Charakter des Systems. Bei ML- oder OCR-Pipelines zusätzlich Computer Vision oder NLP Pipelines. Topics werden so gewählt, dass der Agent bei Implementations-Reasoning die richtigen Architektur-Standards aktiviert. ^p0371
- `knowledge-sources:` sinnvoll, wenn das System auf institutionellen Plattformen (GAMS, eXist-db) oder etablierten Architekturmustern (REST, RDF-Triplestore, statische Generatoren) aufbaut. Standards wie WCAG für Barrierefreiheit oder OWASP für Sicherheit als URI hinterlegen. ^p0372
- `related:` typischerweise `data`, `specification`, `design`. ^p0373

#### Abschnitte im Detail

##### Lead

Funktion: in zwei bis drei Sätzen das Architekturmuster benennen. Inhalt: Charakter der Anwendung (statische Webanwendung, Pipeline mit Frontend, RDF-getriebenes System), die wesentliche Designentscheidung im Sinne von "bewusst schlicht/komplex/redundant gehalten weil…", Verweis auf andere Dokumente, in denen das Was und das Aussehen liegen. ^p0374

##### Stack

Funktion: die eingesetzten Technologien benennen und begründen. Inhalt: Sprachen, Frameworks, Build-Tooling, Plattformen. Pro Wahl ein Begründungssatz, soweit nicht trivial, etwa "Vanilla JavaScript ohne Framework, weil das Projekt ein Forschungsfrontend ist und Pflegeaufwand minimiert werden soll". Versionsangaben sparsam: Major-Version reicht, Minor-Versionen sind im `package.json` oder `requirements.txt`. ^p0375

##### Komponenten

Funktion: die Hauptmodule und ihre Verantwortung. Inhalt: pro Komponente Zweck, Schnittstelle, Modulgrenze. Eine kurze Liste oder Tabelle ist meist klarer als ein ausgreifender Prosatext. Komponenten werden so granular benannt, dass ein Entwickler weiß, welche Datei oder welcher Ordner gemeint ist. ^p0376

##### Datenfluss

Funktion: zeigen, wie Daten von Quelle zu Anzeige fließen. Inhalt: Pipeline-Stufen mit klaren Übergängen, etwa "XML-Quellen → Python-Pipeline → JSON-Export → JavaScript-Frontend". Pro Stufe werden Output-Format und Validierungsstelle dokumentiert. Bei eigenständiger Routing Question und eigenem Pflegezyklus wird diese Sektion zu `pipeline-architecture.md`. ^p0377

##### Externe Modelle und Services

Funktion: alle externen Verarbeitungs-Ressourcen dokumentieren, die das System nutzt. Inhalt: pro Modell oder Service Rolle in der Pipeline, Provider, Endpunkt-Format, Authentifizierung, Limits und Output-Form. Bei eigenständigem Pflegezyklus entsteht `model-services-architecture.md`. ^p0378

##### Sicherheit

Funktion: Sicherheitsannahmen und -maßnahmen offenlegen. Inhalt: was schützt das System wovor (Input-Sanitization, Authentifizierung, Datenminimierung), welche Annahmen liegen zugrunde (statische Site ohne Backend hat keine Server-Side-Angriffsfläche), welche Risiken bleiben akzeptiert. Eine Sicherheitssektion ohne Risikoannahme ist eine Sicherheitsbehauptung. ^p0379

##### Barrierefreiheit

Funktion: WCAG-Konformität und Maßnahmen dokumentieren. Inhalt: angestrebte WCAG-Stufe (typischerweise AA), eingesetzte Maßnahmen (semantisches HTML, ARIA-Attribute, Tastaturbedienung, Kontrastwerte, Screenreader-Tests), bekannte Lücken. Verweis auf Audit-Tools und -Berichte falls vorhanden. ^p0380

##### Repository-Struktur

Funktion: Top-Level-Ordner mit Funktionszuweisung erklären. Inhalt: Tabelle oder Liste der Hauptordner mit einem Satz pro Ordner. Reihenfolge folgt der Datenflusslogik, nicht alphabetisch. ^p0381

##### Build und Deployment

Funktion: den Weg vom Repo zur laufenden Anwendung dokumentieren. Inhalt: lokale Entwicklungsumgebung, Build-Schritt, Deployment-Ziel, CI/CD-Konfiguration. Verweis auf die konkreten Workflow-Dateien (`.github/workflows/`, `pyproject.toml`) als Source of Truth. ^p0382

#### Was nicht reingehört

- User-Anforderungen. Welche Funktionalität das System leistet, gehört in `specification.md`. ^p0383
- Designtokens, UI-Patterns. Wie das System aussieht, gehört in `design.md`. ^p0384
- Code-Implementation. Wie eine Komponente intern arbeitet, gehört in den Code (Docstrings, Kommentare). ^p0385
- Testfälle. Konkrete Testsuites werden im Code dokumentiert; Architecture nennt nur die Test-Strategie als ein bis zwei Sätze. ^p0386

#### Vorlage zum Befüllen

Der folgende Block ist als Template gedacht. ^p0387

````markdown
---
title: Architektur
project:
  name: [Projektname]
  repository: [Repository-URL]
status: complete
language: [de | en]
version: [Repo-Schema-Version]
created: [YYYY-MM-DD]
updated: [YYYY-MM-DD]
authors: [Autor 1, Autor 2]
generated-with: [Harness (LLM), falls relevant]
method:
  name: Promptotyping
  url: https://lisa.gerda-henkel-stiftung.de/digitale_geschichte_pollin
template:
  name: Vorlage Architecture
  version: 0.4
  url: https://dhcraft.org/Promptotyping/promptotyping-document/architecture
  alias: https://dhcraft.org/Promptotyping/#promptotyping-document-architecture
topics: ["[[Software Architecture]]"]  # bei Pipeline-Projekten zusätzlich [[Pipeline Design]]
knowledge-sources:
  standards:
    [Standard, etwa WCAG]: [URI]
related: [data, specification, design]
---

<!-- Lead: zwei bis drei Sätze. Architekturmuster benennen, wesentliche Designentscheidung andeuten, Verweis auf was und aussehen. -->

[Lead-Absatz]

#### Stack

<!-- Sprachen, Frameworks, Build-Tooling. Pro Wahl ein Begründungssatz. -->

[...]

#### Komponenten

<!-- Hauptmodule mit Zweck, Schnittstelle, Modulgrenze. Tabelle oft klarer als Prosa. -->

| Komponente | Zweck | Schnittstelle |
|---|---|---|
| [Komponente] | [Zweck] | [Schnittstelle] |

#### Datenfluss

<!-- Pipeline-Stufen mit Übergängen und Validierungspunkten. Bei eigener Routing Question und eigenem Pflegezyklus als pipeline-architecture.md auslagern. -->

[...]

#### Externe Modelle und Services

<!-- Optional. OCR-Modelle, LLM-Endpunkte, NER-Tools, Embeddings, Geocoding. Bei eigenem Pflegezyklus als model-services-architecture.md auslagern. -->

| Modell/Service | Rolle | Provider | Endpunkt |
|---|---|---|---|
| [Modell] | [Rolle in der Pipeline] | [Provider] | [Endpunkt-Format] |

#### Sicherheit

<!-- Annahmen, Maßnahmen, akzeptierte Risiken. Keine reine Behauptung. -->

[...]

#### Barrierefreiheit

<!-- WCAG-Stufe, Maßnahmen, bekannte Lücken. -->

[...]

#### Repository-Struktur

<!-- Top-Level-Ordner mit Funktionszuweisung. -->

| Ordner | Funktion |
|---|---|
| `[ordner/]` | [Funktion] |

#### Build und Deployment

<!-- Lokale Entwicklung, Build, Deployment-Ziel. Verweis auf Workflow-Dateien. -->

[...]
````

#### Anwendung als Prompt-Template

Strukturanker beim Aufsetzen der Architektur. Der Agent erhält den Template-Block und befüllt ihn aus dem real existierenden Code-Aufbau, dem `package.json` oder `requirements.txt`, der CI/CD-Konfiguration und den Build-Skripten. Sicherheits- und Barrierefreiheits-Sektionen verlangen Domänenwissen und sollten gegebenenfalls vom Critical Expert verifiziert werden. ^p0388

Review-Folie für eine bestehende Architektur. Ein vorhandenes `architecture.md` wird gegen die Vorlage gehalten, um zu prüfen, ob alle Sektionen tragen, ob die Modulgrenzen sauber sind, ob Sicherheit und Barrierefreiheit als Hauptbestandteile geführt werden und nicht als Anhang, und ob keine Code-Implementation hineingewachsen ist. ^p0389

#### Beispiel

Monolithischer Fall: HerData führt `architecture.md` mit den Sektionen Stack, Komponenten, Datenfluss, Sicherheit, Barrierefreiheit, Repository-Struktur, Build und Deployment. Charakteristisch ist die Lead-Begründung: "HerData ist eine statische Web-Anwendung mit einer Python-Pipeline für die Datenaufbereitung und einem Vanilla-JavaScript-Frontend ohne Framework. Diese Schlichtheit ist bewusst gewählt: sie reduziert Pflegeaufwand, Lade-Komplexität und Fehlerrisiken auf das Minimum, das ein Forschungs-Frontend braucht." Der Lead trägt die wesentliche Architekturentscheidung (bewusste Schlichtheit) und ihre Begründung in zwei Sätzen. ^p0390

Beispiel-Frontmatter aus HerData/`architecture.md`: ^p0391

```yaml
---
title: Architektur
project:
  name: HerData
  repository: https://github.com/chpollin/HerData
status: complete
language: de
version: 0.2
tags: [template, promptotyping, vault-operations]
created: 2026-05-05
updated: 2026-05-09
authors: [Christopher Pollin]
generated-with: Claude Code mit Claude Opus 4.7
method:
  name: Promptotyping
  url: https://lisa.gerda-henkel-stiftung.de/digitale_geschichte_pollin
knowledge-sources:
  institutions:
    Goethe- und Schiller-Archiv: https://www.klassik-stiftung.de/goethe-und-schiller-archiv/
    PROPYLÄEN: https://goethe-biographica.de
related: [data, design, features, maintenance]
---
```

Gespaltener Fall: zbz-ocr-tei führt die Bauweise-Funktion in drei Dokumenten: `PIPELINE.md` (7-stufige OCR-zu-TEI-Pipeline mit Skripten, Input- und Output-Pfaden, Stage-Status), `INFRASTRUKTUR.md` (Azure-API-Zugang, Podman-Container, GitLab-CI, ZBZ-Deployment), `ENGINES.md` (Mistral Document AI, DeepSeek, Gemini, Docling als OCR- und Layout-Engines mit Endpunkten und Limits). Diese Spaltung ist die Praxisform des Geltungsbereich-Hinweises oben: bei mehrstufigen ML-Pipelines mit mehreren externen Modellen reicht eine Datei nicht, weil die einzelnen Aspekte je eigenen Aktualisierungsrhythmus tragen. ^p0392

#### Begriffe

- Stack: die Gesamtheit der eingesetzten Technologien (Sprachen, Frameworks, Plattformen, Tooling). ^p0393
- Modulgrenze: die Schnittstelle, an der eine Komponente endet und eine andere beginnt; die zentrale Information einer Architekturbeschreibung. ^p0394
- Datenfluss: der Weg, den Daten von der Quelle bis zur Anzeige durchlaufen, mit Formaten und Validierungspunkten an jedem Übergang. ^p0395

#### Related

- [Vorlage Specification](#promptotyping-document-specification) ^p0396
- [Vorlage Datengrundlage](#promptotyping-document-data) ^p0397
- [Vorlage Design](#promptotyping-document-design) ^p0398
- [Konvention Promptotyping Documents](#konvention-v0.1) ^p0399

## Template `technology.md`: Vorlage Technology

Source file `_content/promptotyping-document/technology.md`, template version 0.1. ^p0400


### Vorlage Technology

Diese Vorlage strukturiert ein Technology-Baseline-Dokument, das projektübergreifende Technologie-Entscheidungen für eine Artefaktfamilie trägt und begründet. Das resultierende Dokument heißt typischerweise `technology-baseline.md` und wird zentral publiziert, sodass Projektinstanzen per URL darauf verweisen; die `architecture.md` einer Instanz dokumentiert dann nur den projektspezifischen Stack und die Abweichungen von der Baseline. Der erste Absatz des resultierenden Dokuments trägt den Zweck in einem Satz. ^p0401

Die Vorlage unterscheidet sich von den übrigen Vorlagen des Katalogs in einem Punkt. Die anderen Vorlagen strukturieren Dokumente, deren Inhalt pro Projekt neu entsteht; ein Baseline-Dokument trägt wiederverwendbaren Inhalt, der für alle Projekte derselben Artefaktfamilie gilt. Es wird deshalb selten geschrieben und oft referenziert. ^p0402

#### Geltungsbereich

Die Funktion trägt, sobald mehrere Projekte denselben Artefakttyp bauen und die Stack-Begründung wiederverwendbar ist. Triggerkriterium: Es existiert eine Menge von Technologie-Regeln (Sprachwahl, Abhängigkeits-Politik, Hosting-Form, Sicherheits- und Nachhaltigkeits-Anforderungen), die ein Fachverantwortlicher für eine ganze Artefaktfamilie vertritt und die man kennen muss, um ein einzelnes Artefakt dieser Familie zu bewerten oder zu regenerieren. Der Leitfall ist das selbstständige statische Web-Tool; weitere Familien (Datenpipeline, TEI-Editions-Toolchain) können eigene Baselines tragen. ^p0403

Die Funktion trägt nicht für die Architektur eines einzelnen Projekts; die gehört in `architecture.md` ([Vorlage Architecture](#promptotyping-document-architecture)). Sie trägt nicht für imperative Agenten-Anweisung; die gehört in den Action-Layer ([Vorlage Action-Layer](#promptotyping-document-action-layer)), der auf die Baseline verweisen kann. Ein Einzelprojekt ohne Familienzusammenhang braucht keine Baseline; dort genügt die Begründung in der eigenen `architecture.md`. ^p0404

#### Funktion des Dokuments

Das Dokument beantwortet, mit welchen Technologien Artefakte einer Familie gebaut werden und warum diese Regeln so lauten. Adressiert sind drei Lesergruppen. Ein Forschender oder Reviewer prüft, ob die Technologiewahl eines Projekts begründet ist, ohne die Begründung in jedem Repo suchen zu müssen. Ein Coding-Agent liest die Baseline als Vorgabe, bevor er ein Artefakt der Familie generiert oder regeneriert; die Regeln sind für ihn direkte Constraints. Der Methodenverantwortliche pflegt die Regeln an einer Stelle statt in jedem Repo. ^p0405

Der Dokumenttyp ist Action. Die Zuordnung folgt der Diagnosefrage der Typologie, welcher Dokumenttyp nachzuziehen ist, wenn der Output nicht stimmt. Generiert ein Agent ein Artefakt der Familie mit einem Build-Schritt und einer npm-Abhängigkeit, ist der Output formal falsch, und nachzuziehen ist die Baseline. Die Baseline steht damit neben Action-Layer und Teststrategie und unterscheidet sich von beiden durch ihren Geltungsbereich, sie gilt für eine Artefaktfamilie statt für ein Projekt. ^p0406

Der Grund, warum die Zuordnung nicht offensichtlich ist, liegt in der Form. Die Baseline formuliert Regeln mit Begründung und nicht Anweisungen im Imperativ, was sie oberflächlich wie ein deklaratives Dokument aussehen lässt. Maßgeblich ist aber, dass ihre Sätze das Bauen binden und nicht einen Sachverhalt des Projekts beschreiben. ^p0407

#### Strukturprinzipien

Drei Prinzipien tragen das Dokument. ^p0408

Erstens trägt jede Regel ihre Begründung. Eine Technologie-Vorgabe ohne Begründung ist eine Geschmacksentscheidung; die Baseline bindet jede Regel an ein prüfbares Argument (Generierbarkeit, Haltbarkeit, Sicherheit, Ressourcenlage) und, wo vorhanden, an eine externe Quelle. ^p0409

Zweitens regelt es den Abweichungsfall mit. Eine Baseline, von der nicht abgewichen werden darf, ist ein Dogma; eine, von der stillschweigend abgewichen wird, ist wirkungslos. Die Baseline legt fest, dass Abweichungen in der `architecture.md` der Instanz mit Begründung dokumentiert werden, und macht die undokumentierte Abweichung zum Review-Befund. ^p0410

Drittens benennt es die Grenzen der Artefaktfamilie. Wo das Format endet (Datenvolumen, Persistenz, Kollaboration), steht in der Baseline, samt dem Übergabepunkt an die nächste Zuständigkeit; das schützt vor der schleichenden Ausweitung eines Prototyps in Software mit Wartungspflichten. ^p0411

#### Frontmatter-Schema

Das Dokument folgt dem reduzierten Frontmatter-Pflichtkern aus der [Konvention Promptotyping Documents](#konvention-v0.1); `title`, `status`, `created`, `updated`. Da die Baseline projektübergreifend gilt, entfällt der `project:`-Block oder benennt das tragende Methodik-Repo. Empfohlen sind `language`, `version`, `authors` beziehungsweise `generated-with` und `machine-url`, weil die Baseline gerade für maschinelle Abrufung gebaut ist. `authors` trägt ausschließlich Menschen, auch wenn ein LLM den Text erzeugt hat; `generated-with` nennt Harness und LLM im Format `Harness (LLM)`, etwa `Claude Code (Claude Opus 5)`. Siehe Sektion *Provenienz im Frontmatter* der Konvention. ^p0412

#### Abschnitte im Detail

`## Warum diese Form` (Pflicht). Funktion: die Grundentscheidung für die Artefaktfamilie begründen. Inhalt: die Eigenschaften, die den Default motivieren, mit externen Quellen, wo der Fachdiskurs sie liefert. ^p0413

`## Die Regeln` (Kern). Funktion: die operativen Vorgaben festlegen. Inhalt: pro Regel eine eigene Untersektion mit der Vorgabe und ihrer Begründung; wo eine Regel Ausnahmen kennt, stehen die Ausnahmekriterien explizit dabei (Muster Kompromissregel mit benannten Kriterien). Konkrete gelebte Beispiele aus realen Repos stützen die Regel. ^p0414

`## Nachhaltigkeit` (empfohlen). Funktion: die Baseline gegen die externen Standards des Feldes stellen. Inhalt: Messung gegen die einschlägigen Prinzipienkataloge, ehrlich auch dort, wo der Artefakttyp im Default durchfällt, mit dem Weg, die Lücke zu schließen. ^p0415

`## Grenzen und Übergabepunkt` (Pflicht). Funktion: das Ende der Artefaktfamilie markieren. Inhalt: die harten Grenzen des Formats und die Zuständigkeit, die jenseits davon trägt. ^p0416

`## Anwendung in einer Projektinstanz` (Pflicht). Funktion: den Referenz- und Abweichungsmechanismus festlegen. Inhalt: wie `architecture.md` und Action-Layer auf die Baseline verweisen (Maschinenadresse), was die Instanz selbst führen muss und wie Abweichungen dokumentiert werden. ^p0417

`## Quellen` (Pflicht, wo externe Quellen tragen). Funktion: die zitierten Standards und Diskursbeiträge nachweisen. Inhalt: Referenzen mit Autor, Jahr, Titel, DOI oder URL. ^p0418

#### Was nicht reingehört

- Projektspezifischer Stack und Modulstruktur; das gehört in die `architecture.md` der Instanz. ^p0419
- Projektspezifische Anweisung an den Agenten; das ist Action-Layer. Beide Dokumente sind Action-Dokumente, und die Grenze läuft über den Geltungsbereich. Was für jedes Artefakt der Familie gilt, steht in der Baseline; was nur in diesem Repo gilt, steht im Action-Layer. ^p0420
- Designsystem und visuelle Vorgaben; die gehören in `design.md` ([Vorlage Design](#promptotyping-document-design)) beziehungsweise ein zentrales Designsystem-Dokument. ^p0421
- Fachmethodische Regelwerke; die gehören ins Domänenwissen ([Vorlage Domänenwissen](#promptotyping-document-domain-knowledge)). ^p0422

#### Vorlage zum Befüllen

````markdown
---
title: Technology Baseline. [Artefaktfamilie]
status: draft
language: [de | en]
version: 0.1
created: [YYYY-MM-DD]
updated: [YYYY-MM-DD]
authors: [Autor]
generated-with: [Harness (LLM), falls relevant]
machine-url: [statische URL dieses Dokuments]
---

### Technology Baseline. [Artefaktfamilie]

[Zweck-Satz. Für welche Artefaktfamilie die Baseline gilt und wie Instanzen auf sie verweisen.]

#### Warum diese Form

[Eigenschaften, die den Default motivieren, mit Quellen.]

#### Die Regeln

##### [Regel]

[Vorgabe und Begründung. Ausnahmekriterien explizit, gelebte Beispiele aus realen Repos.]

#### Nachhaltigkeit

[Messung gegen die einschlägigen Prinzipienkataloge, samt Lücken und Schließungsweg.]

#### Grenzen und Übergabepunkt

[Harte Grenzen des Formats; Zuständigkeit jenseits davon.]

#### Anwendung in einer Projektinstanz

[Referenzmechanismus, Pflichten der Instanz, Abweichungsdokumentation.]

#### Quellen

[Autor, Jahr, Titel, DOI/URL.]
````

#### Anwendung als Prompt-Template

Strukturanker beim Aufschreiben einer Baseline. Der Agent erhält den Template-Block und befüllt ihn aus dem, was die Repositorien der Familie faktisch tun, also aus den Stacks, den Abhängigkeitslisten, der Hosting-Form und den vorhandenen `architecture.md`-Dokumenten. Der entscheidende Arbeitsschritt liegt danach und ist nicht delegierbar. Eine Regel, die der Agent aus dem Bestand abliest, ist eine Beobachtung; zur Regel wird sie erst, wenn der Fachverantwortliche sie vertritt. Die Begründungen verlangen deshalb Verifikation durch den Critical Expert, und die Abweichungskriterien ebenso, weil sie festlegen, wann ein Projekt vom Default abrücken darf. ^p0423

Vorgabe an den bauenden Agenten. Die Baseline wird über ihre Maschinenadresse in den Kontext geladen, bevor ein Artefakt der Familie generiert oder regeneriert wird; ihre Regeln sind für den Lauf Constraints. Verweist der Action-Layer eines Projekts auf die Baseline, genügt dort die Adresse und die Nennung der Abweichungen. ^p0424

Review-Folie für ein bestehendes Artefakt. Ein ausgeliefertes Artefakt wird gegen die Baseline gehalten, Regel für Regel. Jede Abweichung, die in der `architecture.md` der Instanz nicht mit Begründung steht, ist ein Review-Befund; das ist die Prüfform, die das zweite Strukturprinzip einlöst. ^p0425

#### Beispiel

Das Methodik-Repo führt `_content/technology-baseline.md` als Baseline für die Familie der selbstständigen statischen Web-Tools; Warum-Sektion mit Minimal Computing und Endings-Prinzipien, sieben Regeln einschließlich der Kompromissregel mit vier Kriterien, FAIR4RS-Messung mit dem Findability-Befund, Grenzen mit RSE-Übergabepunkt und der Anwendungsmechanismus über die Maschinenadresse. ^p0426

#### Begriffe

- Technology Baseline: projektübergreifendes Knowledge Document, das Technologie-Regeln und ihre Begründung für eine Artefaktfamilie trägt und von Projektinstanzen referenziert wird. ^p0427
- Artefaktfamilie: Menge von Forschungsartefakten mit gleicher technischer Grundform (statisches Web-Tool, Datenpipeline), für die dieselben Technologie-Regeln gelten. ^p0428
- Abweichungsdokumentation: Pflicht der Projektinstanz, jede Abweichung von der Baseline in der eigenen `architecture.md` mit Begründung zu führen. ^p0429

#### Versionshistorie

- 0.1 (2026-07-26): Aufnahme in den Vorlagen-Katalog. Empirisch aus der Technology Baseline des Methodik-Repos entstanden (Erstentwurf 2026-07-23). Der Dokumenttyp ist bei der Aufnahme von Declarative auf Action korrigiert, weil der kanonische Papertext die Technology Baseline in Abschnitt 3.3 unter den Action Documents führt und die Diagnosefrage der Typologie zum selben Ergebnis kommt. Die Vorlage ist im Repo kanonisch und hat kein Vault-Original. ^p0430

#### Related

- [Konvention Promptotyping Documents](#konvention-v0.1) ^p0431
- [Vorlage Architecture](#promptotyping-document-architecture) ^p0432
- [Vorlage Action-Layer](#promptotyping-document-action-layer) ^p0433
- [Vorlage Design](#promptotyping-document-design) ^p0434

## Template `design.md`: Vorlage Design

Source file `_content/promptotyping-document/design.md`, template version 0.2. ^p0435


### Vorlage Design

Diese Vorlage strukturiert das Gestalt-Dokument einer Promptotyping-Wissensbasis. Das resultierende Dokument heißt typischerweise `design.md` und liegt im `knowledge/`-Ordner des Repos. Es ist deklaratives Knowledge; es beschreibt Designhaltung, Designsystem, Interaktionsmuster und Visualisierungslogik. Die Sozialisierung des Coding-Agenten auf der ästhetischen Schicht (siehe Glossar, [Agent-Sozialisierung](#glossar)) entsteht durch Komposition: `CLAUDE.md` (im Repo-Root, Action) verweist auf `design.md` als Wertequelle. Das Knowledge bleibt deklarativ, der Action-Layer übersetzt es in Imperative. ^p0436

#### Geltungsbereich

Die Vorlage trägt, sobald das Projekt eine UI hat, also visuelle Oberflächen, mit denen ein Mensch interagiert. Bei reinen Pipeline-, Datenmodell- oder Bibliotheks-Repos entfällt sie. Sie trägt nicht für reine Style-Guides oder Designsystem-Spezifikationen ohne Projektbezug; diese sind eigene Artefakte. ^p0437

#### Funktion des Dokuments

Das Dokument dokumentiert Gestaltungsentscheidungen für menschliche Leser: welche Designhaltung trägt das Projekt, welches Designsystem ist eingesetzt, welche Interaktionsmuster gelten, welche Visualisierungslogik gilt. Adressiert sind drei Lesergruppen: ein Reviewer, der die Designhaltung prüft; ein UX-Designer, der gegen die Designhaltung weiterarbeitet; ein Coding-Agent, der vor UI-Generierung das Dokument liest, um die Werteskala des Projekts zu kennen. ^p0438

Die Sozialisierung des Agenten auf der ästhetischen Schicht (Agent-Sozialisierung) ist kein eigenständiger Bestandteil des Designdokuments, sondern ein Kompositions-Effekt: `CLAUDE.md` im Repo-Root verweist auf `design.md` und führt eine Sektion mit imperativ formulierten Designprinzipien, die aus der Designhaltung abgeleitet sind. Das Designdokument bleibt deklarativ, der Action-Layer übersetzt es in Imperative. Diese Aufgabenteilung verhindert, dass ein Knowledge-Dokument seinen analytischen Typ wechselt. ^p0439

#### Strukturprinzipien

Drei Prinzipien tragen das Dokument. ^p0440

Erstens trennt es Gestalt von Bauweise und Substanz. Wie etwas aussieht, ist nicht wie es technisch realisiert ist (`architecture.md`) und nicht was es leisten soll (`specification.md`). Eine Vermischung lässt jede UI-Änderung in alle drei Dokumente einsickern. ^p0441

Zweitens verweist es auf den Code als Source of Truth, statt Token-Werte zu kopieren. Konkrete Hex-Werte, Schriftgrößen, Spacing-Tokens stehen in der Token-Datei (typischerweise `tokens.css` oder ähnlich). Das Dokument beschreibt das System, nicht die Werte; sonst veraltet es bei jedem Token-Refactor. ^p0442

Drittens bleibt es deklarativ. Designhaltung, Tokens-Kategorien, Interaktionsmuster werden beschrieben, nicht als Imperative an den Agenten formuliert. Die imperative Übersetzung passiert im Action-Layer (`CLAUDE.md` im Repo-Root), der auf dieses Dokument als Wertequelle verweist. Wer Imperativ-Sätze in das Designdokument schreibt, verletzt die Knowledge/Action-Trennung. ^p0443

#### Frontmatter-Schema

Das Dokument folgt dem Frontmatter-Schema aus der [Konvention Promptotyping Documents](#konvention-v0.1) (Pflichtkern: `title, project, method, status, created, updated`). Spezifisch für Design: ^p0444

- `topics:` typisch sind Information Visualisation und Scholar-Centered Design. Sie verorten den Agenten in den Wissensfeldern, die ihm bei UI-Generierung Halt geben: Tufte, Munzner, Bertin als Hintergrund statt generische UI-Patterns. Bei nicht-visualisierungslastigen Frontends statt Information Visualisation ein anderes UX-Wissensfeld wie Interaction Design. ^p0445
- `knowledge-sources:` selten genutzt, weil Designentscheidungen meist projekt-intern getroffen werden. Wenn ein etabliertes Designsystem (Material, Carbon, IBM Design Language) als Bezug dient, wird es hier als URI hinterlegt. ^p0446
- `related:` typischerweise `specification`, `architecture`. ^p0447

#### Abschnitte im Detail

##### Lead

Funktion: in zwei bis drei Sätzen die Designhaltung benennen. Inhalt: Charakter der Anwendung (Forschungswerkzeug, didaktische Edition, explorative Datenansicht), wessen Tradition sie nahesteht, wovon sie sich abgrenzt. Der Lead trägt die Designentscheidung in einem Satz; alle weiteren Sektionen entfalten sie. ^p0448

##### Designhaltung

Funktion: das ästhetische Wertesystem explizit machen. Inhalt: drei bis fünf Sätze über die grundlegende Haltung, etwa "das Interface positioniert sich als Forschungswerkzeug, nicht als Dashboard. Datenqualität wird nicht kaschiert; Lücken stehen so da, wie sie im Bestand sind". Diese Sektion ist später die Quelle, aus der die Action-Prinzipien für den Agenten abgeleitet werden. ^p0449

##### Designsystem

Funktion: die strukturellen Bestandteile benennen. Inhalt: Tokens (Farben, Typografie, Spacing) als Kategorien mit Verweis auf die Token-Datei im Repo, nicht als Wertetabelle. Komponenten (Cards, Buttons, Filter) als Kategorien mit Verweis auf den Komponentenordner. Layoutprinzipien (Grid, Container, responsive Breakpoints) in Prosa. ^p0450

##### Interaktionsmuster

Funktion: das Verhalten der Anwendung beschreiben. Inhalt: wie funktionieren Filter, Navigation, Profile, Detailansichten. Beschreibt die Logik der Interaktion, nicht die Implementation, etwa "Filter wirken kumulativ, der gefilterte Zustand wird durch Akzent-Färbung der Stat-Cards sichtbar", nicht "in `applyFilters()` wird die Klasse `is-filtered` gesetzt". ^p0451

##### Visualisierungslogik

Funktion: bei Datenvisualisierungen die methodische Wahl dokumentieren. Inhalt: welche Diagrammtypen für welche Forschungsfrage, welche bewusst ausgeschlossen wurden, wie mit Datenunsicherheit visuell umgegangen wird (Coverage-Anker, Provenance-Marker, Lücken-Darstellung). Diese Sektion entfällt, wenn das Projekt keine wesentlichen Datenvisualisierungen trägt. ^p0452

##### Anbindung an den Action-Layer

Funktion: dokumentieren, dass und wie `CLAUDE.md` (im Repo-Root) auf dieses Dokument verweist. Inhalt: ein knapper Hinweis, dass die imperative Übersetzung der Designhaltung in der `CLAUDE.md` liegt, typischerweise als Sektion "Designprinzipien" mit drei bis acht imperativ formulierten Sätzen, die aus der Designhaltung abgeleitet sind. Beispielhaft: aus dem Satz "Datenqualität wird nicht kaschiert" wird in CLAUDE.md "Lücken in den Daten werden visuell markiert, nicht ausgeblendet". Das Designdokument selbst trägt keine Imperative; es liefert die Wertequelle, aus der der Action-Layer schöpft. ^p0453

#### Was nicht reingehört

- Konkrete Token-Werte (Hex-Farben, Pixel-Größen, Schriftnamen). Diese liegen in der Token-Datei im Code. ^p0454
- Komponenten-Implementation. Wie eine Komponente technisch gebaut ist, liegt im Code. ^p0455
- Anforderungen oder Features. Was die Anwendung leistet, gehört in `specification.md`. ^p0456
- Stack-Wahl. Vanilla JS vs. Framework ist Architektur, nicht Design. ^p0457

#### Vorlage zum Befüllen

Der folgende Block ist als Template gedacht. ^p0458

````markdown
---
title: Gestaltung
project:
  name: [Projektname]
  repository: [Repository-URL]
status: complete
language: [de | en]
version: [Repo-Schema-Version]
created: [YYYY-MM-DD]
updated: [YYYY-MM-DD]
authors: [Autor 1, Autor 2]
generated-with: [Harness (LLM), falls relevant]
method:
  name: Promptotyping
  url: https://lisa.gerda-henkel-stiftung.de/digitale_geschichte_pollin
template:
  name: Vorlage Design
  version: 0.1
  url: https://dhcraft.org/Promptotyping/promptotyping-document/design
  alias: https://dhcraft.org/Promptotyping/#promptotyping-document-design
topics: ["[[Information Visualisation]]", "[[Scholar-Centered Design]]"]
related: [specification, architecture]
---

<!-- Lead: zwei bis drei Sätze. Designhaltung in einem Satz, Charakter der Anwendung. -->

[Lead-Absatz]

#### Designhaltung

<!-- Drei bis fünf Sätze über das ästhetische Wertesystem. Quelle für die Agent-Prinzipien weiter unten. -->

[...]

#### Designsystem

<!-- Tokens, Komponenten, Layout als Kategorien mit Verweis auf Code als Source of Truth. Keine Werte hier. -->

Tokens. [Beschreibung der Token-Kategorien, Verweis auf Token-Datei.]

Komponenten. [Beschreibung der Komponenten-Kategorien, Verweis auf Komponentenordner.]

Layout. [Grid, Container, responsive Breakpoints in Prosa.]

#### Interaktionsmuster

<!-- Verhalten der Anwendung, nicht Implementation. Filter, Navigation, Profile, Detailansichten. -->

[...]

#### Visualisierungslogik

<!-- Optional. Bei Datenvisualisierungen: methodische Wahl, Umgang mit Unsicherheit. -->

[...]

#### Anbindung an den Action-Layer

<!-- Knapper Hinweis: CLAUDE.md im Repo-Root verweist auf dieses Dokument und führt die imperative Übersetzung als "Designprinzipien"-Sektion. Beispielhaft, was dort stehen würde. -->

Die imperative Übersetzung der oben beschriebenen Designhaltung lebt im Action-Layer (`../CLAUDE.md`, Sektion "Designprinzipien"). Beispielhafte Imperative, abgeleitet aus der Designhaltung:

- [Imperativ-Satz, abgeleitet aus Designhaltung]
- [Imperativ-Satz, abgeleitet aus Designsystem]

Diese Imperative gehören in `CLAUDE.md`, nicht in dieses Dokument. Hier stehen sie nur als Beispiel-Hinweis.
````

#### Anwendung als Prompt-Template

Strukturanker beim Aufsetzen des Designsystems. Der Agent erhält den Template-Block und füllt zuerst Designhaltung und Designsystem aus, weil die imperative Übersetzung im Action-Layer (`CLAUDE.md`) aus diesen abgeleitet wird. Die Imperative entstehen typischerweise nach drei bis fünf UI-Iterationen; vorher sind sie spekulativ, weil die tragenden Prinzipien noch nicht durch Praxis validiert sind. ^p0459

Review-Folie für ein bestehendes Design-Dokument. Ein vorhandenes `design.md` wird gegen die Vorlage gehalten, um zu prüfen, ob die Designhaltung deklarativ und schärfbar formuliert ist, ob die imperative Übersetzung in `CLAUDE.md` (nicht im Designdokument selbst) lebt, ob Token-Werte fehlen statt im Dokument zu stehen, und ob Interaktionsmuster die Logik beschreiben statt Implementation zu zitieren. ^p0460

#### Beispiel

HerData führt `design.md` mit Lead, Designhaltung, Designsystem, Interaktionsmuster und Designprinzipien für den Agenten. Charakteristisch ist der Lead-Satz: "Komponenten-Detail liegt im Code, nicht in der Doku, weil es dort schneller veraltet als nutzt." Diese Begründung trägt das zweite Strukturprinzip (Verweis auf Code als Source of Truth) als ausgesprochene Regel in den Lead. ^p0461

#### Begriffe

- Designhaltung: das grundlegende ästhetische Wertesystem eines Projekts, in drei bis fünf Sätzen formuliert. ^p0462
- Designsystem: die Sammlung der Tokens, Komponenten und Layoutprinzipien, die ein Projekt einsetzt. ^p0463
- Designprinzip: imperativ formulierte Regel, die den Coding-Agenten bei UI-Generierung leitet. Lebt im Action-Layer (`CLAUDE.md`), nicht im Designdokument selbst. ^p0464
- Anbindung an den Action-Layer: die Komposition, durch die `CLAUDE.md` auf das deklarative Designdokument verweist und dessen Werte in Imperative übersetzt. ^p0465

#### Related

- [Vorlage Specification](#promptotyping-document-specification) ^p0466
- [Vorlage Architecture](#promptotyping-document-architecture) ^p0467
- [Vorlage Action-Layer](#promptotyping-document-action-layer) ^p0468
- [Konvention Promptotyping Documents](#konvention-v0.1) ^p0469

## Template `integration.md`: Vorlage Integration

Source file `_content/promptotyping-document/integration.md`, template version 0.3. ^p0470

### Vorlage Integration

Diese Vorlage strukturiert das dauerhaft gepflegte Integration-Dokument einer Promptotyping-Wissensbasis. Ein einzelner Kontrakt heißt `integration.md`; mehrere Schnittstellen werden als `<counterpart>-integration.md` spezialisiert. Das Dokument liegt im `knowledge/`-Ordner und trägt Austauschformat, Zuständigkeiten sowie Abnahmekriterien. Neue Übergabedeltas liegen bis zur fachlichen Verarbeitung in `knowledge/handoff.md`; datierte außergewöhnliche Übergabestände liegen unter `handoffs/`. ^p0471

#### Geltungsbereich

Die Vorlage trägt, sobald ein Projekt Daten, Formate oder Zuständigkeiten mit einem anderen Projekt, einem externen System oder einer parallelen Lane teilt und diese Schnittstelle explizit gemacht werden muss. Triggerkriterium ist der projektübergreifende Kontrakt. ^p0472

Das Dokument entsteht mit dem Kontrakt, idealerweise bevor die erste Lieferung fließt, und wird bei jeder Kontraktänderung auf beiden Seiten der Schnittstelle im selben Zug nachgezogen. Wird die Schnittstelle stillgelegt, bleibt der letzte gültige Kontrakt als Erklärung der gelieferten Daten erhalten. ^p0473

Integration ist von den Nachbarfunktionen Architecture, Handoff und Provenance abgegrenzt. `architecture.md` beschreibt den internen Aufbau des eigenen Projekts. `handoff.md` führt übernommene Deltas bis zu ihrer Integration oder Verwerfung. `journal.md` weist den rückwärts gerichteten Übergang nach. Integration hält den aktuell gültigen Kontrakt an der Projektgrenze. Ein dauerhafter Research-to-Operations-Handoff ist deshalb ein Declarative Integration Document. ^p0474

Zwei Zuschnitte sind gleichwertig und richten sich nach dem Adressaten. Die Mehrprojekt-Referenz (teiCrafter-Muster) beschreibt ein Mehrprojekt-Geflecht aus einer Hand für alle Beteiligten; das lane-lokale Schnittstellendokument (szd-htr-Muster) beschreibt eine Richtung aus Sicht des eigenen Repos. Beschreiben beide Seiten denselben Kontrakt, muss genau eine Seite als Quelle der Wahrheit deklariert sein und beide müssen aufeinander verweisen; die einseitige Verlinkung war der eine Konsistenzbefund der Extraktion. ^p0475

#### Funktion des Dokuments

Das Dokument beantwortet "was schulden wir dem Gegenüber, was schuldet es uns, in welchem Format, und woran erkennen beide Seiten die Erfüllung". Adressiert sind der Agent des eigenen Repos, der die Schnittstelle implementiert oder betreibt, der Agent des Gegenübers, der konsumiert oder liefert, und der Operator, der bei Kontraktänderungen entscheidet. Im Promptotyping-Kontext ist das Dokument die Stelle, an der zwei Wissensbasen konsistent gehalten werden müssen; implizites Schnittstellenwissen ist hier am teuersten. ^p0476

#### Strukturprinzipien

Erstens Kontrakt vor Implementierung. Das Austauschformat, die Zuständigkeitsgrenze und die Abnahmekriterien sind der stabile Kern; CLI-Details und Pfade sind nachgeordnet und dürfen an die Architecture delegiert werden. ^p0477

Zweitens deklarierte Quelle der Wahrheit. Wo mehrere Dokumente denselben Kontrakt berühren, benennt jede Seite explizit, welches Dokument verbindlich ist; die anderen positionieren sich als Implementierungs- oder Abnahmedokumentation. ^p0478

Drittens Richtung explizit. Ob die Schnittstelle liefert, empfängt oder beides, steht im Frontmatter (`direction`) und bestimmt den Zuschnitt; unidirektionale Lieferbeziehungen und bidirektionale Kontrakte haben verschiedene Pflichtsektionen (der Zeitplan gehört nur hinein, wenn eine externe Phase ihn erzwingt). ^p0479

#### Frontmatter-Schema

Pflichtkern der Konvention (`title`, `project`, `method`, `status`, `created`, `updated`), dazu Integration-spezifisch: ^p0480

- `template:` als Block mit `name: Vorlage Integration`, `version`, `url`, sobald diese Vorlage angewandt wurde. ^p0481
- `counterpart:` das Gegenüber als Objekt mit `name` und, falls vorhanden, `repository`. ^p0482
- `direction:` `outbound`, `inbound` oder `bidirectional`. ^p0483
- `related:` typischerweise `architecture`, `specification`, `handoff`, `journal`. ^p0484

#### Abschnitte im Detail

##### Zweck

Funktion: die Schnittstelle in einem Absatz benennen. Inhalt: wer liefert was an wen, der Use Case dahinter und was die Schnittstelle nicht ist (bei szd-htr etwa die Klarstellung, dass DIA-XAI konsumiert und nichts zurückliefert). ^p0485

##### Datenfluss

Funktion: den Übergabepunkt visuell fassbar machen. Inhalt: ein ASCII-Diagramm der beteiligten Systeme, der Richtung(en) und der Übergabepunkte. Alle Belegdokumente führen dieses Diagramm. ^p0486

##### Austauschformat

Funktion: das Format exakt festlegen. Inhalt: Feldliste oder Schema (JSON-Schema, TEI-Skelett, Mapping-Tabelle Quellfeld zu Zielfeld), Pflicht- und optionale Felder, bewusste Auslassungen mit Begründung. Bei tiefen Formaten delegiert die Sektion an ein eigenes Kontrakt-Dokument (teiCrafter delegiert an `converter-reference.md` als frozen contract) und trägt hier nur die Bindungsaussage. ^p0487

##### Zuständigkeiten

Funktion: die Grenze ziehen. Inhalt: wer produziert, wer konsumiert, wo die Trennlinie zwischen den Systemen verläuft, in wenigen Sätzen oder einer Rollen-Tabelle. ^p0488

##### Abnahmekriterien

Funktion: die Erfüllung prüfbar machen. Inhalt: die formalen Bedingungen, unter denen die Schnittstelle als erfüllt gilt, je mit Prüfweg (bei teiCrafter und szd-htr formale Engine-Checks wie Byte-Identität im Round-Trip, mit benannten Prüf-Fallen). ^p0489

##### Offene Punkte und Input-Gaps

Funktion: vertragliche Input-Verpflichtungen benennen. Inhalt: pro Verpflichtung, was geliefert werden muss, welche Seite es schuldet und welche Abnahmekriterien gelten. Neu eingegangene, noch ungeprüfte Deltas bleiben bis zur Integration in `knowledge/handoff.md`. ^p0490

##### Korrekturen und Fallgruben

Funktion: bekannte Missinterpretationen festhalten, bevor sie sich wiederholen. Inhalt: pro Fallgrube die falsche Annahme und die richtige Lesart (teiCrafter führt eine eigene Corrections-Sektion, szd-htr integriert die Byte-Identitäts-Fallen in die Abnahmekriterien). ^p0491

##### Autoritäre Dokumente

Funktion: die Quellen der Wahrheit auflisten. Inhalt: pro Aspekt des Kontrakts das verbindliche Dokument mit Pfad, auf beiden Seiten der Schnittstelle; hier wird die wechselseitige Verlinkung beider Repos hergestellt. ^p0492

#### Was nicht reingehört

- Interner Aufbau. Schichten, Module und Signaturen des eigenen Systems gehören in `architecture.md`; hier steht nur, was an der Grenze sichtbar ist. ^p0493
- Entscheidungsgeschichte. Warum der Kontrakt so aussieht, gehört in `journal.md` oder ein gegenstandsbezogenes Entscheidungsregister wie `architecture-decisions.md`; hier steht der gültige Stand. ^p0494
- Detailwissen des Gegenübers. Die Pipeline-Internas des anderen Projekts gehören in dessen Wissensbasis; hier stehen sie nur, soweit der Kontrakt sie braucht, sonst als Verweis. ^p0495
- Zeitpläne ohne externe Phase. Meilenstein-Tabellen veralten unmarkiert; sie gehören nur hinein, wenn eine externe Projektphase sie erzwingt, und dann als datierter Snapshot. ^p0496
- Wiedereinstiegsstände. Session- und Lane-Übergaben liegen als `<scope>-handoff-YYYY-MM-DD.md` unter `handoffs/` und verweisen auf den gültigen Kontrakt. ^p0497
- Ungeprüfte Übergabedeltas. Sie verbleiben bis zur Integration oder Verwerfung in `knowledge/handoff.md`. ^p0498

#### Vorlage zum Befüllen

````markdown
---
title: "Integration: [Gegenüber oder Funktion]"
project:
  name: [Projektname]
  repository: [Repository-URL]
method:
  name: Promptotyping
  url: https://lisa.gerda-henkel-stiftung.de/digitale_geschichte_pollin
template:
  name: Vorlage Integration
  version: 0.3
  url: https://dhcraft.org/Promptotyping/promptotyping-document/integration
  alias: https://dhcraft.org/Promptotyping/#promptotyping-document-integration
counterpart:
  name: [Gegenüber-Projekt oder -System]
  repository: [URL, falls vorhanden]
direction: [outbound | inbound | bidirectional]
status: draft
language: [de | en]
version: [Repo-Schema-Version]
created: [YYYY-MM-DD]
updated: [YYYY-MM-DD]
related: [architecture, specification, handoff, journal]
---

### Integration: [Gegenüber]

<!-- Erster Absatz = Zweck in einem Satz. Wer liefert was an wen, Use Case, was die Schnittstelle nicht ist. -->

[Lead-Absatz]

#### Datenfluss

<!-- ASCII-Diagramm: Systeme, Richtung(en), Übergabepunkte. -->

```
[System A] --(Format)--> [System B] ^p0499
```

#### Austauschformat

<!-- Exaktes Schema oder Feldliste, Pflicht/optional, bewusste Auslassungen mit Begründung. Bei tiefen Formaten: Bindungsaussage plus Delegation an das Kontrakt-Dokument. -->

[...]

#### Zuständigkeiten

<!-- Wer produziert, wer konsumiert, Trennlinie in einem Satz oder einer Rollen-Tabelle. -->

[...]

#### Abnahmekriterien

<!-- Formale Bedingungen der Erfüllung, je mit Prüfweg und bekannten Prüf-Fallen. -->

[...]

#### Offene Punkte und Input-Gaps

<!-- Nur vertragliche Input-Verpflichtungen. Neu eingegangene Deltas verbleiben bis zur Integration in knowledge/handoff.md. -->

[...]

#### Korrekturen und Fallgruben

<!-- Pro Fallgrube: falsche Annahme, richtige Lesart. -->

[...]

#### Autoritäre Dokumente

<!-- Pro Kontrakt-Aspekt das verbindliche Dokument mit Pfad, auf beiden Seiten. Wechselseitige Verlinkung herstellen. -->

| Aspekt | Quelle der Wahrheit | Pfad |
|---|---|---|
| [Aspekt] | [Dokument] | [Pfad] |

````

#### Anwendung als Prompt-Template

Strukturanker beim Aufsetzen einer neuen Schnittstelle. Der Agent erhält den Template-Block, das Format (Schema, Beispieldateien) und die Gegenüber-Wissensbasis; er befüllt Zweck, Datenfluss, Format und Zuständigkeiten, leitet die Abnahmekriterien aus den formalen Eigenschaften des Formats ab und prüft, ob das Gegenüber die Schnittstelle bereits beschreibt. Wenn ja, ist zuerst die Quelle der Wahrheit zu deklarieren und die wechselseitige Verlinkung herzustellen, bevor Inhalt dupliziert wird. ^p0500

Review-Folie für eine bestehende Integration. Ein vorhandenes Dokument wird gegen die Vorlage gehalten, um Richtung, Quelle der Wahrheit, beidseitige Verlinkung, Abnahmekriterien und die Trennung von datierten Handoffs zu prüfen. ^p0501

#### Beispiel

teiCrafter (`knowledge/integration.md`, "Three-Project Integration Reference") ist die Mehrprojekt-Referenz über drei Projekte: Rollen-Tabelle, Tool-Boundary, Datenfluss-Diagramm, die Kontrakte beider Pipelines, eine eigene Corrections-Sektion gegen wiederkehrende Missinterpretationen und eine Source-Evidence-Sektion als Liste der autoritären Dokumente; die Schichten des eigenen Editors delegiert es ausdrücklich an `architecture.md`. szd-htr-ocr-pipeline führt die Gegenseite lane-lokal: `teicrafter-integration.md` deklariert teiCrafters `converter-reference.md` als verbindlichen Kontrakt und positioniert sich als Implementierungs- und Abnahmedokumentation (CLI, Byte-Identitäts-Fallen, Realitätsabgleich an realen Objekten), `dia-xai-integration.md` beschreibt eine unidirektionale Lieferbeziehung mit Inline-JSON-Schema und externem Phasen-Zeitplan. Die Extraktion fand die beiden Seiten des teiCrafter-Kontrakts inhaltlich konsistent, aber nur einseitig verlinkt; die Autoritäre-Dokumente-Sektion der Vorlage adressiert genau das. ^p0502

#### Begriffe

- Kontrakt: die explizit gemachte Vereinbarung an der Projektgrenze, Format plus Zuständigkeit plus Abnahmekriterien. ^p0503
- Gegenüber (counterpart): das Projekt, System oder die Lane auf der anderen Seite der Schnittstelle, im Frontmatter benannt. ^p0504
- Richtung (direction): ob die Schnittstelle liefert (outbound), empfängt (inbound) oder beides (bidirectional). ^p0505
- Mehrprojekt-Referenz: der Zuschnitt, der ein Mehrprojekt-Geflecht aus einer Hand für alle Beteiligten beschreibt. ^p0506
- Quelle der Wahrheit: das eine pro Kontrakt-Aspekt als verbindlich deklarierte Dokument; alle anderen verweisen. ^p0507
- Input-Gap: eine ausstehende Lieferung einer Seite, die die andere blockiert. ^p0508

#### Versionshistorie

- 0.3 (2026-08-21): Process Inbox, datierte Snapshots und dauerhafter Research-to-Operations-Kontrakt funktional getrennt. ^p0509
- 0.2 (2026-08-21): Naming Contract übernommen. Integration bleibt der dauerhafte Kontrakt in `knowledge/`; datierte Wiedereinstiegsstände liegen unter `handoffs/`. ^p0510
- 0.1 (2026-07-19): Erstfassung, empirisch extrahiert aus teiCrafter und szd-htr-ocr-pipeline; Wiedereinstiegs-Kontext als ergänzte Sektion. Freigegeben am 2026-07-19. ^p0511

#### Related

- [Vorlagen Promptotyping Documents](#vorlagen) ^p0512
- [Konvention Promptotyping Documents](#konvention-v0.1) ^p0513
- 2026-07-19 - Promptotyping-Wissensbasen Inhaltsaudit (Befund) ^p0514
- [Vorlage Architecture](#promptotyping-document-architecture) ^p0515
- [Vorlage Journal](#promptotyping-document-journal) ^p0516
- [Vorlage Verification](#promptotyping-document-verification) ^p0517
- [Vorlage Handoff](#promptotyping-document-handoff) ^p0518

## Template `testing.md`: Vorlage Testing

Source file `_content/promptotyping-document/testing.md`, template version 0.3. ^p0519


### Vorlage Testing

Diese Vorlage strukturiert das Quality-Assurance-Dokument einer Promptotyping-Wissensbasis. Ein einzelner Träger heißt `testing.md`; getrennte Testdomänen werden als `<subject>-testing.md` spezialisiert. Das Dokument liegt im `knowledge/`-Ordner und trägt die Teststrategie, ihre Garantien, ihre offenen Lücken und die reproduzierbaren Run-Kommandos. Der erste Absatz bestätigt diese Funktion; ein eigenes `zweck:`- oder `function:`-Frontmatter-Feld entsteht nicht. ^p0520

#### Geltungsbereich

Die Vorlage trägt, sobald das System eine automatisierte oder systematische Qualitätssicherung führt und diese dokumentiert werden soll: eine Testsuite, eine Validierungs-Harness, eine Acceptance-Prüfung gegen die Projektziele. Triggerkriterium ist nicht die bloße Existenz einzelner Tests, sondern die Notwendigkeit, die Teststrategie als Ganzes nachvollziehbar zu machen, also was geprüft wird, was bewusst nicht geprüft wird, und welche Garantie daraus folgt. ^p0521

Bei trivialen Tool-Repos ohne eigene Tests entfällt die Vorlage; ein Satz in `architecture.md` reicht dann. Die Dokumentation einzelner Testfälle liegt im Testcode. Continuous-Integration-Konfiguration liegt in `architecture.md` oder bei eigenständiger Routing Question in `deployment-architecture.md`. Das Testing-Dokument verweist auf die CI nur als Auslöser. ^p0522

Testing bleibt im Regelfall ein Dokument. Wächst die Suite auf mehrere unabhängige Engines mit eigenen Aktualisierungsrhythmen (eine Node-Engine-Harness und eine getrennte Python/lxml-Validierungs-Harness, wie bei teiCrafter), bleiben diese dennoch Sektionen desselben Dokuments, solange sie eine gemeinsame Teststrategie tragen. Die Spaltung in eine eigene Datei lohnt sich erst, wenn ein Aspekt der Qualitätssicherung (etwa eine CER-Evaluationsmethodik in einem OCR-Projekt) einen eigenen Leser und eigenen Pflegerhythmus entwickelt. ^p0523

Lebenszyklus: das Dokument entsteht mit der ersten Suite und wird nachgezogen, wenn eine Garantie hinzukommt, eine Lücke sich schließt oder ein Run-Kommando sich ändert, im selben Commit wie die Suite selbst. Der optionale Stand-Block trägt Stichtags-Semantik und veraltet planmäßig; der Rest des Dokuments beschreibt die Strategie und veraltet nur, wenn die Suite umgebaut wird, ohne das Dokument anzufassen. ^p0524

#### Funktion des Dokuments

Das Dokument beantwortet "was garantiert dieses System nachweislich, woran zeigt es das, und was bleibt bewusst ungeprüft". Adressiert sind drei Lesergruppen: ein Reviewer, der entscheiden will, ob er einer Behauptung trauen kann oder sie selbst prüfen muss; ein Coding-Agent, der eine Änderung vornimmt und den passenden Regressionstest mitliefern soll; ein externer Prüfer oder Domänenexperte, der die Reproduzierbarkeit der Ergebnisse beurteilt. Im Promptotyping-Kontext ist die zweite Lesergruppe besonders bedeutsam: das Dokument sagt dem Agenten, in welcher Form eine neue Garantie abzusichern ist, und hebt damit jeden Sign-off von der Behauptung ("die IDs sind weg") zur Messung ("der Test ist grün"). ^p0525

#### Strukturprinzipien

Drei Prinzipien tragen das Dokument. ^p0526

Erstens trennt es Garantie von Lücke. Was das System nachweislich hält, steht getrennt von dem, was es bewusst nicht prüft. Eine Teststrategie, die nur ihre Garantien nennt, verschweigt ihre blinden Flecken und verleitet zu falschem Vertrauen. Die explizite Lücken-Sektion ist konstitutiv, nicht ein Eingeständnis von Unvollständigkeit; sie sagt dem Reviewer genau, wo er selbst hinschauen muss. ^p0527

Zweitens beschreibt es Garantien, nicht Implementationen. Was ein Proof behauptet und gegen welche Daten er es zeigt, ist Teststrategie; wie der Testcode intern aufgebaut ist, ist Code. Eine Beschreibung, die in den Testcode hineingreift, veraltet schneller als sie nutzt. Die zentrale Information ist die Behauptung pro Proof und ihr Belegstatus, nicht der Code, der sie prüft. ^p0528

Drittens bindet es Tests an die Projektziele zurück. Eine Testsuite ist kein Selbstzweck, sondern der Maßstab für die Frage, ob das System sein Ziel erreicht. Das Dokument macht diese Bindung über eine Acceptance-Sektion explizit: pro Projektziel die Methode, die es prüft, und der Beleg, dass sie grün ist. Damit unterscheidet sich das Dokument von einer reinen Liste grüner Tests. ^p0529

#### Frontmatter-Schema

Das Dokument folgt dem reduzierten Pflichtkern der aktuellen Konvention: `title`, `project` (Objekt mit `name` und `repository`), `method` (Objekt mit `name` und `url`), `status`, `created`, `updated`. Der Dateiname ist das primäre Routing-Signal, der erste Absatz bestätigt die Funktion. Es gibt kein `zweck:`- oder `function:`-Feld. ^p0530

- `template:` empfohlen, als Block mit `name`, `version`, `url` und optional `alias`, dort wo diese Vorlage angewandt wurde. teiCrafter führt das Feld bereits kanonisch mit der dhcraft.org-URL. ^p0531
- `status:` meint die Dokument-Maturity (`idea`, `draft`, `stub`, `complete`, `reviewed`, `archived`; seit 2026-07-19 auch `active` für fortlaufende Prozessdokumente und `snapshot` für Stichtagsdokumente), nicht den operativen Projektstatus. Ein Testing-Dokument mit gepflegtem Stand-Block kann `snapshot`-Semantik tragen; maßgeblich ist das Vokabular der Konvention. ^p0532
- `topics:` typisch sind `[[Software Testing]]`, `[[Regression]]`, `[[Test-Driven Development]]`, `[[Data Validation]]`, `[[Evaluation]]`. Bei Editions- und OCR-Projekten zusätzlich domänennahe Topics wie `[[TEI XML]]`. Sie verorten den Agenten in den Wissensfeldern, in denen Teststrategie reasoning braucht. ^p0533
- `version:` repo-weit konsistent, gemeinsam mit den Geschwister-Dokumenten erhöht. ^p0534
- `authors:` trägt ausschließlich Menschen, auch wenn ein LLM den Text erzeugt hat; `generated-with:` daneben im Format `Harness (LLM)`, etwa `Claude Code (Claude Opus 5)`, falls LLM-gestützt entstanden. Siehe Sektion *Provenienz im Frontmatter* der Konvention. ^p0535
- `related:` typischerweise `architecture`, `specification`, `data`; die Dokumente, gegen die die Tests messen. ^p0536

#### Abschnitte im Detail

##### Lead

Funktion: in ein bis drei Sätzen die Teststrategie in ihrem Kern benennen und damit den Zweck tragen. Inhalt: das tragende Prinzip (Testing-first, Output-testen-statt-Code-testen, vier Säulen), die Architektur der Prüfung (headless Proofs plus Validierungs-Harness, oder pytest plus Verifikations-Set plus manuelle Sichtprüfung), und der eine Satz, der das Dokument zusammenfasst. teiCrafter führt hier "Testing-first. Der Maßstab wird vor den Features gebaut, die er beurteilt"; M3GIM führt "Die Test-Suite validiert den Output der Pipeline, nicht den Pipeline-Code". ^p0537

##### Teststrategie und Test-Taxonomie

Funktion: die Architektur der Qualitätssicherung benennen, das tragende Ordnungsprinzip der Tests. Inhalt: die Säulen oder Ebenen, in die sich die Tests gliedern, je mit der Fehlerklasse, die sie abdecken und die die anderen nicht sehen. SuGW führt vier komplementäre Säulen (pytest für den Build-Code, Verifikations-Set für die Daten-Konsistenz End-to-End, JS-Tests für die Browser-Logik, manuelle Sichtprüfung); teiCrafter führt zwei Schichten (headless Engine-Proofs und eine Validierungs-Harness mit drei Leveln); co-ocr-htr führt eine Logik-vor-UI-Priorisierung. Die Taxonomie ist der Kern dieser Sektion: jede wiederkehrende Test-Art bekommt einen Namen und eine abgegrenzte Fehlerklasse. ^p0538

##### Was garantiert wird (Proofs)

Funktion: die zentralen Garantien einzeln auflisten, je mit Behauptung und Belegstatus. Inhalt: eine Tabelle mit Spalten Proof, Was behauptet wird, Ergebnis. Bei teiCrafter sind das die Engine Proofs (die zentrale Behauptung "lies beliebiges TEI und speichere es byte-verlustfrei zurück", belegt durch den roundtrip-Sweep) und die Feature Proofs pro Meilenstein. Bei einem Daten-Pipeline-Projekt sind das die Teststufen (Schema-Validierung, String-Integrität, referentielle Integrität, Determinismus). Pro Eintrag steht die Behauptung, nicht der Code; das Ergebnis ist binär (PASS oder Zahlenstand wie 295/295) oder qualitativ (grün, wechselnd). Konkrete Test-Zähler dürfen hier stehen, weil dieses Dokument ein Snapshot-Charakter trägt; die Regel gegen volatile Metriken gilt für Wissens- und Strategiedokumente, nicht für ein Testing-Dokument, das den Belegstand führt. ^p0539

##### Acceptance und Engine-Proofs (Verifikation der Projektziele)

Funktion: die Tests an die Projektziele zurückbinden. Inhalt: pro Projektziel oder Erfolgskriterium die Frage, die zu beantworten ist, die Verifikationsmethode, die Ebene (automatisch, kontextuell, visuell, professionell) und der Beleg. teiCrafter führt diese Verifikationskaskade explizit: "Wurde alles verarbeitet" (Coverage-Sweep, automatisch), "Ist der Output valides TEI" (Schema, automatisch), "Geht nichts verloren und ist die einzige Änderung die beabsichtigte" (Roundtrip-Byte-Identität, kontextuell), "Funktioniert die intendierte Nutzung für einen Menschen" (Browser-Durchlauf, visuell), "Ist es korrekt als Edition" (Domänenexperten-Review, professionell). Der Engine-Proof ist dabei die zentrale Behauptung, die das ganze System trägt; er steht hier, weil er die Brücke zwischen Testsuite und Projektziel ist. Bei kleineren Projekten reduziert sich diese Sektion auf eine kurze Zuordnung der Säulen zu den Akzeptanzfragen. ^p0540

##### Was bewusst nicht geprüft wird (Lücken)

Funktion: die blinden Flecken der Teststrategie explizit machen. Inhalt: pro Lücke, was nicht abgedeckt ist, warum (nicht automatisierbar, nicht lohnend, separater Meilenstein), und wodurch sie aktuell ersatzweise gedeckt ist. SuGW führt "Browser-Visual-Regression" (Screenshot-Vergleich, separater Meilenstein, aktuell durch manuelle Sichtprüfung gedeckt), "JS-rendered DOM-Inhalte" und "Stakeholder-Acceptance". M3GIM führt unter "Abgrenzungen" Pipeline-Internas, Google-Sheets-Content und Performance als bewusst ungetestet. co-ocr-htr führt UI-Komponenten, externe Abhängigkeiten und visuelle Aspekte. Diese Sektion ist konstitutiv: eine Garantie ohne benannte Lücke ist eine Behauptung, keine Strategie. ^p0541

##### How to Run

Funktion: einem Dritten ermöglichen, die Tests selbst zu laufen. Inhalt: die konkreten Kommandos in einem Codeblock, je mit einem Kommentar, was sie prüfen und welchen Zielstand sie haben. teiCrafter führt "node test/tools/run_all.mjs" als das eine Regression-Gate plus die Einzel-Proofs mit Zielständen; M3GIM führt "pytest tests/ -m 'not slow'" plus die Determinismus-Variante; co-ocr-htr führt die npm-test-Kommandos. Dazu gehören gegebenenfalls ENV-Overrides für Pfade und Datenquellen (M3GIM und teiCrafter führen beide solche Overrides). Dies ist der Process-Anteil des sonst deklarativen Knowledge-Dokuments: ausführbare Anweisung, nicht Beschreibung. ^p0542

##### Pattern: Test im selben Commit (optional)

Funktion: das Arbeitsprinzip festhalten, dass jede prüfbare Änderung im selben Commit ihren Regressionstest bekommt. Inhalt: die Regel, ihre Begründung (Tests als Nachgedanke produzieren Lücken), Beispiele und die ausgewiesene Ausnahme (rein visuelle Politur). SuGW führt diese Sektion prominent. Trigger: das Repo praktiziert Test-getriebene oder test-begleitete Entwicklung. Bei Suiten ohne dieses Prinzip entfällt die Sektion. ^p0543

##### TDD-Workflow und Anker-Strategie (optional)

Funktion: dokumentieren, wie neue Garantien entstehen und wie Einzelfall-Fixtures als Living Documentation dienen. Inhalt: der xfail-Workflow (Invariante zuerst als strict-xfail formulieren, dann implementieren, XPASS signalisiert fertige Phase) und die Anker-Record-Strategie (wenige kuratierte Fixtures, die ihre Quell-Herkunft explizit halten und damit die Abbildung Quelle-zu-Output im Test selbst nachlesbar machen). M3GIM führt beides ausführlich. Trigger: das Projekt erweitert ein Datenmodell iterativ. Bei statischen Suiten entfällt die Sektion. ^p0544

##### Bekannte Ausnahmen und Grenzen (optional)

Funktion: dauerhaft tolerierte Abweichungen festhalten. Inhalt: pro Ausnahme der Testname, der Status (xfail, skip), die Ursache und die Bedingung, unter der die Ausnahme aufgehoben wird. M3GIM führt "test_all_record_ids_unique xfail (PL_07 Duplikat aus der Quelle, Fix im Sheet)" und eine skip-Begründung. co-ocr-htr führt unter "Known Limitations" einen konkreten Regex-lastIndex-Bug als gefangene und gefixte Falle. Trigger: die Suite trägt bewusst tolerierte Rot- oder Skip-Zustände. ^p0545

##### Komponenten (optional)

Funktion: die Testdateien und Hilfswerkzeuge auflisten, damit ein Entwickler den Einstieg findet. Inhalt: pro Datei oder Werkzeug ein Satz zur Funktion (der Validator, der Orchestrator, der Negativ-Selbsttest, die Fixture-Generatoren). teiCrafter und M3GIM führen beide eine solche Komponenten- oder Struktur-Auflistung. Trigger: die Suite ist groß genug, dass ihre Struktur selbst Orientierung braucht. Bei kleinen Suiten reicht die How-to-Run-Sektion. ^p0546

##### Aktueller Stand (optional)

Funktion: den Belegstand der Suite zum Stichtag festhalten. Inhalt: eine Tabelle Säule/Stufe, Tests, Status. SuGW und M3GIM führen einen solchen Stand-Block. Dies ist die einzige Stelle, an der volatile Zahlen unkritisch sind, weil das Testing-Dokument ohnehin Snapshot-Charakter trägt. Bei jedem substanziellen Suiten-Stand wird die Tabelle nachgezogen. ^p0547

#### Was nicht reingehört

- Stack und Architecture. Welche Technologien das System einsetzt und wie es aufgebaut ist, gehört in `architecture.md`. Das Testing-Dokument nennt den Test-Runner als Werkzeug (Vitest, pytest, Node-Harness), nicht den Anwendungs-Stack. ^p0548
- Provenance und Chronik. Wie die Suite über Sessions gewachsen ist, welche Sackgassen es gab, gehört in `journal.md`. Das Testing-Dokument trägt den aktuellen Garantiestand, keine Entwicklungsgeschichte. Meilenstein-Bezüge in Proof-Namen (M3.7, Session 33) sind als stabile IDs erlaubt, nicht als Chronik. ^p0549
- Anforderungen. Welche Funktionalität das System leisten soll, gehört in `specification.md`. Das Testing-Dokument prüft gegen diese Anforderungen, formuliert sie nicht. ^p0550
- Code-Implementation des Testcodes. Wie ein Proof intern aufgebaut ist, gehört in den Testcode (Testnamen, Assertions, Kommentare). Das Dokument trägt die Behauptung pro Proof, nicht ihren Code. ^p0551
- CI/CD-Konfiguration. Die Workflow-Datei ist Source of Truth in `architecture.md` oder `.github/workflows/`. Das Testing-Dokument nennt den Auslöser, nicht die Konfiguration. ^p0552

#### Vorlage zum Befüllen

Der folgende Block ist als Template gedacht. Optionale Sektionen, die nicht zutreffen, werden vor dem Commit gelöscht, nicht leer geführt. Der erste Absatz unter der H1 trägt den Zweck in einem Satz. ^p0553

````markdown
---
title: Testing
project:
  name: [Projektname]
  repository: [Repository-URL]
method:
  name: Promptotyping
  url: https://lisa.gerda-henkel-stiftung.de/digitale_geschichte_pollin
template:
  name: Vorlage Testing
  version: 0.3
  url: https://dhcraft.org/Promptotyping/promptotyping-document/testing
  alias: https://dhcraft.org/Promptotyping/#promptotyping-document-testing
status: draft
created: [YYYY-MM-DD]
updated: [YYYY-MM-DD]
language: [de | en]
version: [Repo-Schema-Version]
authors: [Autor 1, Autor 2]
generated-with: [Harness (LLM), falls relevant]
topics: ["[[Software Testing]]", "[[Regression]]"]
related: [architecture, specification, data]
---

### Testing

<!-- Erster Absatz = Zweck in einem Satz. Tragendes Prinzip (Testing-first, Output-testen, vier Säulen), Architektur der Prüfung, der eine zusammenfassende Satz. -->

[Lead-Absatz]

#### Teststrategie

<!-- Die Säulen oder Ebenen, je mit der Fehlerklasse, die sie abdecken und die anderen nicht sehen. -->

[...]

#### Was garantiert wird

<!-- Tabelle: Proof, Behauptung, Ergebnis. Behauptung statt Code. Zähler erlaubt (Snapshot-Dokument). -->

| Proof | Was behauptet wird | Ergebnis |
|---|---|---|
| [Proof] | [Behauptung] | [PASS / n/n / grün] |

#### Acceptance

<!-- Pro Projektziel: Frage, Methode, Ebene (automatisch/kontextuell/visuell/professionell), Beleg. Engine-Proof als zentrale Behauptung. -->

| Frage | Methode | Ebene | Beleg |
|---|---|---|---|
| [Frage] | [Methode] | [Ebene] | [Beleg] |

#### Was bewusst nicht geprüft wird

<!-- Pro Lücke: was nicht abgedeckt, warum, wodurch ersatzweise gedeckt. Konstitutiv. -->

[...]

#### How to Run

<!-- Konkrete Kommandos mit Zielstand. ENV-Overrides falls relevant. Der Process-Anteil. -->

```
[kommando]                # was es prüft, Zielstand ^p0554
```

<!-- ============================================================ -->
<!-- OPTIONALE SEKTIONEN: vor dem Commit nicht zutreffende löschen -->
<!-- ============================================================ -->

#### Pattern: Test im selben Commit

<!-- Trigger: test-begleitete Entwicklung. Regel, Begründung, Beispiele, ausgewiesene Ausnahme. -->

[...]

#### TDD-Workflow und Anker-Strategie

<!-- Trigger: iterative Modell-Erweiterung. xfail-Workflow, Anker-Records als Living Documentation. -->

[...]

#### Bekannte Ausnahmen und Grenzen

<!-- Trigger: bewusst tolerierte Rot-/Skip-Zustände. Pro Eintrag: Testname, Status, Ursache, Aufhebungsbedingung. -->

[...]

#### Komponenten

<!-- Trigger: große Suite. Pro Datei/Werkzeug ein Funktionssatz. -->

[...]

#### Aktueller Stand

<!-- Trigger: Belegstand zum Stichtag gewünscht. Tabelle Säule, Tests, Status. -->

| Säule | Tests | Status |
|---|---|---|
| [Säule] | [n] | [grün] |
````

#### Anwendung als Prompt-Template

Strukturanker beim Aufsetzen der Qualitätssicherung. Der Agent erhält den Template-Block und befüllt ihn aus der real existierenden Testsuite, den Testdateinamen, den Assertions und den Run-Skripten. Die Acceptance-Sektion verlangt eine Rückbindung an die Projektziele aus `specification.md`; sie sollte gegen das Spec-Dokument geprüft werden. Die Lücken-Sektion verlangt Ehrlichkeit über das Ungeprüfte und sollte nicht aus Reflex leer bleiben. ^p0555

Review-Folie für eine bestehende Teststrategie. Ein vorhandenes `testing.md` wird gegen die Vorlage gehalten, um zu prüfen, ob Garantie und Lücke getrennt sind, ob die Proofs ihre Behauptung statt ihren Code tragen, ob eine Acceptance-Bindung an die Projektziele existiert, ob die How-to-Run-Sektion einen Dritten tatsächlich zum Laufen bringt, und ob keine Architecture oder Chronik in das Dokument hineingewachsen ist. ^p0556

#### Beispiel

Der kanonische Träger dieser Funktion ist teiCrafter (`knowledge/testing.md`, "Testing and Evaluation Harness", führt das `template:`-Feld mit der dhcraft.org-URL bereits kanonisch). Es ist Testing-first organisiert: der Lead trägt "Testing-first. Der Maßstab wird vor den Features gebaut, die er beurteilt", dazu die Zwei-Schichten-Architektur (headless Engine-Proofs in Node und eine Validierungs-Harness in Python/lxml) und das eine Regression-Gate `node test/tools/run_all.mjs`. Die zentrale Behauptung ist der Engine-Proof "lies beliebiges TEI und speichere es byte-verlustfrei zurück", belegt durch `roundtrip_sweep.mjs` (byte-identisch über den ganzen realen Korpus). Die Validierungs-Harness führt drei Level (Text-/Wort-Fidelity, Schema-Validität gegen TEI All RelaxNG plus Schematron, strukturelle Invarianten). Die Acceptance-Sektion bindet fünf Projektfragen an Methode und Ebene zurück (automatisch, kontextuell, visuell, professionell) und benennt die visuelle Ebene als Mittelpunkt für "haben wir das Ziel in unserem Sinn erreicht". Die bewusste Lücke ist der Browser-Click-Through der UI, den die headless Proofs nicht abdecken können; er wird durch benannte Browser-Check-Szenarien gedeckt. Die How-to-Run-Sektion listet jeden Proof als Kommando mit Zielstand und ENV-Overrides für die Datenquellen. ^p0557

Drei komplementäre Genres zeigen die Bandbreite. SuGW (`test-strategy.md`) führt das Vier-Säulen-Modell (pytest für den Build-Code, Verifikations-Set für die Daten-Konsistenz End-to-End in drei Coverage-Stufen, JS-Tests für die Browser-Logik, manuelle Sichtprüfung), das Pattern "Code plus Test im selben Commit" mit ausgewiesener Ausnahme für rein visuelle Politur, und eine explizite Sektion "Lücken, die bewusst offen bleiben" (Browser-Visual-Regression als separater Meilenstein, JS-rendered DOM, Stakeholder-Acceptance). M3GIM (`tests.md`) führt das Prinzip "validiert den Output der Pipeline, nicht den Pipeline-Code", eine durchnummerierte Teststufen-Taxonomie mit bewussten ID-Lücken, den TDD-Workflow mit strict-xfail und die Anker-Record-Strategie als Living Documentation ("Zelle 123 in Objekte.xlsx wird zu diesem Record"), dazu eine "Abgrenzungen"-Sektion mit bewusst Ungetestetem und dokumentierten Ausnahmen (PL_07 xfail, NIM_11 skip). co-ocr-htr (`TESTING.md`) führt die Logik-vor-UI-Priorisierung mit zwei expliziten Listen "What We Test" und "What We Don't Test" und unter "Known Limitations" einen konkret gefangenen Regex-lastIndex-Bug. Alle vier teilen die Grundfigur: Garantie und Lücke werden getrennt geführt, und die Tests sind an die Projektziele zurückgebunden statt als Selbstzweck gelistet. ^p0558

Das Fehlmuster aus dem Inhaltsaudit vom Juli 2026 ist die doppelt geführte Teststrategie, einmal in `architecture.md` und einmal in `test-strategy.md`, ohne dass eine der beiden als Quelle der Wahrheit deklariert ist; jede Suiten-Änderung muss dann zwei Stellen treffen und verfehlt in der Praxis eine. ^p0559

#### Begriffe

- Teststrategie: das tragende Ordnungsprinzip der Qualitätssicherung, also welche Test-Arten existieren, welche Fehlerklasse jede abdeckt und welche Garantie daraus folgt. ^p0560
- Proof: eine einzelne, benannte Garantie mit expliziter Behauptung und binärem oder qualitativem Belegstatus; bei teiCrafter ein headless Check, der eine Engine- oder Feature-Eigenschaft gegen reale Daten zeigt. ^p0561
- Acceptance: die Rückbindung der Tests an die Projektziele, pro Ziel mit Frage, Methode, Verifikationsebene und Beleg. ^p0562
- Verifikationsebene: die Art der Prüfung in der Promptotyping-Kaskade, automatisch (maschinell), kontextuell (gegen reale Daten und intendierte Änderung), visuell (Browser-Durchlauf durch einen Menschen) oder professionell (Domänenexperten-Review). ^p0563
- Lücke: ein bewusst ungeprüfter Bereich der Qualitätssicherung, mit Begründung und Angabe der ersatzweisen Deckung; konstitutiver Bestandteil, nicht Eingeständnis. ^p0564
- xfail: ein Test, der absichtlich rot ist, weil die geprüfte Invariante noch nicht implementiert ist; mit strict-Modus bricht die Suite, sobald er grün wird, was die fertige Phase signalisiert. ^p0565

#### Versionshistorie

- 0.3 (2026-08-21): Naming Contract übernommen. Einzelträger heißt `testing.md`, Spezialisierungen folgen `<subject>-testing.md`; der Dateiname ist das primäre Routing-Signal. ^p0566
- 0.2 (2026-07-19): Freigabe (status complete), englisches Funktionsvokabular (Quality Assurance), Lebenszyklus-Absatz, Fehlmuster im Beispiel. Keine Migrationspflicht für bestehende Repos. ^p0567
- 0.1 (2026-06-13): Erstfassung, empirisch destilliert aus teiCrafter, SuGW, M3GIM und co-ocr-htr. ^p0568

#### Related

- [Konvention Promptotyping Documents](#konvention-v0.1) ^p0569
- [Vorlage Architecture](#promptotyping-document-architecture) ^p0570
- [Vorlage Specification](#promptotyping-document-specification) ^p0571
- [Vorlage Datengrundlage](#promptotyping-document-data) ^p0572
- [Vorlage Journal](#promptotyping-document-journal) ^p0573

## Template `verification.md`: Vorlage Verification

Source file `_content/promptotyping-document/verification.md`, template version 0.2. ^p0574


### Vorlage Verification

Diese Vorlage strukturiert das Verification-Dokument einer Promptotyping-Wissensbasis. Ein einzelner Träger heißt `verification.md`; getrennte Prüfgegenstände werden als `<subject>-verification.md` spezialisiert. Das Dokument liegt im `knowledge/`-Ordner und trägt die adversariale Prüfung eigener empirischer und Neuheits-Claims gegen die Rohdaten. Der erste Absatz bestätigt die über den Dateinamen geroutete Funktion. ^p0575

#### Geltungsbereich

Die Vorlage trägt, sobald das Projekt empirische Befunde oder Neuheitsansprüche erhebt, die außenwirksam verwendet werden, in einem Paper, einem Bericht, einer Übergabe an einen Auftraggeber oder einer öffentlichen Site. Triggerkriterium ist der außenwirksame Claim, nicht die bloße Existenz von Daten: ein Projekt, das nur intern exploriert, braucht kein Verification-Dokument. ^p0576

Lebenszyklus: das Dokument entsteht, bevor der erste außenwirksame Claim das Projekt verlässt, nicht danach; eine nachgereichte Verification prüft eine bereits publizierte Formulierung und kann sie nur noch einschränken. Aktualisiert wird es bei jedem neuen Claim und jedem Prüflauf; am Projektende bleibt es als finaler Prüfstand stehen, weil die Bindungsregel für publizierte Formulierungen fortgilt. ^p0577

Verification ist von drei Nachbarfunktionen abgegrenzt. Quality Assurance (`testing.md`) prüft Systemverhalten gegen die Spezifikation, ob Code und Pipeline tun, was sie sollen; Verification prüft, ob inhaltliche Behauptungen durch die Rohdaten gedeckt sind. Reporting unter `snapshots/` kommuniziert Ergebnisse an einen externen Adressaten; Verification prüft deren Belastbarkeit, bevor sie berichtet werden. Provenance (`journal.md`) hält den chronologischen Entscheidungsverlauf; Verification ist die synchrone, antagonistische Prüfung einer Behauptung gegen ihren Beleg. ^p0578

#### Funktion des Dokuments

Das Dokument beantwortet "was behaupten wir, hält es einer Widerlegung stand, und woran erkennt ein Dritter das". Die Grundhaltung ist adversarial: das Verfahren versucht die eigenen Claims zu widerlegen, nicht zu bestätigen. Adressiert sind der Operator als Critical Expert, der über die Freigabe außenwirksamer Formulierungen entscheidet, ein Coding-Agent, der Prüfergebnisse setzt oder liest, und ein externer Reviewer, der die Belastbarkeit der Ergebnisse beurteilt. Die Bindungsregel aus der FemPrompt-Praxis gilt als Grundprinzip: außenwirksame Claims dürfen nur in der Form verwendet werden, die die Verification lizenziert. ^p0579

#### Strukturprinzipien

Erstens Widerlegung statt Bestätigung. Jede Prüfung ist als Widerlegungsversuch angelegt; ein Claim gilt als gestützt, wenn der Versuch scheitert, nicht wenn eine wohlwollende Lektüre ihn plausibel findet. Agreement mehrerer Prüfer ist ein Signal, keine Wahrheit. ^p0580

Zweitens kontrolliertes Verdikt-Vokabular. Jedes Prüfergebnis trägt einen Wert aus einem geschlossenen, im Dokument definierten Vokabular, und jeder Wert hat eine definierte Konsequenz für die Weiterverwendung. Prosa-Einschätzungen ohne Verdikt sind keine Prüfergebnisse. ^p0581

Drittens maschinenlesbare Persistenz. Prüfergebnisse leben nicht nur in Prosa, sondern als strukturierte Felder (Frontmatter-Status, JSON-Blöcke, YAML-Register), damit nachgelagerte Werkzeuge und Agenten auf ihnen aufsetzen können. Alle drei Belegprojekte persistieren so. ^p0582

#### Frontmatter-Schema

Pflichtkern der Konvention (`title`, `project`, `method`, `status`, `created`, `updated`), dazu Verification-spezifisch: ^p0583

- `template:` als Block mit `name: Vorlage Verification`, `version`, `url`, sobald diese Vorlage angewandt wurde. ^p0584
- `scope:` was geprüft wird, aus `empirical-claims`, `novelty-claims`, `conformance`, `provenance`, `quality` (mehrere Werte möglich). ^p0585
- `prüfstand:` Pfad oder Bezeichnung der Referenzquelle, gegen die geprüft wird (Rohdaten-Ordner, Volltexte, Ground Truth). ^p0586
- `verdict-vocabulary:` Verweis auf die Sektion, die das Vokabular definiert, oder Kurzform (`fünfstufig`, `dreistufig`). ^p0587
- `output-of:` trägt den Befehl, der das Dokument erzeugt, und wird gesetzt, sobald ein Prüfskript den Befund aus den Prüfläufen rendert. Steht das Feld, wird das Dokument nicht von Hand bearbeitet und eine Korrektur geht an das Skript. Bleibt die Prosa des Dokuments menschlich verantwortet und nur das Befundregister maschinell gefüllt, wandert das Register in eine eigene Datei und das Feld steht dort. ^p0588
- `authors:` trägt ausschließlich Menschen, auch wenn ein LLM den Text erzeugt hat; `generated-with:` nennt Harness und LLM im Format `Harness (LLM)`, etwa `Claude Code (Claude Opus 5)`. Zu allen drei Feldern siehe Sektion *Provenienz im Frontmatter* der [Konvention Promptotyping Documents](#konvention-v0.1). ^p0589
- `related:` typischerweise `data`, `journal`, `testing` und der konkrete datierte Report unter `snapshots/`, falls einer existiert. ^p0590

#### Abschnitte im Detail

##### Prüfgegenstand

Funktion: benennen, welche Einheiten der Prüfung unterliegen und welcher Prüfstand als Referenz dient. Inhalt: die Einheit (Aussagen, Evidenz-Einträge, Transkriptionen, Kopfzahlen, Konformanz-Items), die Referenzquelle mit Pfad und die Zuordnungsregel zwischen beiden. Bei FemPrompt sind das Evidenz-Einträge gegen die zeichengenauen Volltexte, bei szd-htr Transkriptionen gegen verifizierte Referenzobjekte, bei kisug Kernaussagen gegen Block-Referenzen der Quelltexte. ^p0591

##### Prüfprobleme

Funktion: die spezifischen Risiken jeder Verdichtungsstufe benennen, gegen die geprüft wird. Inhalt: nach dem kisug-Muster mindestens Treue (gibt die Verdichtung die Quelle wieder), Zusammenführung (beziehen sich zusammengeführte Aussagen wirklich auf dasselbe), Vollständigkeit (fehlt Gegenevidenz) und Relationen; projektspezifische Risiken kommen dazu. ^p0592

##### Verdikt-Vokabular

Funktion: das geschlossene Ergebnis-Vokabular definieren, mit Konsequenz pro Wert. Inhalt: mindestens dreistufig (gestützt, teilweise, Befund), besser fünfstufig nach den Belegmustern (kisug: stützt voll, stützt teilweise, überdehnt, widerspricht, nicht im Text; FemPrompt: OK, Paraphrase, Confabulation, Duplikat, Gegenevidenz). Pro Wert steht die Migrationskonsequenz, also was mit dem geprüften Artefakt geschehen darf (verwenden, nachbessern, sperren). Statuswerte wie `verifiziert` werden ausschließlich nach bestandener Prüfung gesetzt. ^p0593

##### Prüfkette

Funktion: das Stufenmodell der Prüfung von deterministisch nach menschlich dokumentieren. Inhalt: Stufe 1 formale Integrität (Lint, Ankerauflösung, Zitat-Identität, deterministisch per Skript), Stufe 2 adversariale Maschinenprüfung, Stufe 3 bindende menschliche Verifikation durch den Critical Expert. Nur Stufe 3 erzeugt den höchsten Status. Alle drei Belegprojekte führen diese Kette in vergleichbarer Form. ^p0594

##### Anti-Anchoring-Protokoll

Funktion: sicherstellen, dass der Prüfer nicht von der Begründung des Verfassers verankert wird. Inhalt: die Regel, dass der Prüfer nur Quellstelle und Behauptung sieht, nicht die Herleitung; ob ein Zweitprüfer aus einer fremden Modellfamilie läuft (Dekorrelation); wie der Prüfer selbst kalibriert wird (Kontrollfälle mit bekannter Wahrheit). Empirisch belegt in kisug, dort das stärkste Muster des Bestands. ^p0595

##### Neuheits-Claims

Funktion: die eigenen Beitragsbehauptungen explizit auflisten und je gegen den Stand der Forschung prüfen. Inhalt: pro Claim die Behauptung im Wortlaut, die Recherche mit dem Ziel der Widerlegung (nicht der Bestätigung), die gefundene nächstliegende Vorarbeit und das Verdikt. Diese Sektion ist im Bestand nirgends realisiert und der genuin neue Beitrag der Vorlage; das Audit vom 2026-07-19 hat gezeigt, dass keine einzige Wissensbasis ihre Neuheits-Claims systematisch prüft. ^p0596

##### Befundregister

Funktion: festhalten, wo Prüfergebnisse persistiert werden und wer sie ändern darf. Inhalt: die Träger (Frontmatter-Felder der geprüften Dokumente, Waitlist- oder Befund-Datei, JSON/YAML-Pendant), das Format pro Eintrag und das Verantwortungsprotokoll (welche Stufe welchen Status setzen darf). ^p0597

##### Offene Befunde und Eskalation

Funktion: benennen, was die Prüfung nicht abschließend klären konnte. Inhalt: pro offenem Befund die Klasse, der Grund der Nichtentscheidbarkeit und der Eskalationspfad zur menschlichen Prüfung, nach dem Waitlist-Muster aus FemPrompt. ^p0598

##### Grenzen

Funktion: aussprechen, was das Verfahren strukturell nicht leisten kann. Inhalt: die bekannten Deckengrenzen, etwa dass Ground-Truth-freie Verfahren Plausibilität statt Korrektheit messen, dass Agreement mehrerer Modelle keine Wahrheit garantiert, dass Halluzinationen unterhalb der Erkennungsschwelle durchrutschen können. Diese Sektion ist konstitutiv, eine Verification ohne benannte Grenzen ist selbst ein ungedeckter Claim. ^p0599

#### Was nicht reingehört

- Systemtests. Ob Code und Pipeline funktionieren, gehört in `testing.md`; hier geht es um inhaltliche Behauptungen. ^p0600
- Berichtsprosa. Die außenwirksame Darstellung der Ergebnisse gehört in den datierten Report unter `snapshots/`; Verification lizenziert sie nur. ^p0601
- Chronologie. Wann welche Prüfung lief und was dabei entschieden wurde, gehört in `journal.md`; hier steht der aktuelle Prüfstand pro Claim. ^p0602
- Rohdaten-Beschreibung. Was die Daten sind, gehört in `data.md`; hier steht nur der Prüfstand-Verweis. ^p0603

#### Vorlage zum Befüllen

````markdown
---
title: Verification
project:
  name: [Projektname]
  repository: [Repository-URL]
method:
  name: Promptotyping
  url: https://lisa.gerda-henkel-stiftung.de/digitale_geschichte_pollin
template:
  name: Vorlage Verification
  version: 0.2
  url: https://dhcraft.org/Promptotyping/promptotyping-document/verification
  alias: https://dhcraft.org/Promptotyping/#promptotyping-document-verification
status: draft
language: [de | en]
version: [Repo-Schema-Version]
created: [YYYY-MM-DD]
updated: [YYYY-MM-DD]
scope: [empirical-claims | novelty-claims | conformance]
prüfstand: [Pfad oder Bezeichnung der Referenzquelle]
verdict-vocabulary: [fünfstufig | dreistufig | Verweis auf Sektion]
related: [data, journal, testing]
---

### Verification

<!-- Erster Absatz = Zweck in einem Satz. Was wird geprüft, gegen welchen Prüfstand, mit welcher Grundhaltung (Widerlegung). -->

[Lead-Absatz]

#### Prüfgegenstand

<!-- Einheit der Prüfung, Referenzquelle mit Pfad, Zuordnungsregel. -->

[...]

#### Prüfprobleme

<!-- Mindestens Treue, Zusammenführung, Vollständigkeit, Relationen; plus projektspezifische Risiken. -->

[...]

#### Verdikt-Vokabular

<!-- Geschlossenes Vokabular, pro Wert die Migrationskonsequenz. -->

| Verdikt | Bedeutung | Konsequenz |
|---|---|---|
| [Wert] | [Definition] | [verwenden / nachbessern / sperren] |

#### Prüfkette

<!-- Stufe 1 deterministisch, Stufe 2 adversarial maschinell, Stufe 3 menschlich bindend. Nur Stufe 3 erzeugt den höchsten Status. -->

[...]

#### Anti-Anchoring-Protokoll

<!-- Prüfer sieht nur Quellstelle und Behauptung. Zweitprüfer fremder Modellfamilie ja/nein. Kalibrierung über Kontrollfälle. -->

[...]

#### Neuheits-Claims

<!-- Pro Claim: Wortlaut, Widerlegungsrecherche, nächstliegende Vorarbeit, Verdikt. -->

| Claim | Nächstliegende Vorarbeit | Verdikt |
|---|---|---|
| [Behauptung] | [Quelle] | [hält / einschränken / fallen lassen] |

#### Befundregister

<!-- Wo Ergebnisse persistiert werden (Frontmatter, Befund-Datei, JSON/YAML), Format, wer welchen Status setzen darf. -->

[...]

#### Offene Befunde und Eskalation

<!-- Pro offenem Befund: Klasse, Grund der Nichtentscheidbarkeit, Eskalationspfad. -->

[...]

#### Grenzen

<!-- Was das Verfahren strukturell nicht leisten kann. Konstitutiv. -->

[...]
````

#### Anwendung als Prompt-Template

Strukturanker beim Aufsetzen der Verification. Der Agent erhält den Template-Block, die Liste der außenwirksamen Claims aus datierten Reports, Research Artefacts oder `project.md` und den Prüfstand-Pfad. Er befüllt Prüfgegenstand, Vokabular und Prüfkette, führt die maschinellen Stufen aus und übergibt die bindenden Entscheidungen als offene Befunde an den Operator. Die Neuheits-Claims-Sektion verlangt eine Webrecherche mit Widerlegungsziel. ^p0604

Review-Folie für eine bestehende Verification. Ein vorhandenes Dokument wird gegen die Vorlage gehalten, um zu prüfen, ob die Grundhaltung adversarial ist (Widerlegung als Ziel formuliert), ob das Verdikt-Vokabular geschlossen ist und Konsequenzen trägt, ob die menschliche Stufe als einzige statuserzeugende Instanz ausgewiesen ist, ob die Neuheits-Claims überhaupt geprüft werden und ob die Grenzen-Sektion existiert. ^p0605

#### Beispiel

kisug führt den strengsten Mechanismus des Bestands: adversariale Verifikation mit Anti-Anchoring (der Prüfer sieht nur Quellstelle und Behauptung), einem Zweitprüfer aus fremder Modellfamilie als Dekorrelation, Kalibrierung des Prüfers an Kontrollfällen mit bekannter Wahrheit und einem fünfstufigen Verdikt-Vokabular, in dem nur `stützt voll` den Status `verifiziert` erlaubt. FemPrompt führt das Fünf-Klassen-Befundvokabular mit direkter Migrationskonsequenz pro Klasse und eine persistierte Waitlist für offene Fälle; die Prüfkette läuft vom deterministischen Skript über die adversariale Maschinenprüfung zur bindenden menschlichen Stufe. szd-htr-ocr-pipeline führt das dreistufige Review-Modell als maschinenlesbaren JSON-Block im Pipeline-Output und benennt die Grenzen explizit (Agreement ist nicht Wahrheit, Ground-Truth-freie Verfahren messen Plausibilität). Alle drei teilen die Grundfigur: kontrolliertes Verdikt, Stufenkette mit menschlichem Abschluss, maschinenlesbare Persistenz. ^p0606

#### Begriffe

- Claim: eine außenwirksam verwendete empirische oder Neuheits-Behauptung des Projekts, die Einheit der Prüfung. ^p0607
- Prüfstand: die Referenzquelle, gegen die geprüft wird (Rohdaten, Volltexte, Ground Truth), im Frontmatter benannt. ^p0608
- Verdikt: ein Wert aus dem geschlossenen Ergebnis-Vokabular mit definierter Konsequenz für die Weiterverwendung. ^p0609
- Anti-Anchoring: Prüfanordnung, in der der Prüfer nur Quellstelle und Behauptung sieht, nicht die Begründung des Verfassers. ^p0610
- Migrationskonsequenz: die pro Verdikt festgelegte Folge für das geprüfte Artefakt (verwenden, nachbessern, sperren). ^p0611
- Bindungsregel: außenwirksame Claims dürfen nur in der Form verwendet werden, die die Verification lizenziert. ^p0612

#### Versionshistorie

- 0.2 (2026-08-21): Naming Contract übernommen. Einzelträger heißt `verification.md`, Spezialisierungen folgen `<subject>-verification.md`; Reports werden als datierte Snapshots referenziert. ^p0613
- 0.1 (2026-07-19): Erstfassung, empirisch extrahiert aus kisug, FemPrompt und szd-htr-ocr-pipeline; Neuheits-Claims-Sektion als nicht empirisch belegter Eigenbeitrag. Freigegeben am 2026-07-19. ^p0614

#### Related

- [Konvention Promptotyping Documents](#konvention-v0.1) ^p0615
- [Vorlage Testing](#promptotyping-document-testing) ^p0616
- [Vorlage Report](#promptotyping-document-report) ^p0617
- [Vorlage Journal](#promptotyping-document-journal) ^p0618

## Template `action-layer.md`: Vorlage Action-Layer

Source file `_content/promptotyping-document/action-layer.md`, template version 0.4. ^p0619

### Vorlage Action-Layer

Diese Vorlage strukturiert das Action-Dokument eines Promptotyping-Repos. Das resultierende Dokument heißt `CLAUDE.md` und liegt im Repo-Root, nicht im `knowledge/`-Ordner. Es sozialisiert den Coding-Agenten: imperative Regeln, die auf die deklarative Wissensbasis verweisen, plus ein klar abgegrenzter, austauschbarer Werkzeug-Block. Der Action-Layer trägt kein Wissen; er routet zu Wissen und übersetzt es in Imperative. Empirische Belegbasis: Action-Layer- und Journal-Praxis in Promptotyping-Repos 2026-06. ^p0620

#### Geltungsbereich

Die Vorlage trägt für jedes Promptotyping-Repo, weil die Funktion Agent Instructions in [Konvention Promptotyping Documents](#konvention-v0.1) als immer-relevant geführt wird. Sie trägt nicht für Forschungsleitstelle-Spezialdokumente (`RULES.md`, `INSTRUCTIONS.md`, `cloud-commands.md` für mehrere parallele Agenten mit differenzierten Rollen) und nicht für den Vault selbst. Bei einem anderen Coding-Agenten als Claude Code (Cursor, Gemini CLI) trägt der Methodenkern der Vorlage unverändert; nur der Werkzeug-Block wird gegen das tool-eigene Format (`.cursorrules`, `GEMINI.md`) getauscht. ^p0621

Lebenszyklus: die CLAUDE.md entsteht beim Repo-Setup, sobald die ersten Knowledge-Dokumente einschließlich `knowledge/handoff.md` stehen, aus denen der Methodenkern abgeleitet wird, und nie als leerer Platzhalter vorab. Aktualisiert wird sie, wenn sich Regeln, Wissensbasis-Struktur oder Werkzeug ändern; weil sie in jeder Session injiziert wird, ist Drift hier teurer als in jedem anderen Dokument und die Distillation-Regel zugleich die Destillat-Grenze, jede Zeile, die aus Code oder Wissensbasis ableitbar ist, wird gestrichen statt gepflegt. ^p0622

#### Funktion des Dokuments

CLAUDE.md ist der Action-Layer der Wissensbasis: imperativ, verhaltenssteuernd, vom Werkzeug bei jedem Sessionstart automatisch injiziert. Es beantwortet "wie soll der Agent sich in diesem Repo verhalten, auch ästhetisch". Adressiert ist ausschließlich der Coding-Agent; Menschen lesen `README.md` und `knowledge/`. Diagnoseraster der Konvention: formal falscher Output, Stilbruch, ignoriertes Verbot, hier prüfen. Inhaltlich falscher Output: Knowledge prüfen, nicht hier nachbessern. ^p0623

#### Strukturprinzipien

Drei Prinzipien tragen das Dokument. ^p0624

Erstens die Trennung von Methodenkern und Werkzeug-Block. Der Methodenkern ist portabel: Wissensbasis-Verweis mit Lesepfad, Handoff-Verarbeitung, Journal-Provenienz, CEIL-Prüfregeln, Designprinzipien, Scope-Negativliste, Wahrheitshierarchie. Der Werkzeug-Block ist austauschbar: Befehle, Hooks, Permissions, Stack-Konventionen, Security, maschinen- und plattformgebundene Details. Prüfkriterium: Wird der Werkzeug-Block gelöscht, muss der Methodenkern ohne Änderung in ein anderes Agent-Format übertragbar sein. Werkzeuggebundene Sätze im Methodenkern sind Fehler (sugw-Befund: "Keine Annahmen" neben `core.longpaths` in derselben Sektion). ^p0625

Zweitens Komposition statt Duplikation. `design.md` bleibt deklaratives Knowledge-Dokument; CLAUDE.md führt die imperative Übersetzung der Designhaltung und benennt `design.md` als Wertequelle. Dasselbe Prinzip gilt für alle volatilen Inhalte: Zahlen, Stände und Inventare werden auf ihre lebende Quelle verlinkt. Offene Eingänge liegen in `handoff.md`, angenommene Zukunftsarbeit in `plan.md` und Prüfresultate in `verification.md`. Die ästhetische und faktische Steuerung kommt aus der Komposition zweier Dokumente, nicht aus einem Hybriddokument. ^p0626

Drittens Distillation. CLAUDE.md ist ein knapper Pointer und trägt nur, was weder aus dem Code noch aus der Wissensbasis ableitbar ist. Jede Zeile kostet Kontextbudget in jeder Session. Referenzformulierungen aus der Praxis: "this file is the concise pointer" (mhdbdb-tei-only), "Prozessual, nicht dokumentarisch" (m3gim), "what is not derivable from the code alone" (HerData). ^p0627

#### Frontmatter-Schema

Abweichend von den `knowledge/`-Vorlagen trägt CLAUDE.md kein YAML-Frontmatter. Begründung: Das Dokument wird vom Werkzeug als roher Prompt-Kontext injiziert, und in der gesamten Belegbasis (35 Repos) führt keine einzige CLAUDE.md Frontmatter. Die Vorlagen-Provenienz steht stattdessen als HTML-Kommentar in der ersten Zeile: ^p0628

```markdown
<!-- template: Vorlage Action-Layer v0.4, https://dhcraft.org/Promptotyping/promptotyping-document/action-layer -->
```

Die kanonische Adresse ist der stabile Slug `action-layer` unter `/promptotyping-document/`, Latest-URL `https://dhcraft.org/Promptotyping/promptotyping-document/action-layer`. Die Frontmatter-Abweichung von der `template:`-Empfehlung der Konvention ist mit der Freigabe der Vorlage am 2026-07-19 ratifiziert. ^p0629

#### Abschnitte im Detail

##### Identität (Kopf)

Funktion: den Agenten in einem Absatz verorten. Inhalt: was das Projekt ist (ein Satz), Methode Promptotyping mit dem Kernsatz, dass die Documents in `knowledge/` das Domänenwissen und die Spezifikation halten, aus denen implementiert wird, Rollenverteilung Mensch/Agent, falls klärungsbedürftig (Critical Expert, Projektleiter, nicht Entwickler). Kein Marketing, keine Geschichte. ^p0630

##### Wissensbasis

Funktion: Routing in die Wissensbasis. Inhalt: Verweis auf `knowledge/` mit `INDEX.md` als Einstieg. Nach dem automatisch geladenen Action-Layer liest der Agent bei jedem Sessionstart `knowledge/INDEX.md`, anschließend `knowledge/handoff.md` und danach das aufgabenrelevante Declarative oder Action Document. `journal.md` wird für Entscheidungsgründe und nachgewiesene Übergänge gelesen. Bei mehr als drei Wissensdokumenten ergänzt eine Routing-Tabelle Aufgabe → Dokument den Lesepfad. Der Verweis muss auf repo-interne Quellen zeigen; ein Repo, dessen Methodenwissen nur in einem externen Vault liegt, ist für eine Session ohne Vault-Zugriff blind. ^p0631

##### Arbeitsregeln

Funktion: der portable Methodenkern als Regelliste. Die Regeln werden projektspezifisch konkretisiert: ^p0632

- Handoff-Verarbeitung. Bei jedem Sessionstart `knowledge/handoff.md` lesen. Vor der Nutzung eines Punkts Quelle und aktuelles Ziel prüfen, dauerhaften Inhalt zuerst in das zuständige Declarative oder Action Document integrieren, anschließend den Journal-Nachweis schreiben und den Punkt vollständig entfernen. ^p0633
- Journal-Provenienz. Ein Eintrag entsteht pro sachlich zusammengehörigem Übergang und verwendet `integriert`, `verworfen` oder `korrigiert`. Das Journal führt keinen aktuellen Projektstatus, keine offenen Aufgaben und keine ausführlichen Prüfresultate. ^p0634
- Journal-Verdichtung. Verdichten, wenn Wiederholungen, kopiertes Dauerwissen, erledigte Offenlisten, verstreute Entscheidungsgründe oder ein zu teurer regulärer Lesekontext die Provenienzfunktion beeinträchtigen. Die semantische Deckungsprüfung folgt [Vorlage Journal](#promptotyping-document-journal); ein Journal-Archiv wird nicht erzeugt. ^p0635
- Verifikation und CEIL. Keine erfundenen Werte, Begriffe oder Zitate; bei fehlendem Wissen nachfragen statt raten. Projektspezifische Checkpoints benennen: was wird wann dem Critical Expert vorgelegt, was läuft nie ohne Freigabe. Wo maschinelle Prüfungen existieren (Tests, Validierungsskripte, Datenverträge), sind sie als Pflichtlauf zu nennen. ^p0636
- Wahrheitshierarchie. Vorrangregel pro Konfliktklasse: welche Quelle ist kanonisch, welche abgeleitet (TEI vor JSON, Spec vor Code, Speicherstand vor Gedächtnis für Zahlen). Schlusssatz: niemals stillschweigend divergieren lassen, Widersprüche melden. ^p0637
- Quantitäten-Regel. Keine volatilen Zahlen in dieser Datei oder in Knowledge-Dokumenten; stattdessen die lebende Quelle benennen. ^p0638

##### Designprinzipien

Funktion: imperative Übersetzung der Designhaltung. Inhalt: `design.md` als Wertequelle benennen, Anweisung, vor UI- oder Textgenerierung das `design.md` zu lesen, dann drei bis sieben imperativ formulierte Sätze, die aus der Designhaltung abgeleitet sind. Entfällt nur, wenn das Projekt keine Design-Funktion hat (kein UI, keine gestalteten Texte). Die Prinzipien sind verbindlich formuliert ("Nutze Farbe nur funktional"), nicht beschreibend. ^p0639

##### Scope

Funktion: Negativliste gegen Feature-Drift und Werkzeug-Fehlgriffe. Inhalt: was das Projekt bewusst nicht tut, mit Verweis auf die geltende Entscheidung in `specification.md`, und was der Agent nicht tun soll. Auslassungen sind Designentscheidungen und werden als solche benannt. ^p0640

##### Bekannte Grenzen

Funktion: epistemischer Status, optional. Inhalt: ehrliche Grenzen von System, Modell oder Daten, die der Agent kennen muss, um Lücken nicht als Bugs zu behandeln; unbestätigte Inferenzen ausdrücklich als solche markiert, bis Klärung vorliegt. Keine Erfolgsprosa, keine Zahlen (Quantitäten-Regel gilt auch hier: qualitative Beschreibung plus Verweis auf die messende Quelle). ^p0641

##### Werkzeug (austauschbarer Block)

Funktion: alles Toolgebundene an genau einer Stelle, durch eine sichtbare Markierung vom Methodenkern getrennt. Inhalt in Untersektionen: ^p0642

- Befehle: Build, Tests, Pipeline-Schritte als konkrete Aufrufe, mit Angabe, wann sie Pflicht sind. ^p0643
- Konventionen: Stack-Festlegungen, Encoding, Plattform-Gotchas, Git-Regeln (Commit-Format, was nie ohne Aufforderung geschieht). ^p0644
- Security: nie `.env` lesen oder ausgeben, Secrets nur als Umgebungsvariablen, Datenschutzgrenzen für LLM-Dienste. ^p0645
- Hooks und Permissions: was `.claude/settings.json` mechanisch erzwingt, damit Regel und Mechanik nicht divergieren. ^p0646

Maschinengebundene absolute Pfade gehören, wenn überhaupt, nur hierher und werden als maschinengebunden markiert. Bei Portierung zu einem anderen Agenten wird ausschließlich dieser Block ersetzt. ^p0647

#### Was nicht reingehört

- Volatile Zahlen, Zählstände, Coverage-Werte, Datei-Inventare. Sie driften zwangsläufig; die lebende Quelle wird verlinkt, nicht kopiert. ^p0648
- Projektstatus-Erzählung und Sitzungsergebnisse. Der aktuelle Stand liegt in der projektspezifischen lebenden Statusquelle, angenommene Zukunftsarbeit in `plan.md`, offene Eingänge in `handoff.md`, Prüfresultate in `verification.md` und Übergangsnachweise in `journal.md`. ^p0649
- Deklaratives Domänen- und Architekturwissen. Das gehört in `knowledge/`; CLAUDE.md verweist. ^p0650
- Kompensatorische Bündelung. CLAUDE.md ist kein Ersatz für fehlende `project.md`, `architecture.md`, `design.md` oder `specification.md`. In den meisten untersuchten Repos absorbiert sie Charter, Architecture, Design oder ADR genau dann, wenn diese Dokumente fehlen; das ist ein Symptom fehlender Knowledge-Dokumente, kein eigener Inhalt. Sie routet und bindet, sie dupliziert keine Substanz. ^p0651
- Falscher Ort oder leerer Stub. CLAUDE.md gehört in den Repo-Root, nie in `knowledge/`, und wird nicht als leerer Platzhalter angelegt. Beides ist ein wiederkehrender Fehler (CLAUDE.md in `knowledge/` bei diged-neolat und grip; Leer-Stubs bei docta und kulturpool). ^p0652
- Spezifikation und Entscheidungen. Anforderungen und ADRs leben in `specification.md`; CLAUDE.md darf einzelne Entscheidungen als Regel zitieren, mit Verweis auf die Quelle. ^p0653
- Secrets, personenbezogene Daten, Modellpreise, hartkodierte Modellnamen im Methodenkern. ^p0654
- Inhalte für menschliche Leser. Die Datei ist Agent-Konfiguration; Nutzerdokumentation liegt in `README.md`. ^p0655

#### Vorlage zum Befüllen

Der folgende Block ist als Template gedacht. ^p0656

````markdown
<!-- template: Vorlage Action-Layer v0.4, https://dhcraft.org/Promptotyping/promptotyping-document/action-layer -->

### CLAUDE.md: [Projektname]

[Ein Absatz: was das Projekt ist, in einem Satz. Methode: Promptotyping, die Documents in `knowledge/` halten Domänenwissen und Spezifikation, aus denen implementiert wird. Rollenverteilung Mensch/Agent, falls klärungsbedürftig.]

#### Wissensbasis

Die Wissensbasis liegt in `knowledge/`. Lies nach diesem Action-Layer bei jedem Sessionstart zuerst `knowledge/INDEX.md`, anschließend `knowledge/handoff.md` und danach die aufgabenrelevanten Declarative oder Action Documents. Konsultiere `knowledge/journal.md`, wenn Herkunft oder Entscheidungsgründe eines Übergangs benötigt werden.

| Aufgabe | Lies zuerst |
|---|---|
| [Datenarbeit] | [`knowledge/data.md`] |
| [Anforderungen, Entscheidungen] | [`knowledge/specification.md`] |
| [UI, Gestaltung] | [`knowledge/design.md`] |
| [Offener Eingang oder Übergabe] | [`knowledge/handoff.md`] |
| [Herkunft oder Entscheidungsgrund unklar] | [`knowledge/journal.md`] |

#### Arbeitsregeln

- Handoff: Bei jedem Sessionstart `knowledge/handoff.md` lesen. Quelle und aktuelles Ziel jedes verwendeten Punkts prüfen, dauerhaften Inhalt zuerst integrieren, den Journal-Nachweis schreiben und den Punkt vollständig entfernen.
- Journal: Pro sachlich zusammengehörigem Übergang einen Eintrag vom Typ `integriert`, `verworfen` oder `korrigiert` schreiben. Aktuellen Projektstatus, offene Aufgaben und ausführliche Prüfresultate in ihren zuständigen Dokumenten halten.
- Verdichtung: Bei Funktionsverlust semantisch nach `knowledge/journal.md` verdichten, jede substantielle Aussage disponieren und kein Journal-Archiv erzeugen.
- Nichts erfinden: [projektspezifische Regel: welche Werte, Begriffe, Zitate nur aus welchen Quellen stammen dürfen]. Bei fehlendem Wissen nachfragen, nicht raten.
- Checkpoints: [was wird wann dem Critical Expert vorgelegt; was läuft nie ohne Freigabe; welche Prüfläufe sind Pflicht].
- Wahrheitshierarchie: Bei Widerspruch gilt [kanonische Quelle] vor [abgeleiteter Quelle]. [Weitere Vorrangregeln.] Niemals stillschweigend divergieren lassen, Widersprüche melden.
- Keine volatilen Zahlen in dieser Datei oder in Knowledge-Dokumenten. Aktuelle Zahlen → [lebende Quelle]. Zukunftsarbeit → `knowledge/plan.md`. Offene Eingänge → `knowledge/handoff.md`. Prüfresultate → `knowledge/verification.md`.

#### Designprinzipien

Wertequelle: `knowledge/design.md`. Vor UI- oder Textgenerierung lesen. Verbindlich:

- [Prinzip 1, imperativ formuliert, aus design.md abgeleitet]
- [Prinzip 2]
- [Prinzip 3]

#### Scope

Was dieses Projekt nicht tut:

- [bewusste Auslassung mit Verweis auf die Entscheidung in specification.md oder journal.md]

Was du nicht tun sollst:

- [rote Linie 1, z.B. keine destruktiven Git-Operationen ohne Auftrag]
- [rote Linie 2]

#### Bekannte Grenzen

[Optional. Grenzen von System, Modell oder Daten, qualitativ beschrieben. Unbestätigte Inferenzen als solche markieren, bis Klärung vorliegt.]

#### Werkzeug (austauschbarer Block: Claude Code)

<!-- Toolgebunden. Bei Portierung zu einem anderen Agenten wird nur dieser Block ersetzt; alles oberhalb bleibt unverändert. -->

##### Befehle

- Build/Pipeline: [`befehl`]
- Tests: [`befehl`], [wann Pflicht, z.B. vor jedem Commit]
- [weitere]

##### Konventionen

- [Stack-Festlegungen, Encoding, Plattform-Gotchas]
- Git: [Commit-Regeln; was nie ohne explizite Aufforderung geschieht]

##### Security

- Nie `.env` lesen oder ausgeben; Secrets nur als Umgebungsvariablen.
- [Datenschutzregel: welche Daten dürfen in LLM-Dienste, welche nicht]

##### Hooks und Permissions

[Falls vorhanden: was `.claude/settings.json` mechanisch erzwingt. Maschinengebundene Pfade nur hier, als maschinengebunden markiert.]
````

#### Anwendung als Prompt-Template

Erzeugung beim Repo-Setup. Der Agent liest [Konvention Promptotyping Documents](#konvention-v0.1) und die vorhandene Wissensbasis, legt `knowledge/handoff.md` an, kopiert das Template und befüllt den Methodenkern aus den Knowledge-Dokumenten. Designprinzipien werden aus `design.md` imperativ übersetzt, die Wahrheitshierarchie aus der Dokumentstruktur abgeleitet und Scope-Grenzen aus `specification.md` übernommen. Wo die Wissensbasis eine Lücke lässt, fragt der Agent. ^p0657

Review-Folie für eine bestehende CLAUDE.md. Geprüft wird die Trennung von Methodenkern und Werkzeug-Block, die Sessionstart-Reihenfolge über `INDEX.md` und `handoff.md`, die Integrationsreihenfolge vor dem Journal-Nachweis, die semantische Journal-Verdichtung sowie die Verweise auf lebende Quellen. Außerdem werden Routing-Tabelle und Wissensbasis gegeneinander geprüft. ^p0658

Portierung. Beim Wechsel des Coding-Agenten wird der Werkzeug-Block durch das tool-eigene Pendant ersetzt; der Methodenkern wird unverändert übernommen. Parallele tool-spezifische Zwillingsdateien werden aus derselben Quelle erzeugt, nicht doppelt gepflegt. ^p0659

#### Beispiel

m3gim eröffnet seine CLAUDE.md mit der Selbstbeschränkung "Workflow-Regeln für Claude-Code-Sessions. Prozessual, nicht dokumentarisch. Für Dokumentation siehe `knowledge/`" und verankert die Spec-Hierarchie als Wahrheitsordnung vor jeder Änderung. zbz-ocr-tei kodiert die Wissensbasis-Disziplin als oberste Regel ("Wissen in `knowledge/`: nicht in CLAUDE.md duplizieren. Single Source of Truth pro Fakt") und führt Journal-Pflicht, Security und Commands als getrennte Sektionen. Beide zeigen den Pointer-Charakter; zbz-ocr-tei zeigt zugleich die Grenze: eine zu umfangreiche CLI-Referenz im Action-Layer erzeugt Drift-Wellen bei jeder Pipeline-Änderung. ^p0660

#### Begriffe

- Action-Layer: das imperative Dokument im Repo-Root, das den Agenten sozialisiert; analytischer Typ Action neben Knowledge und Process. ^p0661
- Methodenkern: der portable Teil des Action-Layers (Wissensbasis-Routing, Handoff-Verarbeitung, Journal-Provenienz, CEIL-Regeln, Designprinzipien, Scope, Wahrheitshierarchie), unabhängig vom konkreten Coding-Agenten. ^p0662
- Werkzeug-Block: der austauschbare, toolgebundene Teil (Befehle, Hooks, Permissions, Security, Plattform-Konventionen). ^p0663
- Komposition: das Prinzip, dass ästhetische und faktische Steuerung aus dem Verweis eines Action-Dokuments auf ein Knowledge-Dokument entsteht (design.md → CLAUDE.md), nicht aus einem Hybridtyp. ^p0664
- Drift: Auseinanderlaufen von CLAUDE.md und Realität (Code, Daten, Wissensbasis); häufigstes Fehlerbild des Dokumenttyps, primär verursacht durch duplizierte volatile Inhalte. ^p0665

#### Versionshistorie

- 0.4 (2026-08-21): `handoff.md` in den Sessionstart aufgenommen. Journal-Pflicht auf sachlich zusammengehörige Übergänge und semantische Verdichtung umgestellt. ^p0666
- 0.3 (2026-07-24): Identitäts-Kernsatz auf die Beschreibung des `knowledge/`-Ordners umgestellt, nachdem die Rangbehauptung (Documents als primäres Artefakt, Code als regenerierbares Nebenprodukt) zurückgenommen wurde. Bestehende Repos ziehen den Kopfabsatz beim nächsten Anfassen der CLAUDE.md nach. ^p0667
- 0.2 (2026-07-19): Freigabe (status complete), englisches Funktionsvokabular (Agent Instructions), Lebenszyklus-Absatz, Frontmatter-Abweichung ratifiziert. Keine Migrationspflicht für bestehende Repos. ^p0668
- 0.1 (2026-06-09): Erstfassung, empirisch destilliert aus 35 Repos (Action-Layer- und Journal-Praxis in Promptotyping-Repos 2026-06). ^p0669

#### Related

- [Vorlagen Promptotyping Documents](#vorlagen) ^p0670
- [Konvention Promptotyping Documents](#konvention-v0.1) ^p0671
- [Promptotyping](#ueberblick) ^p0672
- Agent-Sozialisierung ^p0673
- Knowledge-Action-Komposition ^p0674
- Action-Layer- und Journal-Praxis in Promptotyping-Repos 2026-06 ^p0675
- [Vorlage Design](#promptotyping-document-design) ^p0676
- [Vorlage Journal](#promptotyping-document-journal) ^p0677
- [Vorlage Handoff](#promptotyping-document-handoff) ^p0678
- Context Engineering ^p0679

## Template `journal.md`: Vorlage Journal

Source file `_content/promptotyping-document/journal.md`, template version 0.4. ^p0680

### Vorlage Journal

Diese Vorlage strukturiert den kuratierten rückwärtsgerichteten Provenienzindex einer Promptotyping-Wissensbasis. Das resultierende Dokument heißt `journal.md`, liegt im `knowledge/`-Ordner und weist sachlich zusammengehörige Übergänge nach. Die aktuellen Inhalte bleiben in ihren zuständigen Declarative, Action und Process Documents. ^p0681

#### Geltungsbereich

Die Vorlage trägt für jedes aktive Promptotyping-Projekt. `journal.md` entsteht mit dem ersten nachweiswürdigen Übergang, führt dauerhaft `status: active` und bleibt am Projektende als Provenienzindex erhalten. Einträge entstehen nach integrierten, verworfenen oder korrigierten Übergängen sowie selten nach einer semantischen Verdichtung. ^p0682

Das Journal wird verdichtet, sobald Wiederholungen, kopiertes Dauerwissen, erledigte Offenlisten, verstreute Entscheidungsgründe oder ein zu teurer regulärer Lesekontext seine Provenienzfunktion beeinträchtigen. Seine Länge oder die Zahl der Einträge löst allein keine Verdichtung aus. ^p0683

#### Funktion des Dokuments

Das Journal beantwortet, welcher sachliche Übergang aus welcher Quelle in welches Ziel führte und welches Ergebnis angenommen, verworfen oder korrigiert wurde. Es ist ein kuratierter Provenienzindex für Menschen und Agents, die Herkunft oder Entscheidungsgrund einer aktuellen Aussage prüfen. ^p0684

Der aktuelle Projektstatus liegt in der projektspezifischen lebenden Quelle. Dauerhafte Sach- und Handlungsinhalte liegen in Declarative oder Action Documents, angenommene Zukunftsarbeit in `plan.md`, offene Eingänge in `handoff.md` und ausführliche Prüfresultate in `verification.md`. Git bewahrt frühere Wortlaute. ^p0685

#### Strukturprinzipien

Erstens entsteht ein Eintrag pro sachlich zusammengehörigem Übergang. Sessiongrenzen erzeugen keinen eigenen Eintrag, wenn sie keinen solchen Übergang abschließen. ^p0686

Zweitens führt jeder Eintrag genau einen inhaltlichen Typ. `integriert` weist die Übernahme in ein kanonisches Ziel nach. `verworfen` nennt den geprüften Gegenstand und den Verwerfungsgrund. `korrigiert` referenziert die frühere Aussage und weist die gültige Korrektur nach. Der seltene Wartungstyp `verdichtet` nennt den bearbeiteten Bereich und den Git-Ausgangsstand. ^p0687

Drittens folgt der Journal-Nachweis der dauerhaften Integration. Bei einem Handoff-Punkt werden zuerst Quelle und aktuelles Ziel geprüft, anschließend wird der dauerhafte Inhalt integriert oder begründet verworfen. Danach entsteht der Journal-Eintrag und der Punkt wird aus `handoff.md` entfernt. ^p0688

Viertens verdichtet das Journal semantisch. Jede substantielle Aussage des Vorgängerstands erhält eine Disposition, nämlich behalten, in ein kanonisches Ziel integrieren, begründet verwerfen oder ausschließlich über Git bewahren. Eine temporäre Deckungsliste sichert diese Prüfung und wird danach entfernt. ^p0689

#### Frontmatter-Schema

Das Journal folgt dem Pflichtkern aus [Konvention Promptotyping Documents](#konvention-v0.1). Spezifisch für die Provenance-Funktion gelten folgende Felder. ^p0690

- `status:` ist immer `active`. ^p0691
- `related:` enthält mindestens `handoff` und typischerweise `project` sowie `specification`. ^p0692
- `topics:` und `knowledge-sources:` entfallen üblicherweise. ^p0693
- `updated:` wird nach einem neuen Eintrag oder einer Verdichtung angepasst. ^p0694

#### Abschnitte im Detail

##### Lead

Der Lead benennt die Funktion als kuratierten rückwärtsgerichteten Provenienzindex und verweist auf die Zuständigkeit der Geschwister-Dokumente für aktuelle Inhalte. ^p0695

##### Einträge

Die Einträge stehen in konsistenter chronologischer Ordnung. Die Überschrift enthält Datum, Typ und Gegenstand. Der Inhalt nennt Quelle, Ziel und Ergebnis. Ein Verwerfungsgrund ersetzt bei `verworfen` das Zielergebnis; `korrigiert` referenziert zusätzlich die frühere Aussage. ^p0696

##### Verdichtungsnachweis

Ein `verdichtet`-Eintrag nennt Bereich, Git-Ausgangsstand und Ergebnis. Vor der Verdichtung muss ein sauberer Git-Ausgangsstand vorliegen. Pfade, Anker und Hashes werden gegen den resultierenden Stand geprüft. Die temporäre Deckungsliste wird nach der Prüfung gelöscht. ^p0697

#### Was nicht reingehört

- Aktueller Projektstatus und offene Aufgaben. ^p0698
- Angenommene Zukunftsarbeit, sie liegt in `plan.md`. ^p0699
- Offene Übergabepunkte, sie liegen in `handoff.md`. ^p0700
- Ausführliche Prüfresultate, sie liegen in `verification.md`. ^p0701
- Kopien von dauerhaftem Sachwissen oder Handlungsregeln. ^p0702
- Sessionprotokolle, Code-Diffs und vollständige Commit-Messages. ^p0703
- Starre Verdichtungsschwellen, ein Fenster der jüngsten Einträge oder ein `journal-archive.md`. ^p0704

#### Vorlage zum Befüllen

````markdown
---
title: Journal
project:
  name: [Projektname]
  repository: [Repository-URL]
method:
  name: Promptotyping
  url: https://lisa.gerda-henkel-stiftung.de/digitale_geschichte_pollin
status: active
language: [de | en]
version: [Repo-Schema-Version]
created: [YYYY-MM-DD]
updated: [YYYY-MM-DD]
authors: [Autor 1, Autor 2]
generated-with: [Harness (LLM), falls relevant]
template:
  name: Vorlage Journal
  version: 0.4
  url: https://dhcraft.org/Promptotyping/promptotyping-document/journal
  alias: https://dhcraft.org/Promptotyping/#promptotyping-document-journal
related: [project, specification, handoff]
---

### Journal

Dieses Journal ist der kuratierte rückwärtsgerichtete Provenienzindex des Projekts. Aktuelle Sach- und Handlungsinhalte stehen in den zuständigen Declarative oder Action Documents, Zukunftsarbeit in `plan.md`, offene Eingänge in `handoff.md` und Prüfresultate in `verification.md`.

#### Einträge

<!-- Ein Eintrag pro sachlich zusammengehörigem Übergang. Zulässige Inhaltstypen sind integriert, verworfen und korrigiert. Verdichtet ist ein seltener Wartungstyp. -->

##### YYYY-MM-DD integriert [Gegenstand]

- Quelle: [überprüfbarer Pfad, Nachricht oder Commit]
- Ziel: [kanonisches Declarative oder Action Document]
- Ergebnis: [knapper Nachweis der Integration]

##### YYYY-MM-DD verworfen [Gegenstand]

- Quelle: [überprüfbarer Pfad, Nachricht oder Commit]
- Ziel: [geprüftes kanonisches Ziel]
- Verwerfungsgrund: [fachlicher, technischer oder wissenschaftlicher Grund]

##### YYYY-MM-DD korrigiert [Gegenstand]

- Quelle: [frühere Aussage und neue Evidenz]
- Ziel: [kanonisches Dokument mit gültiger Fassung]
- Ergebnis: [Korrektur und ihre Auswirkung]

<!-- Seltener Wartungseintrag nach semantischer Verdichtung:

##### YYYY-MM-DD verdichtet [Bereich]

- Vorgängerstand: [Git-Commit oder anderer eindeutiger Git-Ausgangsstand]
- Bereich: [geprüfte Einträge oder Sektionen]
- Ergebnis: [behaltene, integrierte, verworfene und ausschließlich über Git bewahrte Aussagen]
-->
````

#### Anwendung als Prompt-Template

Bei einem sachlich zusammengehörigen Übergang wird zuerst der dauerhafte Zielinhalt aktualisiert. Danach ergänzt der Agent den passenden Journal-Eintrag. Für einen Handoff-Punkt folgt anschließend dessen vollständige Entfernung aus `handoff.md`. ^p0705

Eine Verdichtung beginnt auf einem sauberen Git-Ausgangsstand. Der Agent erstellt vorübergehend eine Deckungsliste aller substantiellen Aussagen und weist jeder Aussage eine Disposition zu. Nach der Übernahme werden Pfade, Anker und Hashes geprüft. Die Deckungsliste wird entfernt und ein `verdichtet`-Eintrag referenziert den Vorgängerstand. Ein Archivdokument entsteht dabei nicht. ^p0706

Der Review prüft, ob jeder Eintrag einen sachlichen Übergang abbildet, ob aktueller Status, Zukunftsarbeit, offene Eingänge und Prüfdetails an ihren zuständigen Orten liegen und ob jeder Verdichtungsnachweis einen überprüfbaren Vorgängerstand nennt. ^p0707

#### Beispiel

Ein offener Handoff-Punkt liefert eine neue Schemainvariante. Nach Prüfung wird die Variante in `data-schema.md` integriert. Das Journal erhält einen Eintrag vom Typ `integriert` mit Quelle, Ziel und Ergebnis; anschließend wird der Handoff-Punkt entfernt. ^p0708

#### Begriffe

- Provenienzindex: kuratierte Rückwärtsreferenz auf sachliche Übergänge und ihre überprüfbaren Quellen. ^p0709
- Disposition: Entscheidung für eine substantielle Aussage bei der Verdichtung, nämlich behalten, integrieren, verwerfen oder ausschließlich über Git bewahren. ^p0710
- Vorgängerstand: sauberer Git-Ausgangsstand, gegen den eine Verdichtung vollständig geprüft wird. ^p0711

#### Versionshistorie

- 0.4 (2026-08-21): Journal als kuratierten Provenienzindex gefasst. Inhaltstypen, Handoff-Reihenfolge und semantische Verdichtung ohne Archiv normiert. ^p0712
- 0.2 (2026-07-19): Englisches Funktionsvokabular (Provenance), Block-Status auf `active`, Lebenszyklus-Absatz. ^p0713
- 0.1 (2026-05-09): Erstfassung. ^p0714

#### Related

- [Vorlagen Promptotyping Documents](#vorlagen) ^p0715
- [Konvention Promptotyping Documents](#konvention-v0.1) ^p0716
- [Promptotyping](#ueberblick) ^p0717
- Context Engineering ^p0718
- [Vorlage Handoff](#promptotyping-document-handoff) ^p0719
- [Vorlage Plan](#promptotyping-document-plan) ^p0720
- [Vorlage Verification](#promptotyping-document-verification) ^p0721

## Template `handoff.md`: Vorlage Handoff

Source file `_content/promptotyping-document/handoff.md`, template version 0.1. ^p0722

### Vorlage Handoff

Diese Vorlage strukturiert die verpflichtende Process Inbox eines Promptotyping-Projekts. Das resultierende Dokument heißt `handoff.md`, liegt im `knowledge/`-Ordner und führt ausschließlich offene Übergabepunkte. Ein leerer Zustand bleibt als gültige Inbox bestehen. ^p0723

#### Geltungsbereich

Die Vorlage trägt für jedes Promptotyping-Projekt. `knowledge/handoff.md` entsteht beim Repo-Setup, führt dauerhaft `status: active` und wird bei jedem Sessionstart nach dem Action-Layer und `knowledge/INDEX.md` gelesen. Das Dokument bleibt am Projektende als leere Inbox bestehen oder wird mit der gesamten Wissensbasis archiviert. ^p0724

Datierte außergewöhnliche Übergaben können zusätzlich als `<scope>-handoff-YYYY-MM-DD.md` unter `handoffs/` liegen. Sie dokumentieren einen eingefrorenen Übergabestand und ersetzen die Process Inbox nicht. Dauerhafte Research-to-Operations-Kontrakte folgen [Vorlage Integration](#promptotyping-document-integration). ^p0725

#### Funktion des Dokuments

Das Handoff-Dokument beantwortet, welche übernommenen Deltas noch geprüft, integriert oder verworfen werden müssen. Die Anwesenheit eines Punkts bedeutet offen. Quelle und aktuelles Ziel werden vor jeder Nutzung geprüft. ^p0726

#### Strukturprinzipien

Erstens führt die Inbox ausschließlich offene Punkte. Ein Punktstatus und eine Closed-Sektion würden denselben Zustand doppelt kodieren und entfallen. ^p0727

Zweitens besitzt jeder Punkt genau die Pflichtfelder `Received`, `Source`, `Target` und `Context`. `Evidence`, `Next action`, `Blocker` und `Operator point` werden nur geführt, wenn sie Inhalt tragen. Leere optionale Felder werden gelöscht. ^p0728

Drittens integriert die Bearbeitung dauerhaften Inhalt zuerst in das zuständige Declarative oder Action Document. Danach erhält `knowledge/journal.md` einen knappen Nachweis mit Gegenstand, Quelle, Ziel und Ergebnis oder Verwerfungsgrund. Der bearbeitete Punkt wird anschließend vollständig entfernt. ^p0729

#### Frontmatter-Schema

Der Template-Block verwendet den Pflichtkern aus [Konvention Promptotyping Documents](#konvention-v0.1). Der Status ist immer `active`. Zusätzliche empfohlene Felder der Konvention dürfen ergänzt werden; ein verpflichtendes `function:`-Feld wird nicht eingeführt. ^p0730

#### Abschnitte im Detail

##### Lead

Der Lead benennt die Inbox-Funktion und die Verarbeitungsreihenfolge. Er hält fest, dass Quelle und aktuelles Ziel geprüft, dauerhafte Inhalte integriert, das Journal nachgezogen und erledigte Punkte entfernt werden. ^p0731

##### Offene Handoff-Punkte

Die Sektion enthält entweder den exklusiven Empty State „Keine offenen Handoff-Punkte.“ oder einen oder mehrere offene Punkte. Für einen Punkt wird der Empty State entfernt. Nach Bearbeitung des letzten Punkts wird er wieder eingesetzt. ^p0732

#### Was nicht reingehört

- Dauerhaftes Sachwissen, Spezifikationen oder Handlungsregeln. Sie liegen im zuständigen Declarative oder Action Document. ^p0733
- Angenommene Zukunftsarbeit. Sie liegt in `plan.md`. ^p0734
- Erledigte Punkte, Punktstatus und Closed-Sektionen. Den Nachweis führt `journal.md`, frühere Wortlaute bewahrt Git. ^p0735
- Datierte außergewöhnliche Übergabe-Snapshots. Sie liegen unter `handoffs/`. ^p0736
- Dauerhafte Schnittstellen- und Research-to-Operations-Kontrakte. Sie folgen der Integration-Funktion. ^p0737

#### Vorlage zum Befüllen

````markdown
---
title: Handoff
project:
  name: [Projektname]
  repository: [Repository-URL]
method:
  name: Promptotyping
  url: https://lisa.gerda-henkel-stiftung.de/digitale_geschichte_pollin
status: active
created: [YYYY-MM-DD]
updated: [YYYY-MM-DD]
---

### Handoff

Diese Process Inbox führt ausschließlich offene Übergabepunkte. Prüfe vor der Nutzung die Quelle und das aktuelle Ziel. Integriere dauerhaften Inhalt in das zuständige Declarative oder Action Document, dokumentiere Gegenstand, Quelle, Ziel und Ergebnis oder Verwerfungsgrund knapp in `knowledge/journal.md` und entferne den bearbeiteten Punkt anschließend vollständig.

#### Offene Handoff-Punkte

Keine offenen Handoff-Punkte.

<!--
##### [Kurzer Gegenstand]

- Received: [YYYY-MM-DD]
- Source: [Repo, Lane, Dokument oder Nachricht mit überprüfbarem Verweis]
- Target: [aktuelles Declarative oder Action Document]
- Context: [für Prüfung und Integration erforderlicher Zusammenhang]
- Evidence: [optional]
- Next action: [optional]
- Blocker: [optional]
- Operator point: [optional]
-->
````

#### Anwendung als Prompt-Template

Beim Repo-Setup wird der Block als `knowledge/handoff.md` angelegt. Beim Eingang einer Übergabe prüft der Agent zuerst `Source` und `Target`, übernimmt nur den noch offenen Delta-Kontext und entfernt optionale Felder ohne Inhalt. Nach der fachlichen Verarbeitung schreibt er dauerhafte Inhalte an ihren kanonischen Ort, ergänzt den Journal-Nachweis und löscht den Punkt. ^p0738

Der Review prüft den exklusiven Empty State, die vier Pflichtfelder jedes offenen Punkts, die Abwesenheit leerer optionaler Felder sowie die vollständige Entfernung erledigter Punkte. Ein datierter Snapshot unter `handoffs/` wird als ergänzendes Artefakt behandelt. ^p0739

#### Beispiel

Eine neue Wissensbasis beginnt mit dem Empty State. Eine Übergabe aus einer parallelen Lane ersetzt diesen Satz durch genau einen Punkt. Nach Prüfung und Integration steht wieder „Keine offenen Handoff-Punkte.“; das Journal weist den Übergang nach. ^p0740

#### Begriffe

- Process Inbox: fortlaufendes Process Document für noch offene, übernommene Deltas. ^p0741
- Handoff-Punkt: kleinste sachlich zusammengehörige Übergabeeinheit mit überprüfbarer Quelle und aktuellem Ziel. ^p0742
- Research-to-Operations-Handoff: dauerhafter Vertrag zwischen Forschung und Betrieb, der als Declarative Integration Document geführt wird. ^p0743

#### Versionshistorie

- 0.1 (2026-08-21): Erstfassung als verpflichtende Process Inbox mit exklusivem Empty State und Integrationsnachweis im Journal. ^p0744

#### Related

- [Vorlagen Promptotyping Documents](#vorlagen) ^p0745
- [Konvention Promptotyping Documents](#konvention-v0.1) ^p0746
- [Vorlage Index](#promptotyping-document-index) ^p0747
- [Vorlage Integration](#promptotyping-document-integration) ^p0748
- [Vorlage Action-Layer](#promptotyping-document-action-layer) ^p0749
- [Vorlage Journal](#promptotyping-document-journal) ^p0750

## Template `report.md`: Vorlage Report

Source file `_content/promptotyping-document/report.md`, template version 0.3. ^p0751


### Vorlage Report

Diese Vorlage strukturiert den menschlich kuratierten Projektstatusbericht für einen externen Adressaten. Das resultierende Dokument heißt `<scope>-report-YYYY-MM-DD.md` und liegt unter `snapshots/`. Scope und Datum machen Berichtsgegenstand und Stichtag bereits im Suchtreffer sichtbar. Aus der externen Audience und dem Snapshot-Charakter folgen Lebenszyklus, Struktur und Stil. Die ausführliche Begründung der Funktion liegt in der Konvention Report Document. ^p0752

#### Geltungsbereich

Die Vorlage trägt, sobald ein Projektstand an einen externen Empfänger kommuniziert werden muss: Auftraggeber, Förderer, Stakeholder. Bei Auftragsprojekten ist das der Regelfall, weil Kundinnen und Kunden einen Arbeitsbericht erhalten. Sie entfällt bei reinen Eigenforschungs-Repos ohne externen Berichtsadressaten und bei Tool-Repos ohne Auftragskontext. Sie trägt nicht für interne Stand-Notizen; diese leben im `journal.md`. ^p0753

Der Naming Contract trennt den kuratierten Report von maschinell erzeugten Prüf- und Vollständigkeitsberichten. Kuratierte Berichte tragen Scope, Funktion und Datum. Generierte Berichte liegen unter `generated/` oder einem in `INDEX.md` erklärten domänenspezifischen Ausgabeordner. Ein generisches `report.md` oder `status.md` wird für neue kuratierte Berichte nicht verwendet. ^p0754

#### Funktion des Dokuments

Das Dokument beantwortet einem Dritten ohne Repo-Vorwissen vier Fragen am Stück: was wurde im Berichtszeitraum getan, wo steht das Projekt am Stichtag, welche belastbaren Ergebnisse liegen vor, was geschieht als Nächstes. Adressiert ist ein identifizierbarer externer Empfänger; das unterscheidet den Report von allen anderen Promptotyping-Dokumenten, deren Adressat der Coding-Agent oder das Projekt selbst ist. ^p0755

Abgrenzung gegen `journal.md`: nicht der Inhalt unterscheidet, sondern Lebenszyklus und Kuratierungsgrad. Das Journal trägt fortlaufende, chronologische Einträge für interne Adressaten; der Report ist ein einziger, redaktionell verdichteter Stand ohne Verlaufslogik für externe Adressaten. Der Report zitiert aus dem Journal, das Journal verweist nicht auf den Report. Abgrenzung gegen `project.md`: dort steht zeitlos „Was ist dieses Projekt?", im Report steht „Wie steht es am Stichtag X?". ^p0756

#### Strukturprinzipien

Drei Prinzipien tragen das Dokument, und alle drei kehren bewusst die internen Promptotyping-Prinzipien um, weil der Adressat ein anderer ist. ^p0757

Erstens sind volatile Quantitäten erlaubt und erwünscht. Verarbeitungsstände (X von Y dokumentiert), Genauigkeitswerte (CER, Precision, Recall), Datenmengen, Stundenzahlen gehören in einen Report, weil der eingefrorene Stand genau diese Zahlen ist. Die Regel gegen volatile Quantitäten gilt für Wissens-, Strategie- und Überblicksdokumente, nicht für Snapshots; der Report fällt unter die Snapshot-Ausnahme. ^p0758

Zweitens sind Tabellen liberaler einsetzbar als das Fließprosa-Default. Eine Tabelle für Meilensteine, Deliverables oder Pipeline-Stufen ist für die Stand-Kommunikation oft das ehrlichere Mittel als ein Absatz, weil der Leser den Status zeilenweise prüfen kann. ^p0759

Drittens entfällt die negative Selbstdefinition. Ein externer Adressat erwartet, dass kommuniziert wird, was geleistet wurde, nicht was bewusst ausgespart bleibt. Wo Auslassungen relevant sind (out of scope, geplant aber nicht umgesetzt), gehören sie in „Offene Punkte" und „Ausblick", nicht in eine eigene Negationssektion. ^p0760

Jede inhaltliche Behauptung über fertige Arbeit ist belegbar: über einen Pfad ins Repo, eine URL oder einen Commit-Ref. Das ist nicht Dekoration, sondern der Mechanismus, der den Bericht als korrekten Stand zum Zeitpunkt X tragfähig macht. Erhebt der Bericht empirische Befunde oder Neuheitsansprüche (Genauigkeitswerte, erstmalige Verfahren), verweist er auf das `verification.md` des Projekts ([Vorlage Verification](#promptotyping-document-verification)), in dem diese Claims adversarial gegen die Rohdaten geprüft sind; ein außenwirksamer Claim ohne Verifikationsverweis ist eine Behauptung. ^p0761

#### Lebenszyklus

Der Report trägt `status: snapshot`, weil sein Inhalt ab Erstellung bewusst veraltet. Der Stichtag steht im Dateinamen und im Dokument. Ein sachlich neuer Berichtsstand erzeugt eine neue datierte Datei. Korrekturen am selben eingefrorenen Stand bleiben über git nachvollziehbar. Ein Git-Tag kann zusätzlich das gesamte Repo am Berichtsdatum markieren, wenn Report, Code, Daten und Knowledge Documents gemeinsam referenzierbar bleiben müssen. ^p0762

Mehrere Adressaten oder Genres erhalten eigene Scope-Werte, etwa `funder-interim-report-2026-08-21.md` und `client-final-report-2026-08-21.md`. `report-genre:` hält die kontrollierte Gattung unabhängig von der Sprache des Dateinamens. ^p0763

#### Frontmatter-Schema

Das Dokument folgt dem Frontmatter-Schema aus der [Konvention Promptotyping Documents](#konvention-v0.1) (Pflichtkern: `title, project, method, status, created, updated`; `template:` empfohlen), erweitert um drei adressaten-bezogene Felder: ^p0764

- `audience:` verschachtelt mit `type` (`client`, `funder`, `stakeholder`, `public`) und `name` (Adressatenbezeichnung). Der entscheidende Marker, der den Report von allen anderen Promptotyping-Dokumenten unterscheidet. ^p0765
- `report-period:` verschachtelt mit `from` und `to` (Berichtszeitraum). ^p0766
- `report-genre:` kontrolliertes Vokabular: `zwischenbericht`, `abschlussbericht`, `stakeholder-update`. ^p0767

`topics:` entfällt typischerweise; der Report trägt keine domänen-thematische Verortung im Vault-Sinn. `knowledge-sources:` entfällt; der Report verweist auf die internen Knowledge-Dokumente, nicht auf externe Anschlüsse. ^p0768

#### Abschnitte im Detail

##### Identifikation

Funktion: den eingefrorenen Stand referenzierbar machen. Inhalt: Projekt, Berichtszeitraum, Adressat, Datum, Autor. Ohne diese fünf Angaben ist ein Stand nicht zitierbar. Steht am Anfang, kurz, gegebenenfalls als Kopf-Tabelle. ^p0769

##### Tätigkeiten im Berichtszeitraum

Funktion: dokumentieren, was geleistet wurde. Inhalt: in Abschlussberichten der gesamte Projektverlauf, in Zwischenberichten der aktuelle Abschnitt. Sachlich, belegbar, ohne Verlaufsdramaturgie. ^p0770

##### Status quo

Funktion: den Stand am Stichtag beschreiben. Inhalt: was ist fertig, was ist in Arbeit, was steht aus. Der Kern der eingefrorenen Aussage. Eine Status-Tabelle (Komponente, Stand, Beleg) ist hier oft das ehrlichste Mittel. ^p0771

##### Ergebnisse

Funktion: die belastbaren Outputs listen. Inhalt: Repository, Edition, Pipeline, Daten, Publikationen. Jedes Ergebnis ist über Pfad, URL oder Commit-Ref nachprüfbar. ^p0772

##### Offene Punkte und nächste Schritte

Funktion: benennen, was nach dem Stichtag folgt. Inhalt: in Abschlussberichten als Ausblick formuliert, in Zwischenberichten als Plan für den nächsten Abschnitt. Hier gehören auch relevante Auslassungen hin (out of scope, geplant aber nicht umgesetzt). ^p0773

##### Anhang mit Belegen

Funktion: Nachweise bündeln, optional. Inhalt: sinnvoll bei Förder- und Auftragsberichten, in denen Stundenzahlen, Meilensteine oder Deliverables-Listen verlangt sind. ^p0774

Zwischen- und Abschlussbericht unterscheiden sich in der Gewichtung: Zwischenberichte betonen Status quo und nächste Schritte, Abschlussberichte betonen Tätigkeiten und Ergebnisse und schließen mit Ausblick. ^p0775

#### Schreibweise

Selbsterklärend für jemanden ohne Repo-Vorwissen. Fachbegriffe (TEI, OCR-Engine, NER, CER, DTA-Basisformat) werden beim ersten Auftreten erklärt oder verlinkt; ein Glossar am Ende ist akzeptabel, wenn die Begriffsdichte hoch ist. Kein internes Jargon ohne Auflösung: projekteigene Abkürzungen, interne Codenamen, Insider-Verweise auf Sitzungen oder Personen werden für den externen Leser übersetzt oder weggelassen. Stil sachlich, neutral, präzise, ohne Dramatisierung oder emotionalisierende Attribute. ^p0776

#### Was nicht reingehört

- Interne Stand-Notizen und Sessionchronik. Diese leben im `journal.md`; der Report verdichtet daraus, kopiert nicht. ^p0777
- Negative Selbstdefinition als eigene Sektion. Relevante Auslassungen gehören in „Offene Punkte" und „Ausblick". ^p0778
- Unbelegte Behauptungen über fertige Arbeit. Jede solche Aussage trägt einen Pfad, eine URL oder einen Commit-Ref. ^p0779
- Internes Jargon ohne Auflösung. ^p0780

#### Vorlage zum Befüllen

Der folgende Block ist als Template gedacht. ^p0781

````markdown
---
title: "Projektbericht [Projektname] – [Berichtszeitraum]"
project:
  name: [Projektname]
  repository: [Repository-URL]
status: snapshot
language: [de | en]
version: [Repo-Schema-Version]
created: [YYYY-MM-DD]
updated: [YYYY-MM-DD]
authors: [Autor 1, Autor 2]
generated-with: [Harness (LLM), falls relevant]
method:
  name: Promptotyping
  url: https://lisa.gerda-henkel-stiftung.de/digitale_geschichte_pollin
template:
  name: Vorlage Report
  version: 0.3
  url: https://dhcraft.org/Promptotyping/promptotyping-document/report
  alias: https://dhcraft.org/Promptotyping/#promptotyping-document-report
audience:
  type: [client | funder | stakeholder | public]
  name: [Adressatenbezeichnung]
report-period:
  from: [YYYY-MM-DD]
  to: [YYYY-MM-DD]
report-genre: [zwischenbericht | abschlussbericht | stakeholder-update]
---

<!-- Identifikation: Projekt, Berichtszeitraum, Adressat, Datum, Autor. Kurz, ggf. als Kopf-Tabelle. -->

[Identifikations-Block]

#### Tätigkeiten im Berichtszeitraum

<!-- Was wurde geleistet. Abschlussbericht: ganzer Verlauf. Zwischenbericht: aktueller Abschnitt. Belegbar. -->

[...]

#### Status quo

<!-- Stand am Stichtag: fertig, in Arbeit, ausstehend. Status-Tabelle oft am ehrlichsten. -->

[...]

#### Ergebnisse

<!-- Belastbare Outputs. Jedes über Pfad, URL oder Commit-Ref nachprüfbar. -->

[...]

#### Offene Punkte und nächste Schritte

<!-- Was nach dem Stichtag folgt. Abschlussbericht: Ausblick. Zwischenbericht: Plan. Relevante Auslassungen hier. -->

[...]

#### Anhang

<!-- Optional. Belege, Stundenzahlen, Meilenstein- und Deliverables-Listen bei Förder- und Auftragsberichten. -->

[...]
````

#### Anwendung als Prompt-Template

Strukturanker beim Erstellen eines Berichts. Der Agent erhält den Template-Block und befüllt ihn aus `journal.md` (Tätigkeiten), `specification.md` (Stand der Anforderungen und Entscheidungen), den Ergebnis-Artefakten im Repo (Pfade, Commits) und dem aktuellen Datenstand. Volatile Zahlen werden hier ausdrücklich aus den lebenden Quellen übernommen, nicht aus dem Gedächtnis. Der Bericht wird vor Versand vom Critical Expert gegen den echten Repo-Stand geprüft (Critical Expert in the Loop). ^p0782

Review-Folie für einen bestehenden Bericht. Ein vorhandener `<scope>-report-YYYY-MM-DD.md` wird gegen die Vorlage gehalten, um Naming, Identifikation, Belegbarkeit, Begriffserklärung und Übereinstimmung mit dem referenzierten Repo-Zustand zu prüfen. ^p0783

#### Beispiel

Das Promptotyping-Methodik-Repo führt den früheren Lane-Bericht als `snapshots/paper-zfdg-submission-report-2026-07-23.md`. Der Pfad signalisiert die Artefaktklasse, der Scope benennt Paper und Einreichkontext, das Datum fixiert den Stand. Inhaltliche Behauptungen verweisen auf die damaligen Repo-Pfade und Commit-Refs. ^p0784

#### Begriffe

- Report: menschlich kuratierter Projektstatusbericht für einen externen Adressaten, der einen Stand zum festen Zeitpunkt einfriert. ^p0785
- Audience: der externe Empfänger des Berichts; der Marker, der den Report von allen anderen Promptotyping-Dokumenten unterscheidet. ^p0786
- Snapshot-Serie: Folge eigenständiger, datierter Reports, deren Scope und Stichtag im Dateinamen sichtbar sind. ^p0787
- Berichtsgenre: Gattung des Berichts (Zwischenbericht, Abschlussbericht, Stakeholder-Update), die Gewichtung und Lebenszyklus prägt. ^p0788

#### Versionshistorie

- 0.3 (2026-08-21): Naming Contract übernommen. Reports liegen als datierte Snapshots unter `snapshots/` und führen Scope, Funktion und Datum im Dateinamen. Generische `report.md`- und `status.md`-Träger entfallen für neue kuratierte Berichte. ^p0789
- 0.2 (2026-07-19): Freigabe (status complete), Block-Status auf `snapshot` (neu registriertes Vokabular), Verification-Verweis für außenwirksame Claims. Keine Migrationspflicht für bestehende Repos. ^p0790
- 0.1 (2026-06-13): Erstfassung, Rationale in der Konvention Report Document. ^p0791

#### Related

- [Konvention Promptotyping Documents](#konvention-v0.1) ^p0792
- [Vorlage Verification](#promptotyping-document-verification) ^p0793
- [Vorlage Journal](#promptotyping-document-journal) ^p0794
- [Vorlage Projekt-Wissensdokument](#promptotyping-document-project) ^p0795
