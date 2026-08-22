---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/acceptance-is-a-purpose-bound-decision]]", "[[30_assertions/agents-produce-evidence-without-authority]]", "[[30_assertions/an-early-error-propagates-along-the-trajectory]]", "[[30_assertions/findings-must-be-written-back]]", "[[30_assertions/formal-conformance-is-not-scholarly-adequacy]]", "[[30_assertions/implementation-tests-the-project-understanding]]", "[[30_assertions/increments-must-stay-inspectable]]", "[[30_assertions/independent-review-extends-coverage-not-authority]]", "[[30_assertions/long-runs-accumulate-noise]]", "[[30_assertions/more-agents-raise-coordination-cost]]", "[[30_assertions/self-revision-is-no-independent-verification]]", "[[30_assertions/the-assessment-vocabulary-has-four-levels]]", "[[30_assertions/the-bottleneck-shifts-from-model-to-context]]", "[[30_assertions/the-interface-can-manufacture-false-certainty]]", "[[30_assertions/the-prompt-is-one-component-of-the-loop]]"]
posits: 5
lang: de
part: "III. Agentische Forschungsarbeit"
chapter: 10
title: "Fehler, Drift und Verification Debt"
topic: "[[Agentic-Work]]"
feeding-sources: ["script chapter 6", "slide sections Agentic Engineering and Workflows"]
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Fehler, Drift und Verification Debt

## Fehler, an die Formulierung nicht heranreicht

Die hier behandelten Fehler überstehen bessere Anweisungen. Sie entstehen aus der Länge einer Trajektorie, aus der Anordnung um das Modell herum und aus der Art, wie Ergebnisse angenommen werden, und jeder von ihnen ist eine Eigenschaft des Workflows und nicht eines einzelnen Aufrufs.[^0]

Der erste ist die Fortpflanzung. Mit wachsender Aufgabendauer steigt neben der möglichen Leistung die Zahl der Stellen, an denen ein Fehler in spätere Schritte eingeht, und ein Agent, der eine veraltete Richtlinie liest, kann ein unpassendes Muster erzeugen, es transformieren und alles Nachgelagerte an die falsche Struktur anpassen, sodass jeder einzelne Schritt richtig aussieht, während der ursprüngliche Defekt bis ans Ende wandert.[^1] Nichts im Lauf meldet das, weil jede lokale Prüfung besteht.

Der zweite ist die Ansammlung. Ein langer Lauf sammelt Ausgaben, Fehler, Werkzeugergebnisse und frühere Entscheidungen, und in einem undifferenzierten Kontext kann der Agent erheblichen Aufwand darauf verwenden, durch die eigene Geschichte zu navigieren, weshalb stabiles Wissen außerhalb des flüchtigen Gesprächs gehört, relevante Teile bei Bedarf geladen werden und abgeschlossene Phasen kompakte Artefakte hinterlassen, die spätere Phasen aufnehmen, statt jedes Token mitzuschleppen.[^2] Derselbe Mechanismus erscheint von der anderen Seite in der Kontextschicht. Die Leistung fällt deutlich unterhalb der nominellen Fenstergrenze, Rauschen sammelt sich, das Reasoning-Budget ist endlich, und mit wachsender Autonomie wandert der Engpass vom Modell zum Kontext.[^3]

Der dritte ist ein Fehler der Oberfläche. Ein Interface kann Unsicherheit als entschieden darstellen, weshalb an einem laufenden Artefakt zu fragen ist, ob Unsicherheiten als Unsicherheiten erscheinen, ob die Oberfläche falsche Eindeutigkeit erzeugt, welche Modellierungsprobleme erst dort sichtbar werden und welche Dokumente daraufhin zu revidieren sind. Jede Stufe von der Quelle über Transkription, Datenmodell und Transformation bis zur Darstellung enthält Entscheidungen darüber, welche Unterschiede sichtbar, bearbeitbar und interpretierbar werden, und ein Agent kann die Verantwortung dafür nicht übernehmen.[^4]

## Warum die Ebene mehr zählt als das Symptom

Ein Defekt, der sich in einem Artefakt zeigt, gehört selten dorthin, wo er sich zeigt. Implementation ist eine Form der Untersuchung und keine neutrale Ausführung, weil eine fehlende Regel oder eine zu grobe Modellierung erst durch das funktionierende Artefakt sichtbar werden kann und ein Frontend eine Unterscheidung erzwingen kann, die das Datenmodell einebnet. Anforderungen lassen sich oft nicht vollständig vor der Implementation bestimmen, sodass ein vorläufiges Artefakt Annahmen und Grenzen sichtbar macht und den Vergleich alternativer Operationalisierungen erlaubt, während die folgenreichen Urteile bei den Fachleuten bleiben.[^5]

