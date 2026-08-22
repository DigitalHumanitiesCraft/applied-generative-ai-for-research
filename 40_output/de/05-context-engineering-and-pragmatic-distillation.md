---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/a-knowledge-document-is-materialised-context-compression]]", "[[30_assertions/compression-reduces-volume-distillation-restructures]]", "[[30_assertions/context-engineering-selects-organises-and-provides]]", "[[30_assertions/distillation-is-task-dependent]]", "[[30_assertions/distillation-runs-through-three-operations]]", "[[30_assertions/formats-require-different-access-paths]]", "[[30_assertions/knowledge-engineering-and-context-engineering-divide-the-work]]", "[[30_assertions/nominal-capacity-is-no-guarantee-of-use]]", "[[30_assertions/not-everything-relevant-enters-the-context]]", "[[30_assertions/over-distillation-removes-what-action-needs]]", "[[30_assertions/the-bottleneck-shifts-from-model-to-context]]", "[[30_assertions/the-context-window-is-a-finite-processing-space]]", "[[30_assertions/the-target-is-a-dense-and-sufficient-context]]", "[[30_assertions/the-unit-is-the-supplied-representation]]", "[[30_assertions/three-levels-separate-holding-task-and-window]]"]
posits: 2
lang: de
part: "II. Vom Prompting zum grundierten Wissen"
chapter: 5
title: "Context Engineering und pragmatische Distillation"
topic: "[[Grounded-Knowledge]]"
feeding-sources: ["script chapters 3 to 5", "paper (Project Knowledge Base)", "Vault als materialisiertes Wissensmodell"]
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Context Engineering und pragmatische Distillation

## Der Gegenstand

Context Engineering ist die systematische Auswahl, Organisation, Pflege und Bereitstellung des Informationszustands, den eine Aufgabe verlangt. Es bestimmt, welche Informationen, Anweisungen, Werkzeuge und Beispiele zu einem Zeitpunkt verfügbar sind, in welcher Form und Reihenfolge sie bereitgestellt werden, wann weiteres Material nachgeladen wird und was bewusst draußen bleibt.[^1] Die letzte dieser Entscheidungen bleibt am häufigsten implizit und wiegt so schwer wie die übrigen.

Drei Ebenen sind auseinanderzuhalten, und ihre Vermischung erzeugt den größten Teil der Verwirrung in diesem Feld. Die Project Knowledge Base bewahrt den persistenten, inspizierbaren und revidierbaren Bestand. Der Working Context ist der für eine konkrete Aufgabe zusammengestellte Informationszustand. Das Context Window ist der technische Raum, in dem dieser Zustand verarbeitet wird. Allgemeine Berichte, Richtlinien zu anderen Quellentypen, vollständige Protokolle, überholte Schemaversionen und erledigte Fehlversuche gehören in den Bestand und bleiben aus dem Working Context einer einzelnen Aufgabe heraus, und Wissensdokumente müssen nicht für jede Aufgabe vollständig geladen werden.[^2]

Die daraus folgende Arbeitsteilung ist das Rückgrat von Teil II. Knowledge Engineering baut und pflegt den Bestand, Context Engineering stellt daraus zusammen, was eine Aufgabe braucht, und das zweite setzt das erste voraus, weil nur ein strukturierter Bestand selektives Laden erlaubt. Diese Abhängigkeit trennt Context Engineering von einer besseren Art des Promptings.[^3]

## Was das Fenster ist und was nicht

Das Context Window ist der endliche Raum, der alles hält, was ein Lauf verwenden kann. Darin liegen System- und Projektinstruktionen, die aktuelle Eingabe, der bisherige Verlauf, Dokumentauszüge, Werkzeugbeschreibungen, Werkzeugausgaben, Zwischenergebnisse und die erzeugte Antwort, und wenn Eingabe und Ausgabe zusammen die Grenze überschreiten, muss das System die Sequenz durch Kürzung oder Kompaktierung verkleinern oder die Anfrage zurückweisen.[^4]

Nominelle Kapazität ist keine nutzbare Kapazität. Position, Ablenkung und Umfang beeinflussen die Leistung, und relevante Information wird in langen Eingaben schwerer auffindbar, wenn sie zwischen ähnlichem oder widersprüchlichem Material steht. Context Rot bezeichnet den beobachteten Rückgang von Auffinden und Verwenden, wenn Kontexte länger, dichter oder ablenkungsreicher werden, und ist kein einzelner geklärter Mechanismus, weil Positionseffekte, Distraktoren, widersprüchliche Information, überholte Zwischenzustände und die Struktur der Aufgabe alle beitragen können. Die Leistung kann deshalb sinken, bevor die formale Grenze erreicht ist.[^5]

