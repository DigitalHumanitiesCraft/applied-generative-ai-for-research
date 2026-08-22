---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/a-failure-becomes-learning-only-through-interpretation]]", "[[30_assertions/a-finding-is-attributed-before-it-is-written-back]]", "[[30_assertions/acceptance-rests-with-the-critical-expert]]", "[[30_assertions/agent-instruction-documents-translate-knowledge-into-imperatives]]", "[[30_assertions/agentic-review-yields-probabilistic-evidence]]", "[[30_assertions/design-knowledge-stays-declarative]]", "[[30_assertions/deterministic-verification-is-bounded-by-its-checks]]", "[[30_assertions/exploration-scales-through-computational-profiling]]", "[[30_assertions/findings-arise-at-several-non-interchangeable-levels]]", "[[30_assertions/formal-modelling-does-not-determine-the-operational-form]]", "[[30_assertions/implementation-proceeds-through-bounded-inspectable-increments]]", "[[30_assertions/interaction-exposes-unwarranted-precision]]", "[[30_assertions/preparation-assembles-an-accessible-source-basis]]", "[[30_assertions/promptotype-evaluation-separates-conformity-adequacy-and-purpose]]", "[[30_assertions/the-accepted-state-must-remain-identifiable]]", "[[30_assertions/the-boundary-to-research-software-engineering]]", "[[30_assertions/the-four-forms-of-work-recur-without-a-fixed-order]]", "[[30_assertions/the-material-document-carries-epistemic-responsibility]]", "[[30_assertions/the-specification-holds-interlocked-questions-in-one-place]]", "[[30_assertions/the-sufficiency-of-distillation-is-practical]]", "[[30_assertions/user-stories-bridge-scholar-centred-design-and-implementation]]", "[[30_assertions/verification-documents-are-adversarial-and-precede-the-claim]]", "[[30_assertions/write-back-makes-a-finding-durable]]"]
posits: 2
lang: de
part: "VI. Worked Example, Boundaries, and Implications"
chapter: 21
title: "Ein vollständig durchgeführtes Beispiel"
topic: "[[Boundaries-and-Implications]]"
feeding-sources: ["paper chapter 4", "hands-on chains from slides and script"]
working-title: true
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Ein vollständig durchgeführtes Beispiel

## Was dieses Kapitel trägt und was das Begleit-Repository trägt

Das durchgeführte Beispiel folgt einem Forschungsprojekt von der Ausgangsfrage bis zum veröffentlichten Artefakt. Ausführliche Kommandos, Dateien, Prompts, Screenshots, Übungen und alternative Implementierungen gehören in ein Begleit-Repository und nicht in die Monographie, weshalb dieses Kapitel die Kette darlegt, benennt, was jeder Schritt leisten muss, und die Eigenschaften nennt, die der Tutorial-Datensatz haben muss.[^1] So gelesen ist das Kapitel die Spezifikation des Beispiels und das Repository dessen Ausführung.

Der Tutorial-Datensatz muss echte semantische Komplexität, fehlende Werte, Unsicherheit, mehrere plausible Forschungsperspektiven und genug Struktur für deterministische Verarbeitung tragen.[^2] Jede Anforderung verdient ihren Platz. Semantische Komplexität und mehrere plausible Perspektiven werden gebraucht, weil dieselben Daten verschiedene Forschungsfragen tragen können und dafür verschiedene operative Formen brauchen, was die Lage ist, für die die Methode existiert.[^3] Fehlende Werte und Unsicherheit werden gebraucht, weil die Repräsentation dessen, was die Daten nicht entscheiden, der Ort ist, an dem eine technisch mögliche Visualisierung am leichtesten mehr behauptet, als die Datensätze tragen.[^4] Genug Struktur für deterministische Verarbeitung wird gebraucht, weil der vollständige Datenbestand von prüfbaren Operationen außerhalb des Modellkontexts verarbeitet wird, während Profile und ausgewählte Beispiele in den Arbeitskontext eingehen.[^5]

## Die Kette

Das Beispiel läuft in vier Bewegungen, die den vier Arbeitsformen entsprechen, und die Schritte innerhalb einer Bewegung sind geordnet, ohne eine feste Folge zu sein, denn Befunde aus der Implementation können die Arbeit in jede frühere Form zurückführen.[^6]

