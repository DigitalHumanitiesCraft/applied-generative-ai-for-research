---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/agentic-capability-arises-from-the-compound-system]]", "[[30_assertions/agents-predate-language-models]]", "[[30_assertions/an-agent-pursues-a-goal-across-several-calls]]", "[[30_assertions/autonomy-is-the-span-between-interventions]]", "[[30_assertions/feedback-arrives-from-several-sources]]", "[[30_assertions/intervention-points-are-named-in-advance]]", "[[30_assertions/single-agent-and-federation-are-two-modes]]", "[[30_assertions/the-execution-loop-is-a-control-loop]]", "[[30_assertions/the-scope-of-action-comes-from-tools-and-environment]]", "[[30_assertions/the-semantic-web-took-the-reverse-route]]", "[[30_assertions/the-shift-is-from-response-to-trajectory]]", "[[30_assertions/tool-use-changes-the-epistemic-structure]]"]
posits: 4
lang: de
part: "III. Agentische Forschungsarbeit"
chapter: 8
title: "Vom Modell zum Agenten"
topic: "[[Agentic-Work]]"
feeding-sources: ["script chapter 6", "slide sections Agentic Engineering and Workflows"]
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Vom Modell zum Agenten

## Was ein System zu einem Agenten macht

Ein isolierter Modellaufruf erzeugt eine Ausgabe. Ein Agent verfolgt ein Ziel über mehrere Modell- und Werkzeugaufrufe, untersucht seine Umgebung, wählt eine Handlung, beobachtet das Ergebnis und aktualisiert sein Vorgehen, und die Unterscheidung verlangt keine vollständige Autonomie, weil heutige Agents innerhalb menschlich gesetzter Ziele, Werkzeuge, Berechtigungen und Abbruchbedingungen arbeiten. Entscheidend ist, dass das Modell an Auswahl und Koordination mehrerer Handlungen beteiligt ist.[^1]

Die Fähigkeit ist keine Eigenschaft des Modells. Das Modell steuert flexible Planung und Interpretation bei, und die Handlungsmöglichkeiten entstehen aus den Werkzeugen und der Umgebung, die das umgebende System bereitstellt.[^2] Auf der Ebene des Gesamtsystems formuliert entsteht agentische Leistungsfähigkeit aus dem Verbund von Modell, Harness und Umgebung, sodass die isolierte Beurteilung eines Modells etwas anderes misst als das, was ein Projekt damit tun kann.[^3]

Der Zyklus hat eine Form, die älter ist als das Vokabular. Zustand erfassen, einen begrenzten nächsten Schritt planen, ein Werkzeug oder eine Aktion ausführen, das Ergebnis beobachten und das Vorgehen aktualisieren ist die Schleife, und ihre Struktur ist der Regelkreis, den die Kybernetik 1948 beschrieben hat, ein System, das sich selbst steuert, indem es Information über die eigenen Wirkungen zurückführt, mit Werkzeugausgaben an der Stelle von Sensoren.[^4] Die Information, die einen Lauf steuert, kommt von Validatoren, Tests, Fehlermeldungen, Werkzeugausgaben, Reviews anderer Agents, menschlichen Rückmeldungen und veränderten Anforderungen, und die Quellen unterscheiden sich darin, was jede von ihnen feststellen kann.[^5]

## Werkzeuge und die epistemische Veränderung

Werkzeuge erweitern einen Textgenerator zu einem System, das handeln kann. Dateizugriff, Terminal, Codeausführung, Suche, Datenbanken, Browser, Validatoren und spezialisierte Schnittstellen gehören dazu, und am meisten tragen jene, die Evidenz über die Folgen einer Handlung zurückgeben, weil ein Compiler, eine Testsuite oder ein Schema-Validator eine Frage beantwortet, die das Modell sonst über sich selbst beantworten würde. Das System stützt sich damit nicht mehr allein auf erzeugten Text und kann Beobachtungen gewinnen, die seinen nächsten Schritt einschränken.[^6]

