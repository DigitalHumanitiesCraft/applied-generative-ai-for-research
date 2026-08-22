---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/agent-to-agent-protocols-address-a-second-surface]]", "[[30_assertions/agentic-engineering-organises-multi-step-work]]", "[[30_assertions/checking-a-run-covers-behaviour-data-and-requirements]]", "[[30_assertions/harness-quality-changes-what-can-be-evaluated]]", "[[30_assertions/increments-must-stay-inspectable]]", "[[30_assertions/independent-review-extends-coverage-not-authority]]", "[[30_assertions/instruction-files-are-context-not-enforcement]]", "[[30_assertions/least-privilege-and-reversibility-bound-the-run]]", "[[30_assertions/model-routing-separates-functions]]", "[[30_assertions/more-agents-raise-coordination-cost]]", "[[30_assertions/plans-stay-compact-and-revisable]]", "[[30_assertions/skills-package-procedure-with-progressive-disclosure]]", "[[30_assertions/specification-precedes-implementation]]", "[[30_assertions/subagents-bound-context-and-parallelise]]", "[[30_assertions/the-mechanisms-are-not-interchangeable]]", "[[30_assertions/the-organisation-requirements-are-explicit]]", "[[30_assertions/the-workspace-is-part-of-the-method]]", "[[30_assertions/tool-protocols-solve-integration-not-relevance]]"]
posits: 3
lang: de
part: "III. Agentische Forschungsarbeit"
chapter: 9
title: "Agentic Engineering als Arbeitsorganisation"
topic: "[[Agentic-Work]]"
feeding-sources: ["script chapter 6", "slide sections Agentic Engineering and Workflows"]
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Agentic Engineering als Arbeitsorganisation

## Die Definition und ihre Reichweite

Agentic Engineering ist die systematische Organisation und Kontrolle mehrschrittiger agentischer Arbeit. Es umfasst die Abgrenzung und Zerlegung von Aufgaben, die Werkzeugnutzung, die Verarbeitung von Zwischenergebnissen, Zustände und Übergaben, Abbruch- und Eskalationsbedingungen sowie Prüfung und Fortführung, und seine zentrale Frage lautet, unter welchen Bedingungen die Handlungen eines Agenten nachvollziehbar, begrenzt und korrigierbar bleiben. Sein Gegenstand reicht über Code hinaus auf Datenbeschreibungen, Spezifikationen, Mappings, Designentscheidungen, Prozessdokumente und Verifikationskonzepte.[^1]

Die organisatorischen Anforderungen sind ausdrücklich und nicht emergent. Aufgaben müssen begrenzt und zerlegt, Werkzeuge, Berechtigungen und Abbruchbedingungen festgelegt, Zwischenergebnisse geprüft und bei Bedarf eskaliert und der Projektzustand über Schritte hinweg verständlich gehalten werden, womit agentische Leistungsfähigkeit zu einer neuen Gestaltungsfläche wird, auf der Kontext, Zustand, Werkzeuge, Kontrolle und Bewertung über die Zeit koordiniert werden.[^2] Menschliche Arbeit wird dabei umverteilt und nicht entfernt. Was sich verschiebt, ist der Punkt, an dem ein Mensch handelt, von der Ausführung jedes Implementierungsschritts hin zur Aufbereitung von Wissen, zur Zielformulierung, zur Zerlegung der Arbeit, zur Vergabe von Berechtigungen, zur Prüfung von Zwischenständen und zur Verifikation der Ergebnisse.[^3]

## Vor der Ausführung

Die Arbeit beginnt vor der ersten inhaltlichen Anweisung. Die erste Entscheidung betrifft den Ort, an dem das Modell arbeiten wird, das Vorbereitete bestimmt, welche Dateien, Werkzeuge, Wissensbestände und Rückmeldungsformen später verfügbar sind, und die Vorbereitungsphase erzeugt einen persistenten und nachvollziehbaren Bestand mit dokumentierter Provenienz und unveränderten Quelldateien, sodass die spätere Arbeit nicht bei null beginnt.[^4]

Zwischen exploratives Gespräch und Implementation tritt dann eine ausdrückliche Spezifikation. Anforderungen, User Stories, Datenbedingungen, Schnittstellen und Prüfkriterien vor der eigentlichen Implementation zu entwickeln verringert die stillschweigende Deutung, die an den Agenten delegiert wird, und schafft einen Gegenstand, der geprüft werden kann, bevor Code entsteht, und dieselbe Disziplin zeigt der Arbeitsprompt, der zuerst ein konzeptionelles Vorgehen und einen kompakten Plan verlangt und den Agenten anhält, nach allem zu fragen, was er nicht zuverlässig ableiten kann, statt still anzunehmen.[^5]

Die Planung hat eine eigene Fehlerform. Ein Plan soll bestimmen, welche Teilprobleme vorliegen, welche Informationen fehlen, welche Werkzeuge nötig sind, welche Prüfungen vorgesehen sind und welche Reihenfolge sinnvoll ist, und ein umfangreicher Plan vor der Untersuchung des Bestandes erzeugt falsche Sicherheit, sodass ein brauchbarer Plan kompakt, gegen den aktuellen Zustand prüfbar und revidierbar ist.[^6]

