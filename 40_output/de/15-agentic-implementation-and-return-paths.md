---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/a-failure-becomes-learning-only-through-interpretation]]", "[[30_assertions/a-finding-is-attributed-before-it-is-written-back]]", "[[30_assertions/a-public-deployment-is-the-latest-state-of-a-development-history]]", "[[30_assertions/a-runnable-state-is-not-yet-a-promptotype]]", "[[30_assertions/agentic-capability-arises-from-model-harness-and-environment]]", "[[30_assertions/conformity-to-a-mapping-is-examined-separately-from-its-adequacy]]", "[[30_assertions/critical-expertise-may-be-distributed-without-transferring-responsibility]]", "[[30_assertions/findings-about-agentic-work-change-the-arrangement]]", "[[30_assertions/findings-arise-at-several-non-interchangeable-levels]]", "[[30_assertions/implementation-can-participate-in-the-formation-of-a-model]]", "[[30_assertions/implementation-keeps-the-project-intelligible-and-testable]]", "[[30_assertions/implementation-proceeds-through-bounded-inspectable-increments]]", "[[30_assertions/interface-findings-concern-the-claims-a-representation-implies]]", "[[30_assertions/project-level-and-method-level-write-back-differ]]", "[[30_assertions/the-four-forms-of-work-recur-without-a-fixed-order]]", "[[30_assertions/the-handoff-document-is-a-process-inbox]]", "[[30_assertions/write-back-makes-a-finding-durable]]"]
posits: 0
lang: de
part: "IV. Promptotyping"
chapter: 15
title: "Agentische Implementation und Rückwege"
topic: "[[Promptotyping]]"
feeding-sources: ["paper chapter 2", "script chapter 7", "Promptotyping document templates"]
working-title: true
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Agentische Implementation und Rückwege

## Den Dokumentensatz an einen Agenten übergeben

Implementation macht gepflegtes Projektwissen über LLM-gestützte Entwicklung handlungsfähig. Sie kann als iterative chatbasierte Interaktion laufen, in der Beteiligte Prompts, Code und Ergebnisse zwischen Modell und Projektumgebung bewegen, und sie ist wirksamer über einen AI Harness organisiert, sobald der Agent direkt mit Projektdateien arbeiten, Code ausführen, Zwischenergebnisse prüfen und über mehrere Schritte fortfahren muss. In beiden Anordnungen besteht die Arbeit aus begrenzten Aufgaben, deren Folgen prüfbar werden.[^1] Die technische Umgebung ist Teil des Systems und nicht dessen Verpackung, denn der Harness liefert Kontext, Zugriff auf Projektressourcen, Werkzeuge und Rückmeldung, und Leistungsfähigkeit entsteht aus Modell, Harness und Umgebung zusammen.[^2]

Was der Agent aus der semi-formalen Spezifikation herstellt, ist das gewöhnliche Material von Forschungssoftware, also Parser, Transformationen, Schemata, Tests, Abfragen, Anwendungscode, Oberflächen und die sichtbaren Artefakte, die ein Projekt veröffentlicht oder benutzt. Die Reihenfolge, in der es entsteht, unterscheidet die Methode von unstrukturierter Generierung. Die Arbeit läuft über prüfbare und versionierte Inkremente, und jedes Inkrement soll einen lauffähigen Zustand herstellen, der sich mit dem gepflegten Projektwissen vergleichen lässt, bevor weitere Annahmen in die Implementierung eingebaut werden.[^1] Frühe Inkremente können bewusst auf eine Transformation, eine Oberfläche oder einen Workflow zielen, der funktionsfähig genug für Prüfung und Diskussion ist, statt auf einen vollständigen Funktionsumfang.

Die agentische Implementation hat zudem eine Pflege-Pflicht, die keine Kosmetik ist. Generierter Code kann Refactoring verlangen, und ausführbare Prüfungen werden ergänzt oder überarbeitet, wo sich relevantes Verhalten formalisieren lässt, denn diese Praktiken erhalten die Prüfbarkeit der Implementierung und erlauben, beobachtetes Verhalten auf die Dokumente zu beziehen, die es anleiten. Das Dokument, das die Teststrategie trägt, benennt ihre Garantien, ihre bewussten Lücken und ihre reproduzierbaren Run-Kommandos, und es sagt dem Agenten, in welcher Form eine neue Garantie abzusichern ist, was einen Sign-off von der Behauptung zur Messung hebt.[^3]

Wo mehrere Agents an begrenzten Komponenten oder Prüfungen arbeiten, ändert die Aufteilung die Koordination und nicht die Verantwortung. Zuweisungen und Berechtigungen bleiben explizit und auditierbar, der Zugriff auf Werkzeuge und Projektressourcen bleibt auf die delegierte Aufgabe beschränkt, Aktionen und Ausgaben jedes Agents bleiben gegen Projektwissen, Quellen und Kriterien prüfbar, und eine steigende Zahl von Agents kann den Aufwand für Koordination und Audit erhöhen.[^4]