Daraus folgt nicht, dass Kontext kurz sein soll. Zu starke Reduktion entfernt Bedingungen, Unsicherheiten und Provenienz, und die Zielgröße ist so begrenzt wie möglich und so vollständig und differenziert wie die Aufgabe verlangt, jede Aussage trägt Information, ein minimaler Kern bleibt dauerhaft präsent, und Tiefe wird bedarfsgesteuert nachgeladen.[^6] Am meisten trägt diese Zielgröße im langen Lauf, denn mit wachsender Autonomie verschiebt sich der Engpass eines Workflows vom Modell zum Kontext. Drei Mechanismen tragen die Verschiebung, Leistungsabfall deutlich unterhalb der nominellen Grenze, Rauschansammlung über einen langen autonomen Lauf und ein endliches Reasoning-Budget, das für Navigation durch ungeordnetes Material verbraucht wird. Starke Modelle bleiben bei kurzen Einzelabfragen robust gegen unordentlichen Kontext, und das Problem kippt beim langhorizontigen Delegieren, wenn der Agent über viele Schritte selbständig mit dem Material arbeitet.[^7]

## Was tatsächlich in einen Kontext gelangt

Eine Datei im Projektordner ist nicht Teil des Kontextes, solange das System sie nicht liest, extrahiert, transformiert oder mit einem Werkzeug untersucht. Der Weg führt vom Bestand über ein Werkzeug, einen Parser oder ein Skript zu einer bereitgestellten Repräsentation und von dort über die Tokenisierung in das Fenster, sodass ein Skript die Zahlen zurückgeben kann, die eine Modellierungsfrage braucht, statt das Material selbst, und ein Agent vollständige Datenbestände über Werkzeuge untersuchen kann, während nur Zusammenfassungen, Abfrageergebnisse oder Auszüge in die Tokensequenz eingehen. Die methodisch relevante Einheit ist deshalb die bereitgestellte Repräsentation und nicht die Datei.[^8]

Formate unterscheiden sich darin, was dieser Weg kostet. Plain Text und Quellcode lassen sich meist direkt lesen, tabellarisches Material selektiv profilieren oder abfragen, Office-Formate müssen ausgelesen werden, Layoutformate verbinden Text, Struktur und Bild, Bilder werden multimodal verarbeitet oder beschrieben, und Datenbanken werden über Abfragen genutzt, ohne geladen zu werden.[^9] Projektrelevanz und Aufgabenrelevanz sind getrennte Eigenschaften. Der vollständige Bestand zählt für das Projekt, während nicht alles davon gleichzeitig in einen Kontext gehört, und weitere Ressourcen können bleiben, wo sie sind, und bei Bedarf über Werkzeuge erreicht werden.[^10]

Hier nimmt die Anordnung aus Kapitel 2 ihre allgemeine Form an. Das Modell liest über die Daten und schreibt Code, der die Daten liest. Was das Modell erhält, ist eine aufgabenspezifische Beschreibung von Struktur, Semantik, Unsicherheit, Ausnahmen und Relevanz, und der erzeugte Code verarbeitet das vollständige Material außerhalb des Kontextes.[^11]

## Distillation als pragmatische Modellierung

Reduktion kommt in zwei Formen vor, die häufig verwechselt werden. Kompression verringert den Umfang des Bereitgestellten durch Auswahl von Abschnitten, Zusammenfassung, Entfernen von Wiederholungen, Aggregation und Kompaktierung eines Arbeitsverlaufs, und eine kürzere Fassung ist nicht automatisch eine bessere, weil eine Zusammenfassung Unsicherheit glätten, Begründungen entfernen oder mehrere Alternativen in eine scheinbar eindeutige Regel verwandeln kann. Distillation geht weiter und überführt verfügbares Verständnis in eine selektive, strukturierte, inspizierbare und revidierbare Repräsentation, die für die folgende Arbeit hinreichend sein soll.[^12]