## Grenzen des Laufs

Zwei Grenzen werden dem gesetzt, was ein Agent tun darf. Ein Werkzeugaufruf kann den Projektzustand verändern, sodass Zugriff nach dem Prinzip der geringsten erforderlichen Berechtigung vergeben wird, und das konkrete Muster liest Quelldateien, ohne sie zu überschreiben, erlaubt Änderungen an erzeugten Dateien in einem Arbeitsordner, lässt Validatoren ohne Bestätigung laufen, verlangt für Veröffentlichungsschritte eine ausdrückliche Freigabe und hält Änderungen versioniert und reversibel.[^7]

Die Grenze muss durchgesetzt und nicht beschrieben werden. Eine Instruktionsdatei ist Kontext und keine Garantie, und Verhaltensanleitung ist etwas anderes als Berechtigungen und Hooks, die eine Grenze unabhängig von der Befolgung halten können.[^8] Ein Projekt, das seine Grenzen in ein Dokument schreibt und uneingeschränkten Zugriff gewährt, hat eine Policy beschrieben und keine umgesetzt.[^9]

## Inkremente und ihre Prüfung

Mehrschrittige Arbeit läuft in prüfbaren Inkrementen. Ein brauchbarer Zwischenstand ist ausführbar oder untersuchbar, einem definierten Projektzustand zuordenbar, gegen Anforderungen prüfbar und klein genug, dass die Ursache eines Fehlers rekonstruierbar bleibt, und Pläne, Entscheidungen, Prüfergebnisse und offene Fragen gehören in persistente Projektartefakte und nicht in den Chatverlauf.[^10] Die Prüfung eines erzeugten Artefakts umfasst, ob es läuft, ob die Daten korrekt eingelesen und dargestellt werden, ob die vereinbarten Anforderungen umgesetzt sind und ob die Quelldateien unverändert geblieben sind, und das letzte davon ist eine Eigenschaft des Laufs und nicht des Artefakts.[^11]

Inspizierbar wird all das zum Teil durch die Umgebung. Ein Harness, das Ausführungsspuren, Testergebnisse und Fehlerinformationen bewahrt, hinterlässt eine Trajektorie, die jemand fortsetzen oder korrigieren kann, der nicht dabei war, während ein leistungsfähiges Modell in einem schwachen Harness die Folgen seiner eigenen Handlungen nicht prüfen kann.[^12]

## Mechanismen und ihre Arbeitsteilung

In heutigen Agentensystemen kehren mehrere Mechanismen wieder, und sie als austauschbare Etiketten zu behandeln verdeckt die eigentliche Gestaltungsentscheidung, nämlich welcher Mechanismus welche Art von Information oder Fähigkeit tragen soll.[^13]

Ein Skill bündelt ein wiederverwendbares Verfahren. Er ist ein Ordner mit einer Instruktionsdatei und optional Skripten, Referenzen und Ressourcen, er hält prozedurales und nicht beschreibendes Wissen, und zu Sitzungsbeginn bleiben nur Name und Beschreibung präsent, während die vollen Instruktionen bei Bedarf geladen werden, sodass ein System viele spezialisierte Fähigkeiten führen kann, ohne alle in jede Aufgabe einzuspeisen.[^14]

Ein Werkzeugprotokoll standardisiert die Verbindung zwischen Anwendungen und Werkzeugen, sodass ein Server ein Repository, eine Datenbank oder einen Validator allen protokollfähigen Clients bereitstellt und kein maßgeschneiderter Konnektor je Paarung nötig ist. Ob ein Werkzeug zur Aufgabe passt, ob seine Daten verlässlich sind und wie seine Ergebnisse zu deuten sind, bleibt außerhalb dessen, was der Standard entscheidet.[^15] Ein Agent-zu-Agent-Standard betrifft eine zweite Fläche, er trägt Auffinden, Aufgabenverwaltung und den Austausch von Ergebnissen, ohne dass ein Agent Speicher, Werkzeuge oder Implementierung offenlegen muss, und er ergänzt das Werkzeugprotokoll. Die methodischen Fragen bleiben unabhängig davon offen, welcher Agent wofür zuständig ist, welche Information übergeben wird, wie Konflikte sichtbar werden und wer bei widersprüchlichen Ergebnissen entscheidet.[^16]

Ein Subagent begrenzt einen Kontext. Eine delegierte Instanz bearbeitet einen Teil der Aufgabe in ihrem eigenen frischen Kontext, untersucht eine definierte Teilmenge der Ressourcen und gibt ein kompaktes Ergebnis zurück, was den Elternkontext vor Mengen an Zwischenmaterial schützt und unabhängige Prüfungen gleichzeitig laufen lässt, und das Muster trägt keinen formalen Standard und taucht dennoch nahezu gleich in allen Systemen auf. Jede delegierte Instanz braucht einen klaren Auftrag, begrenzten Kontext, ein definiertes Rückgabeformat und Regeln für Unsicherheit.[^17]