Die diagnostische Frage lautet deshalb, in welche Ebene eine Korrektur gehört. Ein sichtbarer Defekt kann aus der Implementation, aus den Handlungsanweisungen, aus den Anforderungen, aus dem Datenverständnis, aus der Quellenaufbereitung oder aus der Forschungsfrage selbst stammen, und ihn auf der Ebene zu reparieren, auf der er erschien, lässt die Ursache stehen.[^6] Befunde werden nicht dadurch zu Projektwissen, dass sie entstehen; sie werden geprüft und, wo begründet, in den gepflegten Bestand zurückgeführt, und das verhindert, dass relevantes Wissen nur im Chat, im Code oder im Gedächtnis Einzelner bleibt.[^7]

Hier schließt sich die gesamte Anordnung. Der Prompt ist eine operative Komponente eines Zyklus, der von Projektwissen über einen Working Context und eine Implementation zu einer Prüfung führt, die das Projektwissen revidiert, und Artefakt und dokumentiertes Verständnis entwickeln sich gemeinsam weiter.[^8] Ein Projekt, das Code repariert und Befunde nicht zurückführt, hält den Zyklus offen, und jeder folgende Lauf startet aus einem Verständnis, das der vorige bereits widerlegt hat.[^9]

## Selbstprüfung und ihre Grenzen

Zwei Eigenschaften der in Teil I beschriebenen Systeme kehren hier wieder. Self-Revision durch das erzeugende Modell kann Fehler sichtbar machen und liefert keine unabhängige Verifikation, weil dasselbe System eigene Fehlannahmen übersehen oder nachträglich plausibel begründen kann, und verlässlicher machen sie explizite Kriterien, externe Tests und prüfbare Referenzen außerhalb des Modells.[^10] Agents und Validatoren können Fehler lokalisieren, Kriterien anwenden, Unterschiede berichten und Evidenz zusammenstellen, und nichts davon überträgt die Entscheidung über die Annahme eines Ergebnisses.[^11]

Mehr Prüfinstanzen erweitern die Abdeckung und nicht die Autorität. Unabhängige Instanzen machen Uneinigkeit sichtbar und lokalisieren verdächtige Fälle, und die Evidenz aus Schemata, Tests, Quellenvergleichen und Domänenwissen bleibt wichtiger als Übereinstimmung zwischen ihnen.[^12] Jede zusätzliche Instanz kostet außerdem etwas, weil mehr Agents mehr Übergaben, abweichende Annahmen und Fehlerstellen schaffen.[^13]

Was wirkt, ist prozedural. Inkremente bleiben prüfbar, wenn sie ausführbar sind, einem definierten Projektzustand angehören, gegen Anforderungen geprüft werden können und klein genug sind, dass eine Ursache rekonstruierbar bleibt, und das Material, das sonst verschwindet, Pläne, Entscheidungen, Prüfergebnisse und offene Fragen, geht in persistente Artefakte.[^14]

## Verification Debt

Der Begriff, den dieses Buch für das Angesammelte verwendet, ist Verification Debt, der Bestand an erzeugter Arbeit, der vorläufig angenommen und noch nicht auf dem Niveau geprüft wurde, das wissenschaftliche oder betriebliche Verwendung verlangt.[^15] In einer Hinsicht verhält er sich wie andere Formen technischer Schuld und in einer anderen nicht. Er wächst still, weil eine vorläufige Annahme keine Spur im Artefakt hinterlässt, und anders als ein nicht refaktorierter Baustein kann er eine Behauptung entwerten statt eine Änderung zu verlangsamen.

Zwei Dinge machen ihn im Prinzip messbar. Acceptance ist eine zweckgebundene Entscheidung, sodass ein für einen Zweck angenommener und für einen anderen verwendeter Zustand eine bereits fällige Schuld ist, und den Zweck im Moment der Annahme zu benennen verwandelt eine implizite Schuld in eine verzeichnete.[^16] Die vier Prüfebenen sagen dann, was tatsächlich geschehen ist, ob ein Artefakt gegen Kriterien evaluiert, gegen formalisierte Anforderungen verifiziert, als quellen- und zweckangemessen validiert und für eine benannte Verwendung angenommen wurde.[^17] Ein Projekt, das festhält, welche der vier auf welchem Zustand gelaufen sind, kann seine Schuld an diesem Nachweis ablesen.

Formale Konformität ist der Ort, an dem sich die Schuld am häufigsten verbirgt. Gültige Syntax beweist die Syntax und Schemakonformität die formalen Regeln, während die Fragen, ob eine Transkription ihrer Quelle entspricht, ob Unsicherheit angemessen repräsentiert ist, ob ein Interface die vorgesehenen Interpretationshandlungen stützt und ob Modellierungsentscheidungen naturalisiert werden, von anderer Art sind, und ein Artefakt kann jede formale Prüfung bestehen und an allen scheitern.[^18]