## Die Schleife, die nicht zwischen Code und Output läuft

Ein Implementierungsstand ist vorläufig hinreichend, sobald er lauffähig, prüfbar und über Versionierung identifizierbar ist, sodass er Prüfung und Diskussion mit verantwortlichen Beteiligten tragen kann. Dieser Stand ist die Grundlage, von der zweckgebundene Prüfung und Abnahme ausgehen, und noch keine abgenommene Iteration.[^5] Das erzeugte Artefakt ist damit nicht die letzte Instanz. Es ist eine Implementierung, an der sich die Angemessenheit des gepflegten Projektverständnisses prüfen lässt, und es kann an der Bildung des Modells, der Erfassungspraxis und der Anforderungen teilnehmen, aus denen es entwickelt wurde, unter der Bedingung, dass die durch seine Nutzung offengelegten Folgen interpretiert, dokumentiert und eingearbeitet werden.[^6]

An dieser Bedingung arbeitet die Methode. Befunde entstehen auf mehreren zusammenhängenden, aber nicht austauschbaren Ebenen, die die repräsentierte Domäne, die Quelleninterpretation, die Forschungsdatenmodelle, die Erfassungspraxis, die Transformationen, die Interfacerepräsentationen, die Organisation agentischer Arbeit, die Prüfverfahren und die Zuweisung von Autorität betreffen. Jedes beobachtete Problem als Defekt im generierten Code zu behandeln würde die wissenschaftlichen, technischen und organisatorischen Entscheidungen verdecken, durch die das Artefakt entstanden ist, und obwohl ein implementiertes Artefakt die Wirkungen mehrerer Schichten gleichzeitig sichtbar macht, muss verantwortliche Interpretation unterscheiden, welche Schicht die beobachtete Folge erzeugt hat.[^7]

Die Zuordnung geht der Korrektur also voraus. Manche Befunde betreffen die repräsentierte Domäne und verlangen eine Revision von Datenmodell oder Erfassungspraxis, andere betreffen die Zugänglichmachung einer im Übrigen angemessenen Unterscheidung und können im operativen oder visuellen Design der Oberfläche bleiben.[^8] Ein Fehler in der einen Richtung verdeckt eine Grenze des Modells hinter Interfacelogik, ein Fehler in der anderen ändert ein Domänenmodell, das nie schuld war.[^7]

## Wohin ein Befund geht

Die Rückwege des Zyklus lassen sich an den Ebenen ablesen. Ein Implementierungsdefekt wird im Code korrigiert. Eine unvollständige oder mehrdeutige Anweisung an den Agenten wird in der Agent-Konfiguration korrigiert, ebenso Arbeitskontexte, Berechtigungen, Eskalationswege, Prüfzustände oder Abnahmekriterien, wo diese versagt haben.[^9] Eine fehlende oder falsch gefasste Anforderung gehört in das Declarative Document, das sie trägt. Eine ungedeckte Annahme führt die Arbeit in die Exploration zurück, und eine geänderte Quelle oder ein unvollständiges Schema führt sie in die Preparation zurück, denn die Phasen sind wiederkehrend, und Befunde aus der Implementation können die Arbeit in jede von ihnen zurückführen.[^10]

Zwei Ebenen verdienen eine eigene Behandlung, weil ihre Fehler von außen gleich aussehen. Eine Transformation kann ihrem Mapping entsprechen und schemavaliden Output erzeugen und die Quelle dennoch unzureichend repräsentieren, und ein Fehler in der Umsetzung eines angemessenen Mappings wird in der Transformation korrigiert und nicht im Mapping, weshalb das implementierte Ergebnis erlaubt, Konformität getrennt von der wissenschaftlichen Angemessenheit dessen zu prüfen, dem sie entspricht.[^11] Ebenso kann eine Repräsentation mehr behaupten, als ihre Daten tragen, etwa wo mit frühestem und spätestem Datum kodierte Angaben als präzise Punkte auf einer Zeitleiste erschienen und danach als Intervalle dargestellt wurden, sodass das Write-back die visuelle und operative Behandlung von Unsicherheit betraf und die zugrunde liegenden Datensätze unberührt ließ.[^12]

Write-back ist die Operation, die all das dauerhaft macht. Eine Korrektur wird methodisch folgenreich, sobald sie in das gepflegte Projektwissen eingearbeitet wird, statt in der aktuellen Implementierung zu bleiben, ihr Zweck ist es, die interpretierte Folge eines Befunds in den Projektstand zu tragen und nicht jede Beobachtung zu bewahren, und nicht jeder folgenreiche Befund verlangt eine Revision, denn die Implementierung kann stattdessen die Grenze dessen festlegen, was eine Iteration verantwortbar behaupten kann.[^13] Wo ein Projekt eine Process Inbox führt, liegt auch die Mechanik fest, denn dauerhafter Inhalt wird zuerst in das zuständige Dokument integriert, danach hält ein knapper Eintrag Gegenstand, Quelle, Ziel und Ergebnis fest, und erst dann wird der offene Punkt entfernt.[^14]