Die Kostenseite wird leicht unterschätzt. Mehr Agents erzeugen für sich keine besseren Ergebnisse, und jede zusätzliche Instanz schafft mögliche Übergaben, abweichende Annahmen und Fehlerstellen.[^18] Was mehrere Instanzen beitragen, ist Abdeckung. Unabhängige Prüfinstanzen machen Uneinigkeit sichtbar und lokalisieren verdächtige Fälle, die Evidenz aus Schemata, Tests, Quellenvergleichen und Domänenwissen bleibt wichtiger als Übereinstimmung zwischen ihnen, und der Zweck der Orchestrierung ist eine strukturierte Trajektorie unabhängiger Arbeit und keine höhere Zahl von Modellaufrufen.[^19]

Das Routing ist die letzte dieser Entscheidungen. Planung, Implementation und Review brauchen weder dasselbe Modell noch dasselbe Inferenzbudget, sodass Planung und Review auf einem für Reasoning gewählten Modell laufen können, während die Implementation auf einem für Durchsatz gewählten läuft, die Spezifikation im gepflegten Projektwissen kontextualisiert bleibt und das Routing selbst eine Gestaltungsentscheidung ist, die sich mit den Modellen ändert.[^20]

## Lücken

Drei der Themen, die die Gliederung diesem Kapitel zuweist, reichen über die Quellen hinaus.[^21]
- Übergaben nennt die Gliederung, und in den Quellen erscheinen sie nur als ein Punkt in der Liste dessen, was Agentic Engineering umfasst. Was ein Übergabepaket enthält und was eine übernehmende Seite daraus braucht, behandelt Kapitel 22 der anderen Manuskriptlinie.
- Auditierung erscheint hier über das Harness, das Spuren bewahrt, und über unabhängiges Review, und keine Quelle beschreibt ein Auditverfahren über eine abgeschlossene Trajektorie.
- Tests und visuelle Rückmeldung tragen die vier Prüfungen eines Verifikationsdurchgangs und die Reflexionsfragen aus Kapitel 10. Eine Behandlung auf dem von der Gliederung angesetzten Niveau verlangt die Hands-on-Ketten, die zur anderen Arbeitslinie gehören.

[^1]: Grounded in [[30_assertions/agentic-engineering-organises-multi-step-work]].
[^2]: Grounded in [[30_assertions/the-organisation-requirements-are-explicit]].
[^3]: Posit: die Umverteilung menschlicher Arbeit statt ihres Wegfalls ist die Formulierung der Gliederung, und die Quellen nennen die Einzeltätigkeiten ohne die zusammenfassende Aussage. Open evidence question: ein Vergleich, wofür Arbeitszeit vor und nach der Einführung agentischer Workflows aufgewendet wird.
[^4]: Grounded in [[30_assertions/the-workspace-is-part-of-the-method]].
[^5]: Grounded in [[30_assertions/specification-precedes-implementation]].
[^6]: Grounded in [[30_assertions/plans-stay-compact-and-revisable]].
[^7]: Grounded in [[30_assertions/least-privilege-and-reversibility-bound-the-run]].
[^8]: Grounded in [[30_assertions/instruction-files-are-context-not-enforcement]].
[^9]: Posit: das Urteil, dass eine schriftliche Grenze ohne technische nichts umsetzt, folgt aus der vorangehenden Assertion und steht in keiner Quelle. Open evidence question: wie oft dokumentierte Grenzen in Projekten überschritten werden, die sich allein auf Anleitung stützen.
[^10]: Grounded in [[30_assertions/increments-must-stay-inspectable]].
[^11]: Grounded in [[30_assertions/checking-a-run-covers-behaviour-data-and-requirements]].
[^12]: Grounded in [[30_assertions/harness-quality-changes-what-can-be-evaluated]].
[^13]: Grounded in [[30_assertions/the-mechanisms-are-not-interchangeable]].
[^14]: Grounded in [[30_assertions/skills-package-procedure-with-progressive-disclosure]].
[^15]: Grounded in [[30_assertions/tool-protocols-solve-integration-not-relevance]].
[^16]: Grounded in [[30_assertions/agent-to-agent-protocols-address-a-second-surface]].
[^17]: Grounded in [[30_assertions/subagents-bound-context-and-parallelise]].
[^18]: Grounded in [[30_assertions/more-agents-raise-coordination-cost]].
[^19]: Grounded in [[30_assertions/independent-review-extends-coverage-not-authority]].
[^20]: Grounded in [[30_assertions/model-routing-separates-functions]].
[^21]: Posit: die Lückenliste hält fest, wo dieses Kapitel hinter der Gliederung zurückbleibt. Open evidence question: ob sich ein Auditverfahren über eine abgeschlossene Trajektorie aus dem ableiten lässt, was ein Harness bewahrt.
