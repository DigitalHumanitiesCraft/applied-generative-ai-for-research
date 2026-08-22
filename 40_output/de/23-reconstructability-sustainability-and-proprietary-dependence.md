---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/a-knowledge-base-is-tested-by-bounded-continuation-tasks]]", "[[30_assertions/a-public-deployment-is-the-latest-state-of-a-development-history]]", "[[30_assertions/an-artefact-alone-does-not-witness-its-own-history]]", "[[30_assertions/comparative-evaluation-asks-when-the-arrangement-adds-value]]", "[[30_assertions/data-governance-bounds-what-may-be-processed]]", "[[30_assertions/exploration-scales-through-computational-profiling]]", "[[30_assertions/independent-transfer-is-evaluated-through-sustained-work]]", "[[30_assertions/promptotype-evaluation-separates-conformity-adequacy-and-purpose]]", "[[30_assertions/proprietary-dependence-limits-durability]]", "[[30_assertions/the-accepted-state-must-remain-identifiable]]", "[[30_assertions/the-journal-is-a-curated-provenance-index]]", "[[30_assertions/the-method-was-consolidated-from-one-practice]]", "[[30_assertions/the-provenance-of-a-generated-process-is-documentary]]", "[[30_assertions/the-sufficiency-of-distillation-is-practical]]", "[[30_assertions/transferability-differs-from-exact-reproduction]]"]
posits: 2
lang: de
part: "VI. Worked Example, Boundaries, and Implications"
chapter: 23
title: "Rekonstruierbarkeit, Nachhaltigkeit und proprietäre Abhängigkeit"
topic: "[[Boundaries-and-Implications]]"
feeding-sources: ["paper chapter 4", "hands-on chains from slides and script"]
working-title: true
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Rekonstruierbarkeit, Nachhaltigkeit und proprietäre Abhängigkeit

## Warum identische Regenerierung nicht vorausgesetzt werden kann

Generative Systeme sind stochastisch und häufig proprietär, und die Aufzeichnung von Prompts, Daten und Modellnamen garantiert nicht, dass ein späterer Lauf denselben Output erzeugt. Änderungen an Modell und Harness können das Systemverhalten ändern, auch wo Projektwissen und Forschungsdaten stabil bleiben, und die dokumentierte Praxis hängt wesentlich an bezahltem Zugang zu proprietären Frontier-Modellen und leistungsfähigen agentischen Werkzeugen, was direkte Kosten mit sich bringt, die Kontrolle über Systemänderungen verringert und in Spannung zu der Prüfbarkeit, Reproduzierbarkeit und Dauerhaftigkeit steht, die für Forschungssoftware und Forschungsdaten angestrebt wird.[^1] Die Methode trägt dem in ihrer eigenen Definition einer Iteration Rechnung, denn eine erneute Implementierung mit anderem Modell, anderem Harness oder anderem Projektstand gilt als neue Iteration und nicht als Reproduktion der früheren.[^2]

Daraus folgt nicht, dass Reproduzierbarkeit belanglos würde. Die deterministischen Teile eines Workflows bleiben reproduzierbar und sollen es bleiben, denn der vollständige Datenbestand wird von prüfbaren Operationen verarbeitet, während die generative Komponente an einem destillierten Bericht und ausgewählten Beispielen arbeitet.[^17] Was sich ändert, ist die Eigenschaft, die sich für den Prozess als Ganzes zusagen lässt.

## Rekonstruierbarkeit

Ein Forschungsprozess ist rekonstruierbar, wenn genug von seiner Evidenzgrundlage, seinem Projektwissen, seinen Spezifikationen, seinem Code, seinen Transformationen, seinen Entscheidungen und seiner Prüfgeschichte verfügbar bleibt, damit eine andere Person die Logik der Arbeit verstehen und nachvollziehen kann, auch wo die erzeugte Implementierung nicht bytegleich ist.[^3] Die Abgrenzung gegen exakte Reproduzierbarkeit ist dieselbe, die die Methode für den Transfer bereits zieht, denn eine andere Person kann die Methode anwenden und ein anderes Artefakt mit anderen Dokumenten, Modellen, Werkzeugen und Projektstrukturen herstellen, und verlangt ist, dass die Kernrelationen ohne undokumentierten Eingriff hergestellt, angewandt und rekonstruiert werden.[^4]

