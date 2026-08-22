---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/agentic-capability-arises-from-the-compound-system]]", "[[30_assertions/automation-claims-are-self-descriptions]]", "[[30_assertions/capability-evaluations-measure-different-things]]", "[[30_assertions/harness-quality-changes-what-can-be-evaluated]]", "[[30_assertions/model-choice-is-a-system-choice]]", "[[30_assertions/probabilistic-and-deterministic-operations-combine]]", "[[30_assertions/the-harness-is-the-technical-layer-of-action]]", "[[30_assertions/the-harness-supplies-no-scholarly-authority]]", "[[30_assertions/tool-use-changes-the-epistemic-structure]]", "[[30_assertions/vision-language-models-fail-plausibly]]"]
posits: 3
lang: de
part: "I. Generative Modelle als Forschungssysteme"
chapter: 2
title: "Modelle, Werkzeuge und generative Systeme"
topic: "[[Generative-Models]]"
feeding-sources: ["script chapter 2", "slide section AI Agents"]
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Modelle, Werkzeuge und generative Systeme

## Der Gegenstand der Beurteilung

Ein großes Sprachmodell arbeitet selten allein. Gegenwärtige Forschungsanwendungen verbinden ein Basismodell mit Systeminstruktionen, Retrieval-Mechanismen, externen Werkzeugen, Codeausführung, Gedächtnis, Oberflächen und Zugriff auf lokale oder entfernte Dateien, und die Leistungsfähigkeit, über die ein Projekt tatsächlich verfügt, folgt aus diesem Verbund. Die Quellen dieses Buches formulieren den Punkt allgemein so, dass agentische Leistungsfähigkeit aus dem Zusammenspiel von Modell, Harness und Umgebung entsteht und nicht aus dem Modell für sich, sodass die isolierte Beurteilung eines Modells etwas anderes misst als das, was ein Projekt damit tun kann.[^1]

Die Folge für die Forschung ist eine Frage der Benennung. Wenn eine Untersuchung berichtet, ein Modell habe eine Aufgabe gelöst, betrifft die Aussage meist einen Verbund, dessen übrige Bestandteile nicht beschrieben wurden. Zwei Läufe mit demselben Modell in verschiedenen Umgebungen können weiter auseinanderliegen als zwei Läufe mit verschiedenen Modellen in derselben Umgebung, und keiner dieser Unterschiede wird sichtbar, wo nur das Modell genannt ist.[^13]

## Was das Harness ist

Die technische Schicht, über die ein Agent Kontext erhält, Werkzeuge aufruft, auf Dateien zugreift, Programme ausführt und Rückmeldungen verarbeitet, ist das AI Harness. Es verwaltet Zustand, Zugriffsrechte und Kontrollfluss und legt fest, welche Ordner gelesen oder verändert werden dürfen, welche Befehle ohne Bestätigung laufen, wie Werkzeugausgaben in den Kontext zurückgelangen, wie lange ein Lauf fortgesetzt wird, wann ein Mensch einbezogen werden muss und wie Zwischenergebnisse gespeichert werden.[^2] Jede dieser Festlegungen entscheidet, was eine spätere Leserin des Laufs rekonstruieren kann, und macht das Harness damit zum Teil der evidenziellen Anordnung statt zu einer Bequemlichkeitsschicht darum herum.

Seine Qualität verändert, was überhaupt beurteilt werden kann. Ein leistungsfähiges Modell in einem schwachen Harness kann die Folgen seiner eigenen Handlungen weder prüfen noch verifizieren, während Werkzeuge, Tests, persistenter Zustand und gestaltete Rückmeldung das Gesamtsystem leistungsfähiger und inspizierbarer machen, als eine Modellbewertung vermuten ließe. Ein Harness, das Ausführungsspuren, Testergebnisse und Fehlerinformationen bewahrt, hinterlässt eine Trajektorie, die jemand fortsetzen oder korrigieren kann, der nicht dabei war.[^3]