## Lernen auf Projekt- und auf Methodenebene

Write-back hat neben der Ebene auch eine Reichweite. Projektebenes Write-back ändert das gepflegte Wissen, die Implementierungsbedingungen oder die Prüfanordnung eines Projekts, während methodenebenes Write-back einen Befund in allgemeinere Regeln einarbeitet, und die Verallgemeinerung hängt von der verfügbaren Evidenz, von der Wiederkehr des Problems über Fälle hinweg und von den Folgen der vorgeschlagenen Regel ab.[^15] Die Zurückhaltung ist beabsichtigt, denn eine Methode, die jeden lokalen Behelf als allgemeine Vorschrift aufnähme, würde genau in den Projekten unbrauchbar, denen sie dienen soll. Eine dokumentierte Beobachtung qualitativer Verschlechterung in langen Implementierungssitzungen führte zu Änderungen an Sitzungslänge, Kontextauffrischung und Rückgriff auf die gepflegten Dokumente und steht als Kandidat für eine allgemeine Regel und nicht als solche.[^15]

Keine der beiden Lernformen stellt sich von selbst ein. Ein beobachtetes Scheitern wird erst durch Interpretation, Zuordnung, Dokumentation und Einarbeitung in den gepflegten Projektstand zu Wissen auf Projekt- oder Methodenebene, und ohne diese Operationen bleibt es ein lokales Implementierungsereignis, das die nächste Iteration wiederholt.[^16] Die Repositorien der dokumentierten Fälle zeigen, wie die Alternative aussieht, wenn sie umgesetzt wird, denn sie bewahren Nachweise über Alternativen, die geprüft, eingeschränkt, ersetzt oder verworfen wurden, was ihre öffentlichen Deployments zu den jeweils jüngsten prüfbaren Ständen dokumentierter Entwicklungsgeschichten macht.[^17]

## Gaps
- Die Hands-on-Kette des Skriptums, die eine Implementierungssitzung durchgeht, gehört zur parallelen Schreiblane, sodass dieses Kapitel kein Protokoll einer agentischen Sitzung und kein Beispiel einer Milestone-Folge führt.
- Die Liste der Artefaktarten, die ein Agent aus der Spezifikation herstellt, stammt aus der Gliederung. Die Quellen beschreiben die Produkte der Implementation allgemein, sodass die Aufzählung auf der Gliederung ruht und nicht auf einer eigenen Quellstelle.
- Konkrete Praktiken der Agent-Konfiguration, etwa der Zuschnitt von Berechtigungen und die Gestaltung von Eskalationswegen, sind hier auf dem Niveau benannt, das die Quellen erreichen. Eine Behandlung mit ausgearbeiteten Konfigurationen setzt voraus, dass die Action-Layer-Vorlagen als Anweisungen und nicht als Dokumentspezifikationen gelesen werden.

[^1]: Grounded in [[30_assertions/implementation-proceeds-through-bounded-inspectable-increments]].
[^2]: Grounded in [[30_assertions/agentic-capability-arises-from-model-harness-and-environment]].
[^3]: Grounded in [[30_assertions/implementation-keeps-the-project-intelligible-and-testable]].
[^4]: Grounded in [[30_assertions/critical-expertise-may-be-distributed-without-transferring-responsibility]].
[^5]: Grounded in [[30_assertions/a-runnable-state-is-not-yet-a-promptotype]].
[^6]: Grounded in [[30_assertions/implementation-can-participate-in-the-formation-of-a-model]].
[^7]: Grounded in [[30_assertions/findings-arise-at-several-non-interchangeable-levels]].
[^8]: Grounded in [[30_assertions/a-finding-is-attributed-before-it-is-written-back]].
[^9]: Grounded in [[30_assertions/findings-about-agentic-work-change-the-arrangement]].
[^10]: Grounded in [[30_assertions/the-four-forms-of-work-recur-without-a-fixed-order]].
[^11]: Grounded in [[30_assertions/conformity-to-a-mapping-is-examined-separately-from-its-adequacy]].
[^12]: Grounded in [[30_assertions/interface-findings-concern-the-claims-a-representation-implies]].
[^13]: Grounded in [[30_assertions/write-back-makes-a-finding-durable]].
[^14]: Grounded in [[30_assertions/the-handoff-document-is-a-process-inbox]].
[^15]: Grounded in [[30_assertions/project-level-and-method-level-write-back-differ]].
[^16]: Grounded in [[30_assertions/a-failure-becomes-learning-only-through-interpretation]].
[^17]: Grounded in [[30_assertions/a-public-deployment-is-the-latest-state-of-a-development-history]].