Hier wird der Unterschied zu einem Konversationssystem methodisch statt technisch. Ein Chatverlauf lässt sich an einer Antwort beurteilen. Ein agentisches System erzeugt eine Trajektorie aus Beobachtungen, Zwischenentscheidungen, Werkzeugaufrufen, Dateiänderungen, Ausführungsergebnissen und Folgehandlungen, sodass Verlässlichkeit von der Organisation der gesamten Sequenz abhängt und gestaltet wird die Trajektorie und nicht die Antwort.[^7]

## Autonomie als Spanne

Autonomie misst in dieser Praxis den Umfang der Arbeit zwischen zwei menschlichen Eingriffen und bedeutet keine Abwesenheit von Kontrolle.[^8] Sie als Menge an Freiheit zu lesen führt zur falschen Gestaltungsfrage. Die richtige lautet, wo ein Mensch hinsieht, und die Stellen, an denen das geschehen muss, lassen sich vorab benennen, widersprüchliche Anforderungen, fehlende fachliche Grundlagen, schwer reversible Änderungen, sensible Ressourcen, fachlich folgenreiche Modellierungsentscheidungen sowie Validierung und Acceptance.[^9]

Sie vor einem Lauf zu benennen macht den Eingriff zum Teil der Gestaltung. Damit ist auch das Verhältnis bestimmt, das die Gliederung zwischen Fähigkeit und Spezifikationsbedarf ansetzt. Mit wachsender Spanne muss mehr vom Zweck, von den Einschränkungen, vom Wissen, von den Berechtigungen und von den Prüfkriterien eines Projekts in persistenter und inspizierbarer Form vorliegen, bevor die Ausführung beginnt, weil der Agent die Stellen passieren wird, an denen ein Mensch gefragt hätte.[^10]

## Ein älterer Begriff

Der Agentenbegriff ist Jahrzehnte älter als Sprachmodelle. Klassische Arbeiten bestimmen einen Agenten über sein Verhältnis zu einer Umgebung und seine Fähigkeit zu autonomem, reaktivem und zielgerichtetem Handeln, benennen die vier Eigenschaften Autonomie, Reaktivität, Proaktivität und soziale Fähigkeit, und frühere Systeme zeigen, dass Agentenhaftigkeit nicht an Sprache gebunden ist. Verändert haben Sprachmodelle den praktischen Gestaltungsraum, weil natürliche Sprache, Code und heterogene digitale Ressourcen nun eine gemeinsame Schnittstelle für Planung und Handlung bilden können, sodass die heutigen Systeme eine gegenwärtige Ausprägung einer viel älteren Idee sind. Die vier Eigenschaften von 1995 bilden sich auf sie ab als Lauf ohne Rückfrage über viele Schritte, Verarbeiten von Werkzeugergebnissen und Fehlern, Zielverfolgung über die Einzelanweisung hinaus und Delegation an Subagents.[^11]

Eine zweite Linie ist zu nennen, weil sie den umgekehrten Weg zu einem vergleichbaren Ziel nahm. Die Vision des Semantic Web von 2001 zielte nicht darauf, dass Maschinen menschliche Sprache verstehen. Maschinenverständliche Dokumente hießen, dass eine Maschine ein wohldefiniertes Problem auf wohldefinierten Daten löst, während Menschen ihre Daten über Ontologien und eindeutige Bezeichner strukturieren, und heutige Modelle verarbeiten unstrukturierten Text direkt ohne diese Infrastruktur.[^12] Der Vergleich trägt für Teil II, weil er bestimmt, wozu ein gepflegter Wissensbestand da ist. Er ist nicht mehr das formale Substrat, das eine Maschine zum Handeln braucht, und er ist zu dem Nachweis geworden, an dem ein Mensch prüfen kann, was die Maschine getan hat.[^13]

## Ein Agent oder mehrere