Drei Operationen tragen sie. Auswahl entscheidet, was für den Gegenstand relevant ist, Strukturierung macht Begriffe, Regeln und Beziehungen explizit, und Verdichtung entfernt Redundanz, ohne notwendige Differenzierung zu verlieren, und erhalten bleiben müssen die relevanten Begriffe und Unterscheidungen, die Beziehungen und Abhängigkeiten, die Bedingungen und Einschränkungen, die Unsicherheiten und offenen Fragen sowie die Begründungen hinter Entscheidungen.[^13] Das Gegenrisiko ist eine Repräsentation, die über den Punkt hinaus verdichtet wurde, an dem sie Arbeit noch anleiten kann, erkennbar an dem, was sie nicht mehr mitführt, und nicht an ihrer Länge.[^14]

Distillation ist deshalb aufgabenabhängig. Eine allgemeine Einführung, eine Implementierungsspezifikation und eine Verifikationsaufgabe brauchen verschiedene Repräsentationen desselben Wissens, und jede Reduktion entscheidet, welche Unterscheidungen für die folgende Arbeit verfügbar bleiben, was sie epistemisch folgenreich macht und nicht zu einer Frage der Bequemlichkeit.[^15] Ein destilliertes Dokument verlagert die Reduktion außerdem aus dem Lauf heraus. Als materialisierte Context Compression leistet es vorab eine Verdichtung, die das Modell sonst jedes Mal aus dem Rohmaterial herstellen müsste, und darin liegt der praktische Grund, weshalb ein gepflegter Bestand eine gut formulierte Anweisung über eine lange Aufgabe hinweg schlägt.[^16]

## Lücken

Zwei der Themen, die die Gliederung diesem Kapitel zuweist, sind nur teilweise behandelt.[^17]
- Retrieval und selektive Aufnahme nennt die Gliederung. Die Quellen dieser Arbeitslinie halten fest, dass Ressourcen über Werkzeuge erreichbar sind und eine Datenbank abgefragt werden kann, ohne geladen zu werden, und sie beschreiben keine Retrieval-Architektur, sodass das Kapitel das Prinzip nennt und den Mechanismus auslässt.
- Kontext-Refresh und Revision erscheinen hier über die geschichtete Anordnung mit dauerhaft präsentem Kern, und die Quellen geben kein Verfahren dafür, wann ein Kontext während eines Laufs neu gebaut werden sollte. Die andere Manuskriptlinie behandelt den Working Context in ihren Promptotyping-Kapiteln, und bis dieses Destillat gegen dieses hier gelesen werden kann, trägt ein Querverweis das Thema.

[^1]: Grounded in [[30_assertions/context-engineering-selects-organises-and-provides]].
[^2]: Grounded in [[30_assertions/three-levels-separate-holding-task-and-window]].
[^3]: Grounded in [[30_assertions/knowledge-engineering-and-context-engineering-divide-the-work]].
[^4]: Grounded in [[30_assertions/the-context-window-is-a-finite-processing-space]].
[^5]: Grounded in [[30_assertions/nominal-capacity-is-no-guarantee-of-use]].
[^6]: Grounded in [[30_assertions/the-target-is-a-dense-and-sufficient-context]].
[^7]: Grounded in [[30_assertions/the-bottleneck-shifts-from-model-to-context]].
[^8]: Grounded in [[30_assertions/the-unit-is-the-supplied-representation]].
[^9]: Grounded in [[30_assertions/formats-require-different-access-paths]].
[^10]: Grounded in [[30_assertions/not-everything-relevant-enters-the-context]].
[^11]: Posit: die Formel, dass das Modell über die Daten liest und erzeugter Code die Daten liest, ist die Verdichtung der vorangehenden Assertions durch die Gliederung und steht in dieser Form in keiner Quelle. Open evidence question: ein Vergleich von Ergebnissen, bei dem dieselbe Aufgabe einmal mit den Daten im Kontext und einmal mit einer Beschreibung samt erzeugtem Verarbeitungscode gestellt wird.
[^12]: Grounded in [[30_assertions/compression-reduces-volume-distillation-restructures]].
[^13]: Grounded in [[30_assertions/distillation-runs-through-three-operations]].
[^14]: Grounded in [[30_assertions/over-distillation-removes-what-action-needs]].
[^15]: Grounded in [[30_assertions/distillation-is-task-dependent]].
[^16]: Grounded in [[30_assertions/a-knowledge-document-is-materialised-context-compression]].
[^17]: Posit: die Lückenliste hält fest, wo dieses Kapitel hinter der Gliederung zurückbleibt. Open evidence question: ob das Destillat des Promptotyping-Papers ein Verfahren für die Erneuerung eines Working Context während eines Laufs mitführt.