Die erste Bewegung bereitet vor. Die Forschungsfrage wird formuliert, die Nutzenden und ihre wissenschaftlichen Tätigkeiten werden bestimmt, und die Daten werden inspiziert und profiliert. Preparation bringt das Material in eine zugängliche Projektumgebung und macht seinen Stand explizit, wobei sie Zugänglichkeit für Prüfung und computationelle Nutzung mit dokumentierter Provenienz und dokumentierten Grenzen verlangt statt Normalisierung oder formaler Modellierung.[^7] Das Profiling gehört zur Exploration und richtet sich nach dem Umfang des Materials, ein kleiner Tutorial-Datensatz wird also direkt untersucht, während derselbe Schritt an einer großen Sammlung ein Skript wäre, das Struktur über das Korpus extrahiert und aggregiert.[^5] Die Bestimmung von Nutzenden und Tätigkeiten erzeugt die narrative Form der Anforderungen, in der Rolle, Ziel und Nutzen benannt und später einer prüfbaren Erwartung mit Akzeptanzkriterium zugeordnet werden.[^8]

Die zweite Bewegung destilliert. Der Grounded Vault wird angelegt, und die gepflegten Dokumente werden geschrieben, also das Materialdokument, das festhält, was die Daten sind, woher sie kommen, wie sie modelliert sind und wo sie aufhören zu tragen;[^9] die Specification, die Anforderungen, Szenarien, Funktionsumfang und Entscheidungen an einem Ort führt;[^10] das Design-Dokument, das Designhaltung und die Behandlung von Unsicherheit als deklaratives Wissen festhält;[^11] die Prüfkriterien, die benennen, was behauptet wird und wie eine dritte Person es widerlegen könnte;[^12] und das Action Document, das all das in Imperative für den Agenten übersetzt und selbst kein Wissen trägt.[^13] Die Distillation ist fertig, wenn eine neue mitarbeitende Person oder eine neue Agent-Instanz die Logik des Projekts aus diesen Dokumenten rekonstruieren und die Arbeit ohne undokumentierte Erklärung fortsetzen könnte.[^14]

Die dritte Bewegung implementiert und diagnostiziert. Ein minimales Artefakt wird erzeugt, und die Inkremente bleiben klein genug, dass jedes einen lauffähigen Zustand herstellt, der sich mit dem gepflegten Wissen vergleichen lässt, bevor weitere Annahmen eingebaut werden.[^15] Danach wird das Artefakt auf sachliche, konzeptionelle, visuelle und technische Fehler geprüft, und jeder Fehler wird der Schicht zugeordnet, die ihn erzeugt hat, denn Befunde entstehen auf mehreren zusammenhängenden, aber nicht austauschbaren Ebenen, und jedes Problem als Codedefekt zu behandeln würde die Entscheidungen verdecken, durch die das Artefakt entstanden ist.[^16] Die Zuordnung entscheidet, wohin die Korrektur geht, denn ein Befund über die repräsentierte Domäne verlangt eine Revision von Modell oder Erfassungspraxis, während ein Befund über die Darstellung einer angemessenen Unterscheidung im Design der Oberfläche bleiben kann.[^17] Anschließend werden die Dokumente revidiert, und das ist die Operation, die eine Korrektur dauerhaft statt lokal macht.[^18]

Die vierte Bewegung prüft und schließt ab. Die deterministische Validierung läuft zuerst und entscheidet die formal ausdrückbaren Bedingungen, wobei sie genau so weit reicht wie die Eigenschaften, die ihre Prüfungen kodieren.[^19] Modellgestützte Review erweitert Reichweite und Tiefe der Prüfung über eine begrenzte, werkzeuggestützte Untersuchung, deren Befunde probabilistische Evidenz bleiben.[^20] Die Verifikation durch den Critical Expert entscheidet danach, ob die Daten angemessen repräsentiert sind, ob die Frage sinnvoll bearbeitet wird, ob Unsicherheit angemessen behandelt ist und ob der Output als Teil wissenschaftlicher Arbeit angenommen werden kann.[^21] Es folgt die Veröffentlichung mit ihrer Provenienzdokumentation, und der abgenommene Zustand muss über ein Release, eine archivierte Ablage oder eine andere dauerhafte Referenz identifizierbar und rekonstruierbar bleiben.[^22] Der letzte Schritt entscheidet zwischen Abschluss, Wartung und Übergabe an das Research Software Engineering, und das ist eine Entscheidung über Pflichten und nicht über Code, denn die Grenze ist überschritten, sobald ein Artefakt dauerhaft, gewartet, sicher, barrierefrei, institutionell betrieben, geteilt, integriert oder für Dritte unterstützt sein muss.[^23]

## Wozu das Beispiel dient

Ein Beispiel dieser Art zeigt, wie ein Artefakt hergestellt wird, und seine nützlichere Demonstration ist, wie sich diagnostizieren lässt, warum ein erzeugtes Artefakt falsch ist und wohin eine dauerhafte Korrektur gehört.[^24] Das Erste ist ein Abarbeiten von Schritten und lässt sich aus jedem Tutorial ablesen. Das Zweite ist die Kompetenz, die die Methode tatsächlich verlangt, und sie wird nur dort sichtbar, wo ein Fehler von seinem Symptom bis zur erzeugenden Schicht und von dort in das Dokument verfolgt wird, das sich ändert.

