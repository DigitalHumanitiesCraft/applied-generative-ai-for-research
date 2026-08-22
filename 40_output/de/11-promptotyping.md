---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/a-research-artefact-is-a-project-specific-operational-form]]", "[[30_assertions/acceptance-rests-with-the-critical-expert]]", "[[30_assertions/agentic-capability-arises-from-model-harness-and-environment]]", "[[30_assertions/agentic-engineering-organises-extended-model-mediated-work]]", "[[30_assertions/context-and-agentic-engineering-are-interdependent]]", "[[30_assertions/context-engineering-organises-the-informational-environment]]", "[[30_assertions/distillation-is-the-documentary-operation-of-context-engineering]]", "[[30_assertions/mapping-into-an-existing-tool-confines-the-inquiry]]", "[[30_assertions/models-shift-the-cost-of-project-specific-implementation]]", "[[30_assertions/promptotyping-is-a-knowledge-driven-method]]", "[[30_assertions/software-operationalises-only-encoded-distinctions]]", "[[30_assertions/technical-verification-and-scholarly-validation-differ-in-kind]]", "[[30_assertions/the-four-forms-of-work-recur-without-a-fixed-order]]", "[[30_assertions/the-knowledge-base-differs-from-the-working-context]]", "[[30_assertions/the-knowledge-base-is-a-set-of-interrelated-documents]]", "[[30_assertions/the-method-was-consolidated-from-one-practice]]", "[[30_assertions/the-name-promptotyping-keeps-the-prototype-function]]", "[[30_assertions/the-promptotype-is-the-accepted-iteration-state]]", "[[30_assertions/write-back-makes-a-finding-durable]]"]
posits: 2
lang: de
part: "IV. Promptotyping"
chapter: 11
title: "Promptotyping. Forschungsdaten durch Context Engineering und Agentic Engineering in Forschungsartefakte übersetzen"
topic: "[[Promptotyping]]"
feeding-sources: ["paper chapter 2", "script chapter 7", "Promptotyping document templates"]
working-title: true
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Promptotyping. Forschungsdaten durch Context Engineering und Agentic Engineering in Forschungsartefakte übersetzen

## Die Asymmetrie, auf die die Methode antwortet

Wissenschaftliche Arbeit mit digitalen Forschungsdaten läuft über Software, und Software operationalisiert nur, was in Strukturen kodiert ist, die ihr Repräsentationsmodell verarbeiten kann.[^1] Eine tabellarische Datei öffnet sich als sortierbare Tabelle und lässt sich als Knotenliste importieren, sobald ihre Datensätze und Attribute den Strukturen entsprechen, die das aufnehmende Programm erwartet. Relationen, die in projekteigenem Markup kodiert sind, werden erst dann zu einem Netzwerk, wenn Entitäten, Relationen und Unsicherheiten interpretiert und auf ein Graphmodell abgebildet worden sind. Die Richtung dieser Übersetzung verlief üblicherweise vom Projekt zum Werkzeug, also bilden Forschende ihre Daten und ihre Fragen auf Repräsentationen ab, die für andere Zwecke gebaut wurden.[^1]

Diese Richtung hat einen Preis, der über den Aufwand hinausgeht. Die Abbildung auf ein vorhandenes Werkzeug bindet alles Weitere an die Unterscheidungen, Operationen und Interaktionsformen, die das Werkzeug bereitstellt, was dort wenig kostet, wo das Werkzeug für die Frage gebaut wurde, und viel dort, wo das nicht der Fall ist.[^2] Die Alternative bestand lange darin, etwas projektspezifisch zu bauen, und Expertise und Ressourcen dafür standen nicht gleichmäßig zur Verfügung.

Verändert hat sich der Preis einer ersten funktionierenden Implementierung. Large Language Models verringern Teile des Aufwands, Forschungsdaten auf die Modelle vorhandener Software abzubilden und näher angepasste Arbeitsweisen zu implementieren, während jeder Schritt, der eine Struktur erst erkennen oder interpretieren muss, probabilistisch bleibt.[^3] Ausschlaggebend ist dabei nicht die Geschwindigkeit. Weil sich nicht alle relevanten Anforderungen im Voraus bestimmen lassen, kann ein vorläufiges Artefakt Probleme der Spezifikation sichtbar machen und zeigen, was die Daten tragen und was nicht, wodurch die Implementierung Teil der Anforderungsbestimmung wird statt deren Ausführung.[^3]