Zweierlei folgt daraus. Erstens, wo Rekonstruierbarkeit wohnt. Wo Interaktionsprotokolle nicht aufbewahrt werden, besteht die dauerhafte Provenienz eines generativen Prozesses aus dem gepflegten Projektwissen, dem Arbeitsnachweis, den Quellen, den dokumentierten Entscheidungen und der Versionsgeschichte, und dieses Material macht folgenreiche Stationen prüfbar, ohne jede Interaktion, jede verworfene Alternative und jedes Element stillschweigenden Urteils wiederzugeben.[^5] Ein kuratierter Provenienznachweis liefert genau den Teil, den Code nicht liefern kann, denn er hält pro Übergang fest, ob ein Ergebnis integriert, verworfen oder korrigiert wurde.[^6] Das Artefakt selbst liefert am wenigsten, denn ein lauffähiger Zustand belegt, dass er existierte und welche Operationen er bot, und er belegt weder seine Geschichte noch die Entscheidungen dahinter, noch die zurückgeschriebenen Befunde, noch die Autorität, über die etwas abgenommen wurde.[^7]

Zweitens ist Rekonstruierbarkeit prüfbar, was die Reproduzierbarkeit eines stochastischen Prozesses nicht ist. Eine begrenzte Fortsetzungsaufgabe setzt eine unabhängige Person vor die gepflegten Dokumente und die Projektressourcen und verlangt, das Projekt zu erklären, eine ausgewählte Abweichung zu diagnostizieren oder eine abgegrenzte Implementierungsaufgabe fortzusetzen, wobei beobachtete Schwierigkeiten dokumentarischen, technischen, zugangsbezogenen oder kompetenzbezogenen Grenzen zugeordnet werden.[^8] Das ist das Abschlusskriterium der Distillation als Messung verwendet, und es macht aus einer Eigenschaft, die wie ein Anspruch klingt, etwas, woran ein Projekt scheitern kann.[^9]

## Was sie bedroht

Mehrere Bedingungen zehren an der Rekonstruierbarkeit, und sie unterscheiden sich darin, ob ein Projekt auf sie einwirken kann. Modellversionswechsel und verändertes Produktverhalten ändern, was dieselbe Anweisung erzeugt, verdeckte Systeminstruktionen halten einen Teil des wirksamen Kontexts der Prüfung entzogen, proprietäre Modelle können ganz wegfallen, und die Einstellung eines Dienstes entfernt die Komponente, um die ein Workflow gebaut war.[^1] Kosten und Zugangsbeschränkungen wirken leiser, denn ein Prozess, den nur eine gut ausgestattete Gruppe erneut ausführen kann, ist im Prinzip rekonstruierbar und in der Praxis nicht, und dieselbe Praxis, die an bezahltem Frontier-Zugang hängt, muss das als Bedingung ihrer eigenen Ergebnisse benennen.[^1]

Lokale und offengewichtige Modelle sind der naheliegende Gegenzug, und die dokumentierte Praxis belegt nicht, wie weit die Methode mit ihnen wirksam bleibt.[^1] Diese Lücke ehrlich festzuhalten wiegt schwerer, als sie rhetorisch zu schließen, denn eine Evaluation müsste Modell und Harness als experimentelle Variablen behandeln und nicht als unsichtbare Hintergrundbedingungen.[^10]

Dagegen stehen drei Maßnahmen, die schon jetzt verfügbar sind. Der abgenommene Zustand muss über ein Repository-Release, eine archivierte Ablage oder eine andere dauerhafte Referenz identifizierbar und rekonstruierbar bleiben, ohne dass eine bestimmte Hosting-Plattform oder ein bestimmtes Versionierungsschema verlangt wäre.[^2] Outputs und Zwischenstände lassen sich zusammen mit dem Code archivieren, aus dem sie hervorgingen, und genau das macht ein öffentliches Deployment als jüngsten prüfbaren Stand einer dokumentierten Entwicklungsgeschichte lesbar statt als fertige Sache.[^11] Und Provenienz lässt sich erklären statt unterstellen, indem ein veröffentlichtes Artefakt benennt, welche Modelle und Werkzeuge verwendet wurden, was geprüft wurde, von wem und woran.[^5] Data Governance setzt dem allen die äußere Grenze, denn die Zulässigkeit hängt vom Material und von rechtlichen, institutionellen und architektonischen Bedingungen ab, und folgenreiche Änderungen sollen prüfbar und umkehrbar bleiben.[^12]

## Nachhaltigkeit bewahrt das Wissen und nicht nur den Code