Die abschließende Abnahme ist gebunden wie jede andere. Ein Tutorial-Promptotype wird als Lehrartefakt abgenommen, und seine Bewertung trennt technische Konformität, wissenschaftliche Angemessenheit und Eignung für diesen erklärten Zweck, sodass ein exploratives oder lehrendes Artefakt keine Kriterien des Produktionsbetriebs erfüllen muss, die außerhalb seines abgenommenen Umfangs liegen.[^25]

## Gaps
- Welcher Datensatz das durchgeführte Beispiel trägt, ist eine offene Entscheidung, die im Projektplan und in der Topic Map festgehalten ist. Bis sie fällt, benennt dieses Kapitel die verlangten Eigenschaften und kann die Kette an keinem Datensatz durchführen.
- Das Paper beschreibt kein Tutorial-Projekt, weshalb die achtzehn Schritte der Gliederung hier über die allgemeinen Assertions zu jeder Arbeitsform verankert sind und nicht über eine dokumentierte Instanz.
- Die Hands-on-Ketten des Skriptums und des Foliensatzes sind in der Feeding Map für Teil VI genannt und gehören zur parallelen Schreiblane, sodass keine didaktische Fassung der Kette zum Vergleich vorlag.
- Das Begleit-Repository existiert noch nicht. Was es enthalten muss, folgt aus diesem Kapitel, und die Entscheidung, es anzulegen, ist eine Operator-Entscheidung.

[^1]: Posit: das durchgeführte Beispiel zwischen einer Spezifikation in der Monographie und einer Ausführung im Begleit-Repository zu teilen, folgt der Gliederung und hält aus dem Buch heraus, was mit einer Modellversion oder einem Werkzeugrelease altert. Open evidence question: ob Lesende der Kette allein aus der Spezifikation folgen können, was nur ein Versuch mit Lesenden zeigen würde.
[^2]: Posit: die fünf verlangten Eigenschaften des Tutorial-Datensatzes stehen in der Gliederung, und keine Quelle dieses Vaults nennt einen Datensatz, der sie hat. Open evidence question: welcher offen verfügbare Datensatz alle fünf in einem Umfang erfüllt, den Lesende durcharbeiten können.
[^3]: Grounded in [[30_assertions/formal-modelling-does-not-determine-the-operational-form]].
[^4]: Grounded in [[30_assertions/interaction-exposes-unwarranted-precision]].
[^5]: Grounded in [[30_assertions/exploration-scales-through-computational-profiling]].
[^6]: Grounded in [[30_assertions/the-four-forms-of-work-recur-without-a-fixed-order]].
[^7]: Grounded in [[30_assertions/preparation-assembles-an-accessible-source-basis]].
[^8]: Grounded in [[30_assertions/user-stories-bridge-scholar-centred-design-and-implementation]].
[^9]: Grounded in [[30_assertions/the-material-document-carries-epistemic-responsibility]].
[^10]: Grounded in [[30_assertions/the-specification-holds-interlocked-questions-in-one-place]].
[^11]: Grounded in [[30_assertions/design-knowledge-stays-declarative]].
[^12]: Grounded in [[30_assertions/verification-documents-are-adversarial-and-precede-the-claim]].
[^13]: Grounded in [[30_assertions/agent-instruction-documents-translate-knowledge-into-imperatives]].
[^14]: Grounded in [[30_assertions/the-sufficiency-of-distillation-is-practical]].
[^15]: Grounded in [[30_assertions/implementation-proceeds-through-bounded-inspectable-increments]].
[^16]: Grounded in [[30_assertions/findings-arise-at-several-non-interchangeable-levels]].
[^17]: Grounded in [[30_assertions/a-finding-is-attributed-before-it-is-written-back]].
[^18]: Grounded in [[30_assertions/write-back-makes-a-finding-durable]].
[^19]: Grounded in [[30_assertions/deterministic-verification-is-bounded-by-its-checks]].
[^20]: Grounded in [[30_assertions/agentic-review-yields-probabilistic-evidence]].
[^21]: Grounded in [[30_assertions/acceptance-rests-with-the-critical-expert]].
[^22]: Grounded in [[30_assertions/the-accepted-state-must-remain-identifiable]].
[^23]: Grounded in [[30_assertions/the-boundary-to-research-software-engineering]].
[^24]: Grounded in [[30_assertions/a-failure-becomes-learning-only-through-interpretation]].
[^25]: Grounded in [[30_assertions/promptotype-evaluation-separates-conformity-adequacy-and-purpose]].