## Was Promptotyping ist

Promptotyping ist eine iterative, wissensgetriebene Methode, um projektspezifische digitale Forschungsartefakte aus strukturierten Forschungsdaten und gepflegtem Projektwissen über Context Engineering und Agentic Engineering zu entwickeln.[^4] Ihre organisierende Struktur ist eine sich entwickelnde und versionierte Projektwissensbasis, und Befunde aus Implementierung und Prüfung werden in sie zurückgeschrieben, sodass spätere Arbeit vom revidierten Verständnis ausgeht.[^4] Wissensgetrieben ist die Methode in einem präzisen Sinn. Die Implementierung geht von einem gepflegten Bericht darüber aus, wie die Daten verstanden werden und wofür sie operationalisiert werden sollen, und dieser Bericht hat eine semi-formale dokumentarische Form, die keine formale Inferenz trägt.[^4]

Der Name verbindet Prompt und Prototyping und behält die etablierte Funktion des Prototyps als vorläufige Implementierung, an der Anforderungen und Gestaltungsmöglichkeiten geprüft und verfeinert werden.[^5] Das Artefakt, das dabei entsteht, ist eine projektspezifische operative Form, in der Forschende für einen definierten wissenschaftlichen Zweck mit strukturierten Forschungsdaten arbeiten, was es über seine Funktion im Forschungsprozess von den Daten unterscheidet.[^6]

Die Arbeitseinheit ist weder ein einzelner Prompt noch ein einzelner Akt der Codegenerierung. Sie ist ein Satz zusammenhängender Dokumente, begrenzter Repräsentationen, die aus umfangreicherem Forschungsmaterial destilliert, für menschliche Prüfung und Revision gepflegt und für die Arbeitskontexte von Agents verfügbar gehalten werden.[^7] Diese Dokumente halten das aktuelle Verständnis des Projekts von seinen Quellen und Daten fest, seinen Forschungskontext, seine Anforderungen, seine Repräsentationsentscheidungen, seine technischen Randbedingungen, seine Prozessgeschichte und seine Prüfkriterien. Die dauerhafte Wissensbasis ist vom aufgabenspezifischen Arbeitskontext zu trennen, den ein Agent für einen bestimmten Auftrag erhält, und die Methode behandelt Auswahl als Teil des Context Engineering, statt Anhäufung an deren Stelle treten zu lassen.[^8]

## Die beiden Praktiken, die sie integriert

Context Engineering ist die systematische Auswahl, Organisation, Pflege und Bereitstellung der Information, die ein LLM-basiertes System für seine Arbeit braucht. Es erweitert Prompt Engineering vom einzelnen Prompt auf die informationelle Umgebung, in der Prompts interpretiert werden, und es besteht nicht darin, alles verfügbare Material in ein Kontextfenster zu legen.[^9] Agentic Engineering ist die systematische Organisation der ausgedehnten, werkzeuggestützten Arbeit eines Agents und regelt, wie Aufgaben zerlegt und koordiniert werden, wie Werkzeuge eingesetzt werden, wann menschliches Eingreifen nötig ist und wie die Arbeit geprüft und fortgesetzt wird.[^10]

Keine der beiden Praktiken gleicht ein Versagen der anderen aus. Eine sorgfältig gepflegte Wissensbasis bestimmt kein angemessenes Vorgehen, und ein gut organisierter Workflow repariert keinen unzureichenden Bericht über die Daten oder den Forschungszweck.[^11] Beide arbeiten in einer technischen Umgebung, die selbst zum System gehört, denn der Harness liefert Kontext, Zugriff auf Projektressourcen, Werkzeuge und Rückmeldung, und agentische Leistungsfähigkeit entsteht aus Modell, Harness und Umgebung zusammen.[^12]