Am selben Werkzeug sind zwei Betriebsarten unterscheidbar. Im engeren Sinn ist ein Agent ein modulares, von einem Sprachmodell angetriebenes System für abgegrenzte Aufgaben, mit Werkzeugzugriff, Gedächtnis und Planung um das Modell herum. Ein orchestrierter Verbund ergänzt Zusammenarbeit, dynamische Aufgabenzerlegung, persistentes Gedächtnis und koordinierte Autonomie und unterscheidet sich in der Architektur und nicht im Grad der Autonomie, sodass ein System im einfachen Lauf als ein Agent handelt und sich zum Verbund bewegt, sobald es an mehrere koordinierte Instanzen delegiert.[^14]

Das als Stufenleiter zu lesen verschöbe die Entscheidung. Was die zweite Betriebsart einbringt und was sie kostet, ist Gegenstand von Kapitel 9, und hier zählt, dass es sich um Betriebsarten und nicht um Kategorien handelt, sodass ein Projekt pro Aufgabe wählt und nicht ein einziges Mal.[^15]

## Lücken

Zwei der Themen, die die Gliederung diesem Kapitel zuweist, sind nur teilweise abgedeckt.[^16]
- Gedächtnis und Persistenz erscheinen in den Quellen als Teil der allgemeinen Liste dessen, was ein Harness verwaltet, und als Hinweis, dass Zwischenergebnisse in persistente Artefakte gehören. Wie sich Gedächtnis über Sitzungen hinweg verhält und worauf ein Projekt sich dabei verlassen kann, beschreiben diese Quellen nirgends.
- Repository- und Dateizugriff sowie Codeausführung stehen hier innerhalb der Liste der Werkzeugklassen und nicht als eigene Behandlung. Das durchgearbeitete Beispiel in Teil VI ist der Ort, an dem sie die von der Gliederung angesetzte Genauigkeit erhalten, und die Hands-on-Ketten der anderen Manuskriptlinie tragen das Material.

[^1]: Grounded in [[30_assertions/an-agent-pursues-a-goal-across-several-calls]].
[^2]: Grounded in [[30_assertions/the-scope-of-action-comes-from-tools-and-environment]].
[^3]: Grounded in [[30_assertions/agentic-capability-arises-from-the-compound-system]].
[^4]: Grounded in [[30_assertions/the-execution-loop-is-a-control-loop]].
[^5]: Grounded in [[30_assertions/feedback-arrives-from-several-sources]].
[^6]: Grounded in [[30_assertions/tool-use-changes-the-epistemic-structure]].
[^7]: Grounded in [[30_assertions/the-shift-is-from-response-to-trajectory]].
[^8]: Grounded in [[30_assertions/autonomy-is-the-span-between-interventions]].
[^9]: Grounded in [[30_assertions/intervention-points-are-named-in-advance]].
[^10]: Posit: der Schluss, dass eine längere Spanne mehr vom Projekt in persistenter Form vor der Ausführung verlangt, stammt aus der Gliederung und steht in dieser Allgemeinheit in keiner Quelle. Open evidence question: ein Vergleich von Läufen wachsender Spanne mit der Vollständigkeit der Spezifikation, von der sie ausgingen.
[^11]: Grounded in [[30_assertions/agents-predate-language-models]].
[^12]: Grounded in [[30_assertions/the-semantic-web-took-the-reverse-route]].
[^13]: Posit: den gepflegten Bestand als Nachweis für die Prüfung statt als Substrat für Maschinenhandeln zu lesen ist die eigene Verortung dieses Buches. Open evidence question: ob Projekte, die formale Repräsentationen neben Prosa führen, sie zum Handeln, zum Prüfen oder für beides verwenden.
[^14]: Grounded in [[30_assertions/single-agent-and-federation-are-two-modes]].
[^15]: Posit: die Empfehlung, die Betriebsart pro Aufgabe zu wählen, folgt aus der Zwei-Modi-Assertion und steht in keiner Quelle. Open evidence question: welche Aufgabeneigenschaften vorhersagen, dass ein Verbund einen einzelnen Agenten schlägt.
[^16]: Posit: die Lückenliste hält fest, wo dieses Kapitel hinter der Gliederung zurückbleibt. Open evidence question: ob die Hands-on-Ketten der anderen Manuskriptlinie eine Beschreibung von Gedächtnis über Sitzungen hinweg mitführen.