## Lücken

Vier der Fehlerformen, die die Gliederung aufzählt, haben in den Quellen dieser Arbeitslinie keinen Anker, und der zentrale Begriff des Kapitels ist eine Prägung.[^19]
- Implementation Drift, unkontrolliertes Abhängigkeitswachstum, Overengineering und Automation Bias nennt die Gliederung, und in keiner der drei Quellen kommen sie vor. Die vergleichenden Fälle in Teil V wären der Ort, an dem sie Evidenz erhalten, und bis dahin behandelt das Kapitel an ihrer Stelle Fortpflanzung, Ansammlung und falsche Eindeutigkeit.
- Verification Debt ist ein Begriff dieses Buches. Keine Quelle dieser Arbeitslinie verwendet ihn, und seine Bestimmung hier ist aus den Assertions zur zweckgebundenen Acceptance und zu den vier Prüfebenen zusammengesetzt.
- Das diagnostische Verfahren zur Zuordnung eines Defekts zu einer Ebene steht als Frage und nicht als Methode. Die Dokumenttypologie der anderen Manuskriptlinie trägt ein diagnostisches Raster, das einen Defekt an ein zuständiges Dokument leitet, und Kapitel 15 ist der Ort, an dem beide zusammentreffen.
- Unautorisierte Klassifikation, von der Gliederung unter den Fehlerformen genannt, ist hier nur über das Interface behandelt, das falsche Eindeutigkeit erzeugt. Ein Fall, in dem eine erzeugte Klassifikation ohne Autorisierung in einen Datenbestand gelangt, gehört nach Teil V.

[^0]: Posit: diese Fehler nach ihrem Ursprung in Trajektorienlänge, Anordnung und Annahme zu gruppieren ist die eigene Klassifikation dieses Buches, und keine Quelle dieser Arbeitslinie ordnet sie so. Open evidence question: ob eine Menge dokumentierter agentischer Fehler in diese drei Gruppen fällt oder weitere verlangt.
[^1]: Grounded in [[30_assertions/an-early-error-propagates-along-the-trajectory]].
[^2]: Grounded in [[30_assertions/long-runs-accumulate-noise]].
[^3]: Grounded in [[30_assertions/the-bottleneck-shifts-from-model-to-context]].
[^4]: Grounded in [[30_assertions/the-interface-can-manufacture-false-certainty]].
[^5]: Grounded in [[30_assertions/implementation-tests-the-project-understanding]].
[^6]: Posit: die Ebenendiagnose stammt aus der Gliederung, und die Quellen belegen, dass ein Defekt außerhalb der Implementation entstehen kann, ohne ein Verfahren zu seiner Lokalisierung zu geben. Open evidence question: eine Menge dokumentierter Defekte, klassifiziert nach der Ebene, die ihre Korrektur tatsächlich verlangt hat.
[^7]: Grounded in [[30_assertions/findings-must-be-written-back]].
[^8]: Grounded in [[30_assertions/the-prompt-is-one-component-of-the-loop]].
[^9]: Posit: die Aussage, dass ein offener Zyklus jeden Lauf aus einem widerlegten Verständnis starten lässt, folgt aus der Write-back-Assertion und ist in keiner Quelle gemessen. Open evidence question: wie oft ein wiederkehrender Defekt in einem Projekt auf einen nie zurückgeschriebenen Befund zurückgeht.
[^10]: Grounded in [[30_assertions/self-revision-is-no-independent-verification]].
[^11]: Grounded in [[30_assertions/agents-produce-evidence-without-authority]].
[^12]: Grounded in [[30_assertions/independent-review-extends-coverage-not-authority]].
[^13]: Grounded in [[30_assertions/more-agents-raise-coordination-cost]].
[^14]: Grounded in [[30_assertions/increments-must-stay-inspectable]].
[^15]: Posit: Verification Debt ist die Prägung dieses Buches für die Ansammlung vorläufig angenommener erzeugter Arbeit, und keine Quelle dieser Arbeitslinie verwendet den Begriff. Open evidence question: ein Maß dafür, wie viel ungeprüfte erzeugte Ausgabe ein Projekt zu einem Zeitpunkt trägt.
[^16]: Grounded in [[30_assertions/acceptance-is-a-purpose-bound-decision]].
[^17]: Grounded in [[30_assertions/the-assessment-vocabulary-has-four-levels]].
[^18]: Grounded in [[30_assertions/formal-conformance-is-not-scholarly-adequacy]].
[^19]: Posit: die Lückenliste hält fest, was dieses Kapitel aus seinen eigenen Quellen nicht tragen kann. Open evidence question: ob die vergleichenden Fälle in Teil V dokumentierte Instanzen von Drift, Abhängigkeitswachstum, Overengineering und Automation Bias liefern.