Um diese beiden Praktiken herum ordnet die Methode die älteren Disziplinen an, auf die sie angewiesen ist. Requirements Engineering und Scholar-Centred Design liefern die Übersetzung wissenschaftlicher Praxis in Aussagen, die eine Implementierung anleiten können. Knowledge Engineering liefert die dauerhafte Repräsentation dessen, was das Projekt für den Fall hält. Distillation ist die dokumentarische Operation, durch die das in Preparation und Exploration gewonnene Verständnis zu den gepflegten Dokumenten wird, aus denen Implementierung und Prüfung hervorgehen.[^13] Deterministische Validierung, modellgestützte Review und Verifikation durch einen Critical Expert bilden die Prüfanordnung und sind Gegenstand von Kapitel 16.

## Der Zyklus und seine Autorität

Die Arbeit läuft in vier wiederkehrenden Formen, Preparation, Exploration, Distillation und Implementation. Sie sind analytisch unterscheidbar und bilden keine feste oder ausschließlich lineare Folge; ihre Tiefe, Reihenfolge und Wiederkehr richten sich nach Stand und Zweck des Projekts, und Befunde aus der Implementation können die Arbeit in jede frühere Form zurückführen, am häufigsten in die Distillation.[^14] Dieser Rückweg ist der Mechanismus und kein Nebeneffekt der Praxis. Eine Korrektur wird methodisch folgenreich, sobald sie in das gepflegte Projektwissen eingearbeitet wird, statt auf die aktuelle Implementierung beschränkt zu bleiben, und genau das meint Write-back, weshalb es keine weitere Phase ist.[^15]

Diese Anordnung gibt den Dokumenten eine Autorität, die prozedural ist.[^20] Sie sind die Referenz, aus der die Implementierung hervorgeht, und sie sind revidierbar durch eben die Implementierung, die sie anleiten. Wo eine Implementierung eine ungedeckte Annahme, eine unvollständige Anforderung oder eine übersehene Eigenschaft der Daten offenlegt, ändert sich das dokumentierte Verständnis.

Die Abnahme ist ein eigener Akt. Eine Iteration wird zum Promptotype, sobald gepflegtes Projektwissen, das entstandene Artefakt, der referenzierte Forschungsdatenstand und die dokumentierten Abnahmegründe für einen erklärten Zweck einen kohärenten und identifizierbaren Zustand bilden, und ein lauffähiges oder plausibles Artefakt erreicht diese Schwelle nicht, wenn sich sein Verhältnis zu Wissen, Daten und Gründen nicht rekonstruieren lässt.[^16] Die Entscheidung liegt beim Critical Expert, also bei der Person oder Gruppe, die kompetent und verantwortlich beurteilt, ob das Projektwissen das Forschungsmaterial angemessen repräsentiert und ob das Artefakt für seinen Zweck taugt. Ein Agent kann Vorschläge und Einschätzungen beitragen und kann keine Verantwortung für deren Angemessenheit übernehmen.[^17]

Hinter dieser Arbeitsteilung liegt eine Unterscheidung, auf die die ganze Methode angewiesen ist. Technische Verifikation fragt, ob ein Output formalisierten Anforderungen entspricht. Wissenschaftliche Validierung fragt, ob die Repräsentation, die diese Anforderungen kodieren, durch das Quellenmaterial gedeckt und für ihren Zweck angemessen ist. Eine Implementierung kann daher zugleich korrekt und unzureichend sein, weil sie eine Anforderung getreu umsetzt, die in dieser Form nicht hätte gestellt werden dürfen.[^18]

## Der Status des Anspruchs

Die Methode wurde aus dokumentierter Praxis konsolidiert und nicht aus einer Theorie abgeleitet oder gegen eine Kontrollbedingung geprüft. Der Bericht, der in diesem Teil folgt, betrifft eine Praxis, die seit 2023 von einer hybriden Person aus Forschung und Entwicklung geführt wurde, deren Fälle keine kontrollierte oder repräsentative Stichprobe bilden, deren Dokumentation Selektionseffekten unterliegt, weil prüfbare Implementierungsstände systematischer erhalten blieben als abgebrochene Versuche, und deren beobachtete Verbesserungen sich nicht sauber der Methode statt leistungsfähigeren Systemen, besseren Werkzeugen oder gewachsener Erfahrung zurechnen lassen.[^19] Jeder Anspruch der folgenden Kapitel ist durch diesen Geltungsbereich begrenzt, und wo das Argument darüber hinausgeht, sagt der Text es.