Nachhaltigkeit verlangt in dieser Lage, neben dem Code auch das Wissen und die Entscheidungen zu bewahren, aus denen er abgeleitet wurde.[^13] Der Grund zeigt sich daran, was jede Schicht beantworten kann. Bewahrter Code beantwortet, was das Artefakt getan hat. Bewahrtes Projektwissen beantwortet, warum es das getan hat, was die Daten tragen und wo die Repräsentation aufhört. Die Bewertung eines abgenommenen Zustands trennt technische Konformität, wissenschaftliche Angemessenheit und Eignung für den erklärten Zweck, und nur die erste dieser drei lässt sich aus einem ausführbaren Stand allein zurückgewinnen.[^14]

Dieselbe Überlegung begrenzt, was Bewahrung einbringt. Die dokumentierte Praxis unterliegt Selektionseffekten, denn prüfbare Implementierungsstände sind systematischer erhalten geblieben als abgebrochene Versuche, weshalb ein bewahrter Nachweis die funktionierenden Wege überrepräsentiert.[^15] Ein Projekt, dessen Nachweis auch die negativen Ergebnisse tragen soll, muss sie bewusst bewahren, und der Vergleich, der zeigen würde, ob die Anordnung insgesamt Wert schafft, muss über die erste funktionsfähige Implementierung hinaussehen auf die Frage, ob sich das Artefakt später noch prüfen, verifizieren, warten, revidieren und übertragen lässt.[^16]

## Gaps
- Die hier gegebene Definition der Rekonstruierbarkeit stammt aus der Gliederung. Die Quellen behandeln sie über die Identifizierbarkeit des abgenommenen Zustands und über die proprietäre Abhängigkeit, ohne die Definition zu geben, was die Topic Map als offene Frage führt.
- Die Aufzählung der Bedrohungen, von verdeckten Systeminstruktionen bis zur Einstellung eines Dienstes, folgt der Gliederung. Die Quellen tragen die proprietäre Abhängigkeit und die Verhaltensänderung bei Modell- und Harness-Updates, sodass die einzelnen Punkte auf dieser Assertion ruhen.
- Publikationsstrategien für einen Promptotype sind in der Gliederung genannt. Die Quellen verlangen eine dauerhafte Referenz, ohne eine Form vorzuschreiben, und welchen Archivierungs- oder Publikationsweg das Buch empfiehlt, ist als offene Frage in der Topic Map festgehalten.
- Die Hands-on-Ketten des Skriptums und des Foliensatzes speisen Teil VI und gehören zur parallelen Schreiblane.

[^1]: Grounded in [[30_assertions/proprietary-dependence-limits-durability]].
[^2]: Grounded in [[30_assertions/the-accepted-state-must-remain-identifiable]].
[^3]: Posit: die Definition der Rekonstruierbarkeit ist der eigenen Gliederung des Buches entnommen, und keine Quelle dieses Vaults definiert den Begriff. Open evidence question: ob in der Literatur zur Reproduzierbarkeit eine etablierte Definition vorliegt, die das Buch stattdessen übernehmen sollte.
[^4]: Grounded in [[30_assertions/transferability-differs-from-exact-reproduction]].
[^5]: Grounded in [[30_assertions/the-provenance-of-a-generated-process-is-documentary]].
[^6]: Grounded in [[30_assertions/the-journal-is-a-curated-provenance-index]].
[^7]: Grounded in [[30_assertions/an-artefact-alone-does-not-witness-its-own-history]].
[^8]: Grounded in [[30_assertions/a-knowledge-base-is-tested-by-bounded-continuation-tasks]].
[^9]: Grounded in [[30_assertions/the-sufficiency-of-distillation-is-practical]].
[^10]: Grounded in [[30_assertions/independent-transfer-is-evaluated-through-sustained-work]].
[^11]: Grounded in [[30_assertions/a-public-deployment-is-the-latest-state-of-a-development-history]].
[^12]: Grounded in [[30_assertions/data-governance-bounds-what-may-be-processed]].
[^13]: Posit: eine Nachhaltigkeit, die nur den erzeugten Code bewahrt, bewahrt die Antwort und verwirft die Frage, denn die Gründe für eine Repräsentation leben in den gepflegten Dokumenten und nicht in einem ausführbaren Stand. Open evidence question: ein Fall, in dem eine bewahrte Codebasis ohne ihr Projektwissen von einem anderen Team erfolgreich fortgesetzt wurde.
[^14]: Grounded in [[30_assertions/promptotype-evaluation-separates-conformity-adequacy-and-purpose]].
[^15]: Grounded in [[30_assertions/the-method-was-consolidated-from-one-practice]].
[^16]: Grounded in [[30_assertions/comparative-evaluation-asks-when-the-arrangement-adds-value]].
[^17]: Grounded in [[30_assertions/exploration-scales-through-computational-profiling]].