Die Grenze ist ebenso bestimmt. Ein Validator kann feststellen, dass ein Element an einer Stelle zulässig ist, und nicht entscheiden, ob die Quelle tatsächlich unleserlich ist oder ob eine andere Lesung wahrscheinlicher wäre, und eine Ebene höher gilt dasselbe für die Umgebung insgesamt. Sie kann begrenzen und aufzeichnen, was geschieht, und sie bestimmt nicht, welches Projektwissen relevant oder welche Modellierungsentscheidung angemessen ist.[^4] Kapitel 3 entwickelt, was daraus folgt, und Teil III kehrt zu dieser Grenze als der Linie zurück, um die agentische Arbeit herum organisiert wird.

## Was Werkzeuge verändern

Werkzeuge erweitern einen Textgenerator zu einem System, das auf eine Umgebung einwirken kann. Dateizugriff, Terminal, Codeausführung, Suche, Datenbanken, Browser, Validatoren und spezialisierte Schnittstellen gehören dazu, und am meisten tragen jene, die Evidenz über die Folgen einer Handlung zurückgeben. Ein Compiler, eine Testsuite oder ein Schema-Validator beantwortet eine Frage, die das Modell sonst über sich selbst beantworten würde, und das verändert die epistemische Struktur des Workflows, weil das System sich nicht mehr allein auf erzeugten Text stützt und Beobachtungen gewinnen kann, die seinen nächsten Schritt einschränken.[^5]

Multimodale Verarbeitung ist ein Fall, in dem diese Erweiterung ein spezifisches Risiko mitbringt. Ein Vision Language Model verarbeitet visuelle und sprachliche Information in derselben Aufgabe, sodass ein Allzwecksystem ein Faksimile zusammen mit einer Anweisung erhalten und eine Transkription liefern kann, ohne ein dediziertes Erkennungssystem zu sein. Visuelle Muster, Layout, sprachlicher Kontext und Anweisung prägen die Ausgabe gemeinsam, woraus die charakteristische Fehlerform entsteht, eine Lesung, die zum Satz passt und nicht zur Seite. Ob die daraus folgende Fähigkeit bei unbekannten Handschriften als emergent zu gelten hat, hängt von der Definition von Emergenz, vom Maßstab und von nicht offengelegten Trainingsdaten ab.[^6]

Produktiv ist die Anordnung, die beide Arten von Operation verbindet, statt zwischen ihnen zu wählen. Eine Tabelle zu erkennen, ein Layout zu deuten oder Werte aus verrauschtem Material zu ziehen kann probabilistisches Verhalten verlangen, und sobald die Werte explizit repräsentiert sind, lassen sich ihre Beziehungen deterministisch nachrechnen. Das wiederkehrende Muster führt von probabilistischer Deutung über eine strukturierte Repräsentation zu deterministischer Prüfung, und Invarianten wie Zeilen- und Spaltensummen decken innere Inkonsistenz auf, ohne zu beweisen, dass die Quelle richtig gelesen wurde.[^7] Das ist das kleinste vollständige Beispiel der Anordnung, die dieses Buch insgesamt beschreibt, und Kapitel 5 gibt ihm seine allgemeine Form als Trennung zwischen dem, worüber das Modell liest, und dem, was der Code liest.

## Ein System wählen

Weil der Verbund die Einheit ist, heißt ein Modell wählen ein System wählen. Systeme unterscheiden sich in Leistungsfähigkeit, Modalitäten, Inferenzkosten, Latenz, Offenheit, Deployment-Optionen, Kontextkapazität, Werkzeugnutzung und den Harnesses, über die sie betrieben werden können, und eine allein an Benchmarkwerten getroffene Entscheidung legt alle übrigen Eigenschaften stillschweigend mit fest.[^8] Ein Projekt, das lokale Ausführung braucht oder einen in fünf Jahren wiederholbaren Lauf, entscheidet über Deployment und Erhaltung, während es scheinbar über Qualität entscheidet.

