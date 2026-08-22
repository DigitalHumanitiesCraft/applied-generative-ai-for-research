---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/distillation-preserved-uncertainty-and-negative-findings]]", "[[30_assertions/early-interfaces-make-a-model-discussable-through-operations]]", "[[30_assertions/exploration-determines-what-the-knowledge-base-must-represent]]", "[[30_assertions/exploration-scales-through-computational-profiling]]", "[[30_assertions/interaction-exposes-unwarranted-precision]]", "[[30_assertions/models-shift-the-cost-of-project-specific-implementation]]", "[[30_assertions/preparation-assembles-an-accessible-source-basis]]", "[[30_assertions/prompt-borne-metadata-can-enter-a-transcription]]", "[[30_assertions/the-four-forms-of-work-recur-without-a-fixed-order]]", "[[30_assertions/the-material-document-carries-epistemic-responsibility]]", "[[30_assertions/user-stories-bridge-scholar-centred-design-and-implementation]]"]
posits: 0
lang: de
part: "IV. Promptotyping"
chapter: 13
title: "Preparation und Exploration"
topic: "[[Promptotyping]]"
feeding-sources: ["paper chapter 2", "script chapter 7", "Promptotyping document templates"]
working-title: true
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Preparation und Exploration

## Preparation

Promptotyping beginnt damit, zusammenzutragen, wovon die Arbeit ausgehen wird. Preparation bringt das einschlägige Forschungsmaterial in eine zugängliche Projektumgebung und macht dessen aktuellen Stand explizit, was für die meisten Projekte heißt, Quellenmaterial und Forschungsdaten zusammen mit den Standards, Schemata und Domänendokumentationen zu sammeln, die sie beschreiben, dazu die Forschungsfragen und die Editions- oder Mapping-Richtlinien, die ihre Behandlung regeln, die bereits vorhandene Software und die bereits artikulierten Anforderungen.[^1]

Die Anforderung dieser Phase ist schwächer, als sie zunächst wirkt. Preparation verlangt nicht, dass das Material normalisiert, formal modelliert oder direkt in den Arbeitskontext eines Agents gelegt wird. Sie verlangt, dass es für Prüfung und computationelle Nutzung zugänglich bleibt und dass Provenienz und bekannte Grenzen dokumentiert sind.[^1] Analoges Material muss unter Umständen zuerst digitalisiert werden, und digitales Material darf über heterogene Formate und Strukturierungsgrade verteilt bleiben, ohne die Phase zu blockieren. Preparation ist vorläufig hinreichend, sobald Quellenbasis und Forschungskontext digital zugänglich und so weit dokumentiert sind, dass eine systematische Untersuchung möglich wird.[^1]

Was das Materialdokument der Wissensbasis später tragen muss, entscheidet sich bereits hier. Pro Quelle hält es Herkunft, Erfassungslogik, Lizenz, Provenienz und Erfassungszeitraum fest, und wo mehrere Quellen zusammenkommen, erklärt es deren Verhältnis, weil die prüfende Person, die die Datenqualität beurteilen soll, der Agent, der die Daten verarbeiten soll, und die fachwissenschaftliche Person, die die Auswahllogik nachvollziehen will, gleichermaßen von diesem Nachweis abhängen.[^2] In der Preparation werden die Angaben dafür gesammelt, auch wenn das Schreiben zur Distillation gehört.

Requirements Engineering gehört in diese Phase, weil sich ein Artefakt nicht unabhängig von den wissenschaftlichen Tätigkeiten spezifizieren lässt, die es stützen soll. Die narrative Form einer Anforderung benennt Rolle, Ziel und Nutzen, entsteht in Sitzungen mit Fachleuten während Preparation und Exploration und wird iterativ verfeinert; ihr formales Gegenstück ist eine festgehaltene Erwartung an das System in prüfbarer Sprache mit einem Akzeptanzkriterium.[^3] Beide Formen zu führen erlaubt, wissenschaftliche Praxis und Systemverhalten aneinander zu prüfen, statt die eine aus der anderen abzulesen.

## Exploration

Exploration untersucht das vorbereitete Material, um seine Struktur und seine Grenzen zu verstehen und zu bestimmen, was die Projektwissensbasis repräsentieren muss.[^4] Ihre Frage ist nicht, ob sich eine Oberfläche bauen lässt. Sie fragt, was die Daten tragen und was nicht, welche Unterscheidungen tatsächlich repräsentiert sind, welche Annahmen implizit bleiben, welche weitere Modellierung nötig wäre, welche visuellen oder computationellen Formen das Material verzerren würden und welche alternativen Repräsentationen einen Vergleich verdienen.

Die Form der Arbeit richtet sich nach dem Umfang des Materials. Ein einzelner Text oder eine kleine Sammlung lässt sich direkt untersuchen, auch mit einem Sprachmodell, wo das hilft, während große oder heterogene Sammlungen computationelles Profiling verlangen, etwa Code, der strukturelle Information über Tausende kodierter Dokumente extrahiert und aggregiert.[^5] Die daraus folgende Arbeitsteilung ist ausdrücklich festzuhalten. Die Sammlung bleibt in der Projektumgebung und wird von prüfbaren Operationen verarbeitet, während die entstehenden Profile und ausgewählte Beispiele in den Arbeitskontext des Agents eingehen.[^5]