Dieses Buch wendet die Methode auf die eigene Entstehung an, was ein weiterer Grund ist, die Grenze früh zu benennen. Eine Methode, die ihre eigene Entstehung organisiert, kann diese Entstehung prüfbar machen, und sie kann damit nicht ihre eigene Wirksamkeit belegen.[^21]

## Gaps
- Kapitel 7 des Skriptums beschreibt dieselbe Methode für ein Lehrpublikum und wird von der parallelen Schreiblane destilliert. Die didaktische Fassung der vier Arbeitsformen und des Critical Expert steht daher noch nicht zum Vergleich mit der Paper-Fassung bereit; die Topic Map hält die offene Frage fest, welche Fassung das Buch trägt.
- Die Hands-on-Ketten des Skriptums und die begleitenden Folien sind in der Feeding Map für Teil IV genannt und gehören der anderen Lane. Das Kapitel führt deshalb kein durchgeführtes Beispiel eines ersten Promptotyping-Zyklus.
- Requirements Engineering und Scholar-Centred Design sind hier als die Disziplinen benannt, die die Methode integriert. Ihre Behandlung stützt sich auf die zusammenfassende Darstellung des Papers; ein direkter Anker in der Literatur zum Requirements Engineering setzt voraus, dass diese Publikationen als Quellen aufgenommen werden.

[^1]: Grounded in [[30_assertions/software-operationalises-only-encoded-distinctions]].
[^2]: Grounded in [[30_assertions/mapping-into-an-existing-tool-confines-the-inquiry]].
[^3]: Grounded in [[30_assertions/models-shift-the-cost-of-project-specific-implementation]].
[^4]: Grounded in [[30_assertions/promptotyping-is-a-knowledge-driven-method]].
[^5]: Grounded in [[30_assertions/the-name-promptotyping-keeps-the-prototype-function]].
[^6]: Grounded in [[30_assertions/a-research-artefact-is-a-project-specific-operational-form]].
[^7]: Grounded in [[30_assertions/the-knowledge-base-is-a-set-of-interrelated-documents]].
[^8]: Grounded in [[30_assertions/the-knowledge-base-differs-from-the-working-context]].
[^9]: Grounded in [[30_assertions/context-engineering-organises-the-informational-environment]].
[^10]: Grounded in [[30_assertions/agentic-engineering-organises-extended-model-mediated-work]].
[^11]: Grounded in [[30_assertions/context-and-agentic-engineering-are-interdependent]].
[^12]: Grounded in [[30_assertions/agentic-capability-arises-from-model-harness-and-environment]].
[^13]: Grounded in [[30_assertions/distillation-is-the-documentary-operation-of-context-engineering]].
[^14]: Grounded in [[30_assertions/the-four-forms-of-work-recur-without-a-fixed-order]].
[^15]: Grounded in [[30_assertions/write-back-makes-a-finding-durable]].
[^16]: Grounded in [[30_assertions/the-promptotype-is-the-accepted-iteration-state]].
[^17]: Grounded in [[30_assertions/acceptance-rests-with-the-critical-expert]].
[^18]: Grounded in [[30_assertions/technical-verification-and-scholarly-validation-differ-in-kind]].
[^19]: Grounded in [[30_assertions/the-method-was-consolidated-from-one-practice]].
[^20]: Posit: die Autorität der Dokumente prozedural zu nennen, folgt aus den Rückwegen des Zyklus, denn eine Referenz, die von der Arbeit revidiert werden darf, die sie anleitet, bindet den nächsten Schritt und nicht die Sache. Open evidence question: ob die Quellen das Autoritätsverhältnis irgendwo in diesen Begriffen fassen, statt seine Wirkungen zu beschreiben.
[^21]: Posit: eine Methode, die auf die eigene Produktion angewandt wird, liefert einen prüfbaren Nachweis dieser Produktion und keine Evidenz über ihre Wirkung auf andere Arbeit, weil der Fall einzeln ist und seine Autorschaft mit der Urheberschaft der Methode zusammenfällt. Open evidence question: eine Evaluation, in der Beteiligte, die die Methode nicht entwickelt haben, aus derselben Spezifikation ein vergleichbares Artefakt herstellen und abnehmen.