Die Evaluationen selbst sperren sich gegen Aggregation. Messungen zur Aufgabendauer, zur Anpassung an unbekannte Probleme, zum mathematischen Schließen und zum Verhalten in ausführbaren Umgebungen beantworten verschiedene Fragen, und sie auf eine Skala zu ziehen verwirft, wozu jede gebaut wurde.[^9] Öffentliche Aussagen von Frontier-Laboren zur Automatisierung von Forschung gehören noch einmal in eine andere Kategorie. Sie halten die Richtung fest, in die ein Labor Fähigkeiten auszudehnen versucht, und sie sind kein Beleg dafür, dass Forschung automatisiert wäre.[^10]

Für ein Forschungsprojekt folgt daraus ein bescheidenes Verfahren. Zu benennen ist, von welchen Eigenschaften des Verbunds die Arbeit abhängt, diese Eigenschaften sind direkt zu prüfen, und Fähigkeitsberichte sind als Evidenz über die Bedingungen zu lesen, unter denen sie entstanden sind.[^11]

## Lücken

Zwei der Themen, die die Gliederung diesem Kapitel zuweist, decken die Quellen dieser Arbeitslinie nicht ab, ein drittes nur teilweise.[^12]
- Retrieval-augmented Generation nennt die Gliederung, und in den Quellen erscheint davon nur die allgemeine Beobachtung, dass externe Ressourcen während der Inferenz Information beisteuern können; das Kapitel formuliert deshalb die Ebenenunterscheidung und nicht die Retrieval-Architektur. Vor einer Behandlung des Themas ist eine Quelle zu Retrieval-Systemen nötig.
- Proprietäre Infrastruktur und Reproduzierbarkeit, von der Gliederung hier vorgesehen, hat in den drei Quellen gar keinen Anker. Das Promptotyping-Paper der anderen Manuskriptlinie behandelt Rekonstruierbarkeit, und Kapitel 23 trägt das Thema; bis dessen Destillat vorliegt, ersetzt ein Querverweis die Behandlung an dieser Stelle.
- Persistentes Gedächtnis und gespeicherter Nutzerkontext erscheinen in den Quellen nur als Teil der allgemeinen Liste dessen, was ein Harness verwaltet, ohne Beschreibung, wie sich Gedächtnis über Sitzungen hinweg verändert.

[^1]: Grounded in [[30_assertions/agentic-capability-arises-from-the-compound-system]].
[^2]: Grounded in [[30_assertions/the-harness-is-the-technical-layer-of-action]].
[^3]: Grounded in [[30_assertions/harness-quality-changes-what-can-be-evaluated]].
[^4]: Grounded in [[30_assertions/the-harness-supplies-no-scholarly-authority]].
[^5]: Grounded in [[30_assertions/tool-use-changes-the-epistemic-structure]].
[^6]: Grounded in [[30_assertions/vision-language-models-fail-plausibly]].
[^7]: Grounded in [[30_assertions/probabilistic-and-deterministic-operations-combine]].
[^8]: Grounded in [[30_assertions/model-choice-is-a-system-choice]].
[^9]: Grounded in [[30_assertions/capability-evaluations-measure-different-things]].
[^10]: Grounded in [[30_assertions/automation-claims-are-self-descriptions]].
[^11]: Posit: das Verfahren folgt aus den vorangehenden Assertions und steht in keiner Quelle. Open evidence question: ob Projekte, die es übernehmen, anders entscheiden als Projekte, die Benchmarktabellen lesen, was eine Untersuchung dokumentierter Modellentscheidungen prüfen könnte.
[^12]: Posit: die Lückenliste ist das Urteil der Autorenschaft darüber, was dieses Kapitel nicht tragen kann. Open evidence question: ob das Destillat des Promptotyping-Papers die Reproduzierbarkeitslücke schließt oder sie nur nach Kapitel 23 verschiebt.
[^13]: Posit: der Vergleich zwischen zwei Läufen in verschiedenen Umgebungen und zwei Modellen in einer Umgebung ist ein Schluss aus der Verbund-Assertion und in keiner Quelle gemessen. Open evidence question: eine Studie, die Modell und Harness unabhängig voneinander variiert und dieselbe Forschungsaufgabe stellt.