Exploration greift auch über vorläufige Artefakte in das Material. Rasch entwickelte Oberflächen erlauben Projektbeteiligten, Information in einer gemeinsamen operativen Umgebung einzugeben, anzuzeigen, zu filtern und zu vergleichen, statt ein Modell nur über Schemata und abstrakte Beschreibungen zu diskutieren, und Kategorien, Relationen und Erfassungsanforderungen bleiben dabei revidierbar.[^6] Interaktion dieser Art hat gezeigt, wo Unterscheidungen vom verfügbaren Material getragen wurden, wo Kategorien mehrdeutig blieben, wo bei der Erfassung zusätzliche Information oder Qualifizierung nötig war und wo eine technisch mögliche Visualisierung ein Maß an Präzision, Vollständigkeit oder Sicherheit unterstellt hätte, das die Daten nicht decken.[^7]

Dieselbe Phase fördert Befunde über die Verarbeitungsanordnung statt über das Material zutage. In einem dokumentierten Workflow wurde Kontextinformation aus vorhandenen kodierten Datensätzen in den Prompt eingefügt, der jedes Manuskriptbild begleitete, und ein kontrollierter Vergleich zeigte danach, dass reichere Metadaten Information aus dem Prompt in eine Transkription tragen konnten, auch wo diese Information im Bild nicht sichtbar war.[^8] Ein solcher Befund steht nur einem Projekt zur Verfügung, das die eigene Anordnung prüft und nicht bloß deren Ergebnisse.

## Der Status dessen, was Exploration hervorbringt

Was Exploration liefert, ist vorläufig. Ihre Ergebnisse sind Beobachtungen und noch kein gepflegtes Projektwissen, und sie gehen erst über Interpretation und Distillation in die Wissensbasis ein.[^4] Dasselbe gilt für die Vorschläge, die ein Modell in dieser Phase erzeugt. Sie vergrößern den Möglichkeitsraum und werden als Hypothesen behandelt, während die Bewertung gegen Quellen, Datenmodell, Forschungskontext und disziplinäre Praxis bei der Fachwissenschaft bleibt.[^9]

Exploration ist vorläufig hinreichend, sobald das Material so weit verstanden und dokumentiert ist, dass sich bestimmen lässt, was weitergetragen werden muss. Zwei Eigenschaften ihrer Ergebnisse gehen an diesem Übergang leicht verloren. Unsicherheit und negative Befunde gehören in den gepflegten Bericht, einschließlich der Phänomene, die das verfügbare Referenzmaterial nicht repräsentiert und daher als Vergleichsgrundlage nicht tragen kann, und die dokumentierten Workflows haben genau das bewahrt, statt unvollständige Evidenz in scheinbar geklärte Anforderungen zu überführen.[^10]

Die Phasen sind wiederkehrend statt sequenziell, dieser Übergang ist also kein einmal passiertes Tor. Befunde aus der Implementation führen die Arbeit in die Exploration zurück, sobald sich eine Annahme als ungedeckt erweist, und in die Preparation, sobald sich eine Quelle ändert oder ein Schema als unvollständig herausstellt.[^11]

## Gaps
- Die Hands-on-Kette des Skriptums, die diese Phase begleitet, gehört zur parallelen Schreiblane, sodass das Kapitel kein schrittweises Profiling-Beispiel und kein Übungsmaterial führt.
- Personas, Epics, Szenarien und Akzeptanzkriterien sind in der Gliederung als Instrumente der Preparation genannt. Verankert sind hier nur User Stories und formale Anforderungen, weil die Vorlagen Personas als eigenes Artefakt behandeln und das Paper sie nicht erörtert.
- Anomalieerkennung und der Vergleich von Schema und Korpus sind in der Gliederung als Explorationstechniken genannt. Die Quellen beschreiben computationelles Profiling allgemein, sodass die einzelnen Techniken auf der allgemeinen Assertion ruhen und nicht auf eigenen Quellstellen.

[^1]: Grounded in [[30_assertions/preparation-assembles-an-accessible-source-basis]].
[^2]: Grounded in [[30_assertions/the-material-document-carries-epistemic-responsibility]].
[^3]: Grounded in [[30_assertions/user-stories-bridge-scholar-centred-design-and-implementation]].
[^4]: Grounded in [[30_assertions/exploration-determines-what-the-knowledge-base-must-represent]].
[^5]: Grounded in [[30_assertions/exploration-scales-through-computational-profiling]].
[^6]: Grounded in [[30_assertions/early-interfaces-make-a-model-discussable-through-operations]].
[^7]: Grounded in [[30_assertions/interaction-exposes-unwarranted-precision]].
[^8]: Grounded in [[30_assertions/prompt-borne-metadata-can-enter-a-transcription]].
[^9]: Grounded in [[30_assertions/models-shift-the-cost-of-project-specific-implementation]].
[^10]: Grounded in [[30_assertions/distillation-preserved-uncertainty-and-negative-findings]].
[^11]: Grounded in [[30_assertions/the-four-forms-of-work-recur-without-a-fixed-order]].
