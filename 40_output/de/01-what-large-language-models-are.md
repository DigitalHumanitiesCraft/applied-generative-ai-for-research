---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/assistant-behaviour-has-three-shaping-layers]]", "[[30_assertions/attention-relates-positions-across-layers]]", "[[30_assertions/capability-evaluations-measure-different-things]]", "[[30_assertions/fluency-is-not-fidelity-to-the-source]]", "[[30_assertions/in-context-adaptation-changes-no-weights]]", "[[30_assertions/interpretability-shows-structure-without-a-theory]]", "[[30_assertions/llm-computes-next-token-probabilities]]", "[[30_assertions/model-output-is-a-candidate-representation]]", "[[30_assertions/model-output-stays-probabilistic]]", "[[30_assertions/parametric-knowledge-carries-no-provenance]]", "[[30_assertions/pretraining-and-posttraining-are-distinguishable-and-blurred]]", "[[30_assertions/prompt-engineering-is-an-external-search]]", "[[30_assertions/prompting-intervenes-in-the-current-computation]]", "[[30_assertions/representations-are-contextual-not-fixed]]", "[[30_assertions/social-fluency-is-no-evidence-of-authority]]", "[[30_assertions/the-assistant-is-a-stabilised-character]]", "[[30_assertions/the-capability-profile-is-jagged]]", "[[30_assertions/the-latent-program-space-models-prompt-effects]]", "[[30_assertions/the-model-boundary-is-not-the-system-boundary]]", "[[30_assertions/tokenisation-fixes-the-unit-of-computation]]", "[[30_assertions/training-objective-differs-from-acquired-capability]]"]
posits: 1
lang: de
part: "I. Generative Modelle als Forschungssysteme"
chapter: 1
title: "Was große Sprachmodelle sind"
topic: "[[Generative-Models]]"
feeding-sources: ["script chapter 2", "slide section AI Agents"]
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Was große Sprachmodelle sind

## Die Arbeitsweise

Die Ausgabe eines generativen Systems richtig zu lesen verlangt eine Vorstellung davon, wie sie entstanden ist, und diese Vorstellung fällt schmaler aus als eine Darstellung des gegenwärtigen Machine Learning. Forschende brauchen den Teil, der für die Lektüre trägt, denn eine Ausgabe ist eine Kandidatenrepräsentation, deren nächster Schritt der Vergleich mit dem Material ist, das sie zu repräsentieren beansprucht, und jede technische Eigenschaft im Folgenden verändert, wie dieser Vergleich zu führen ist.[^13]

Ein großes Sprachmodell erzeugt Text autoregressiv. Aus der bisher verfügbaren Eingabesequenz berechnet es eine Wahrscheinlichkeitsverteilung über das nächste Token, das ausgewählte Token wird Teil des Kontextes, und die Berechnung wiederholt sich bis zum Ende der Ausgabe.[^1] Was eine Leserin als fertige Antwort wahrnimmt, ist die Summe dieser Wiederholung, und kein Schritt darin schlägt in einem Faktenspeicher nach.

Trainingsziel und erworbene Fähigkeit fallen nicht zusammen. Next Token Prediction benennt das Optimierungsproblem, und es über heterogenes Material hinweg gut zu lösen verlangt Repräsentationen und Transformationen für Syntax, Begriffe, Relationen, Stile, Code und wiederkehrende Schlussmuster. Diese Strukturen tragen anschließend Arbeit, die das Ziel nie benannt hat. Das Ziel fragt nach der wahrscheinlichen Fortsetzung und lässt offen, ob eine Aussage wahr ist, sodass ein so optimiertes System breite Weltrepräsentationen aufbauen kann, während Wahrheit außerhalb dessen bleibt, was es zu schätzen gelernt hat.[^2]

Die Einheit, über der all das operiert, legt die Tokenisierung fest. Ein Tokenizer überführt Zeichenfolgen in diskrete Einheiten, die einem Wort, einem Wortteil oder einem Satzzeichen entsprechen können, und jede Einheit wird vor dem Eintritt in das Netz zu einer numerischen Kennung. Die Grenzen folgen einer technischen Abwägung zwischen Vokabulargröße, Sequenzlänge und der Fähigkeit, unbekannte Zeichenfolgen darzustellen, und sind deshalb sprachlich nicht intuitiv. Kontextkapazität, Eingabekosten und Ausgabelänge werden in diesen Einheiten gezählt, sodass ein seltener Eigenname in einer historischen Quelle ein Vielfaches des Budgets eines häufigen Wortes verbraucht.[^3]

Aus diesen Kennungen werden Vektoren. Ein Embedding liefert die erste Abbildung in einen hochdimensionalen Raum, in dem systematische Beziehungen zwischen wiederkehrenden Mustern entstehen können, und die bekannte Illustration, in der verwandte Wörter nahe beieinanderliegen, gibt eine erste Anschauung, ohne Bedeutung zu erklären. Diese erste Abbildung wird über das Netz hinweg wiederholt in Repräsentationen überführt, die von den umgebenden Tokens und der aktuellen Aufgabe abhängen, sodass zwei bedeutungsähnliche Sätze in unterschiedlichen Registern unterschiedliche interne Zustände bedingen können.[^4] Die Architektur, die diese Transformationen ausführt, ist der Transformer, in dem Attention über wiederholte Schichten hinweg Information an verschiedenen Positionen aufeinander wirken lässt, und die Wahrscheinlichkeit, die eine Fortsetzung schließlich erhält, ist das Ergebnis dieser geschichteten Berechnung.[^5]

Hier wird eine technische Tatsache zu einer methodischen. Prompt und Kontext verändern die dem Modell übergebene Tokensequenz und bedingen damit die Berechnung, aus der die nächsten Tokens hervorgehen, und unterschiedliche Formulierungen verändern die internen Aktivierungen hinter der Ausgabeverteilung. Ein Prompt ist deshalb ein Eingriff in eine Berechnung und keine Hülle um eine Antwort, die das System bereits hält.[^6]

## Was das Training hinterlässt

Pre-Training baut breite Repräsentationen aus großem heterogenem Material auf, Post-Training über Instruction Tuning, Preference Learning und verwandte Verfahren prägt, wie dieses Repertoire zum Ausdruck kommt. Das erste als Wissen und das zweite als Verhalten zu beschreiben ist eine Vereinfachung, weil Wissen und Fähigkeit im gesamten Training verschränkt bleiben und aktuelle Entwicklungspipelines Zwischenstufen enthalten können, die verschiedene Labore verschieden benennen.[^7] Eine Aussage darüber, was ein Modell in welcher Stufe gelernt hat, ist deshalb schwächere Evidenz, als sie aussieht.

Was das Training hinterlässt, ist keine abrufbare Kopie seines Materials. Training verändert Parameter, sodass statistische Struktur aus den Daten die spätere Generierung beeinflusst, und es bleibt keine adressierbare Fassung eines Trainingsdokuments zurück. Ein Modell kann deshalb einen Sachverhalt zutreffend beschreiben und zugleich die Quelle nicht benennen, aus der die Beschreibung stammt, und es führt kein verlässliches Seiten- oder Quellenregister.[^8] Für die Forschung ist damit eine praktische Frage entschieden. Parametrisches Wissen ist als Evidenz unbrauchbar, und die Teile einer Antwort, die Provenienz brauchen, müssen von dort kommen, wo das System zitieren kann.

Drei Informationsebenen sind deshalb auseinanderzuhalten, die gelernten Repräsentationen in den Parametern, die abrufbare Information in externen Ressourcen und die im aktuellen Kontext tatsächlich vorhandene Information. Die Grenze des Modells ist nicht die Grenze des Systems, sodass eine Aussage darüber, was ein System wissen kann, unbestimmt bleibt, solange sie nur das Modell benennt.[^9] Innerhalb des aktuellen Kontextes passt sich das Modell stark an Anweisungen, Beispiele und bereitgestelltes Material an, ohne dass ein Gewicht verändert wird, und genau das macht Kontext zu einer Gestaltungsfläche und Teil II überhaupt möglich.[^10]

## Was die Ausgabe ist

Die Ausgabe bleibt probabilistisch. Derselbe Prompt kann über mehrere Durchläufe unterschiedliche Ergebnisse erzeugen, und eine plausible Formulierung ist deshalb keine rekonstruierte Tatsache.[^11] Diese Eigenschaft überrascht am zuverlässigsten, wer aus der Datenbankarbeit kommt, wo dieselbe Abfrage dieselben Zeilen liefert.

Sprachliche Flüssigkeit verschärft das Problem. Eine erzeugte Transkription kann überzeugend zu lesen sein, während einzelne Lesungen falsch sind, und eine erzeugte Auszeichnung kann formal plausibel wirken und dennoch gegen die Projektrichtlinien verstoßen, sodass sprachliche Qualität und fachliche Verlässlichkeit getrennte Eigenschaften sind.[^12] Die erste nimmt eine Leserin unmittelbar wahr, weshalb eine Ausgabe als Kandidatenrepräsentation zu behandeln ist, deren nächster Schritt der Vergleich mit dem Material ist, das sie zu repräsentieren beansprucht.[^13]

Das Fähigkeitsprofil selbst ist ungleichmäßig. Frontier-Modelle lösen sehr schwierige Aufgaben und scheitern an benachbarten, die einfach aussehen, sodass sich ihre Kompetenz aus einem einzelnen Erfolg schwer hochrechnen lässt. Ausgaben können plausible, aber ungestützte Behauptungen enthalten, Modelle können Bias reproduzieren und einer geäußerten Überzeugung zustimmen, und ihre interne Verarbeitung ist nur teilweise verstanden.[^14] Messung behebt die Ungleichmäßigkeit nicht. Evaluationen zur Aufgabendauer, zur Anpassung an unbekannte Probleme, zum mathematischen Schließen und zum Verhalten in ausführbaren Umgebungen beantworten verschiedene Fragen, und sie als Punkte auf einer Intelligenzskala zu lesen verwirft, wozu jede gebaut wurde.[^15]

## Die Figur im Interface

Was einer Nutzerin antwortet, ist nicht das Netz. Die Assistentenfigur ist ein Verhaltensmuster, das durch Training, Laufzeitinstruktionen, Policy-Schichten und Produktgestaltung stabilisiert wird, und sie ist kein menschliches Gegenüber.[^16] Drei prägende Schichten sind zu trennen, Trainingsartefakte wie eine veröffentlichte Spezifikation, Character Training und Post-Training sowie der System Prompt, der zur Laufzeit in einem Deployment wirkt. Das Verhalten, dem eine Nutzerin begegnet, entsteht aus dem Zusammenspiel trainierter Parameter mit dem aktuellen Laufzeitkontext.[^17]

Die praktische Folge ist eine Warnung vor einem bestimmten Schluss. Modelle, die umfangreich auf menschlicher Kommunikation trainiert wurden, erzeugen überzeugendes soziales Verhalten, und Sicherheit, Empathie und Gesprächskompetenz sagen nichts darüber, ob die Behauptungen in einer Antwort zutreffen.[^18] Wer gelernt hat, Abschwächungen in der Prosa einer Kollegin als epistemisches Signal zu lesen, liest hier falsch, weil die Abschwächung eine stilistische Disposition der Assistentenfigur ist und kein Bericht über ihre Sicherheit.

## Ein Modell der Promptwirkung

Die bisherige Darstellung erklärt, dass Formulierung wirkt, und lässt offen, wie. Dieses Buch übernimmt dafür ein theoretisches Modell. In dieser Lesart enthält ein Modell ein großes Repertoire gelernter Verarbeitungstransformationen, und ein Prompt wirkt teilweise als Signal, das sie auswählt und kombiniert. Ein solches Vector Program ist eine verteilte Transformation über hochdimensionale Repräsentationen und Parameter und kein symbolisches Programm, das als abgegrenztes Objekt gespeichert wäre, und Verhaltensweisen wie Übersetzen, Zusammenfassen oder Klassifizieren sind wiederkehrende Muster aus Gewichten und aktuellem Aktivierungsverlauf.[^19] Iteratives Prompt Engineering ist dann eine externe Suche, in der eine Nutzerin die Adresse variiert und das resultierende Verhalten bewertet.[^20]

Interpretierbarkeitsforschung stützt die Form dieses Bildes, ohne es zu vollenden. Attribution Graphs und verwandte Verfahren rekonstruieren Teile interner Pfade, zeigen, dass bestimmte interne Strukturen mit beobachtbarem Verhalten zusammenhängen, und belegen, dass Eingriffe in Repräsentationen Ausgaben systematisch verändern. Daraus ergibt sich keine Karte, aus der sich die Wirkung eines natürlichsprachlichen Prompts vorhersagen ließe.[^21] Das Modell wird hier deshalb als Arbeitsdarstellung übernommen, die Beobachtungen ordnet, und Kapitel 4 zieht die praktische Folge, dass ein Prompting-Befund geprüft und nicht übertragen werden muss.

## Lücken

Drei Themen, die die Gliederung diesem Kapitel zuweist, haben in den Quellen dieser Arbeitslinie keinen Anker.[^22]
- Konfabulation wird in den Quellen als Eigenschaft genannt, ohne eine Definition, die sie vom gewöhnlichen Fehler trennt, sodass der Begriff hier noch nicht als Fachterminus verwendbar ist; nötig ist eine Quelle aus der Forschungsliteratur zu Halluzination und Kalibrierung.
- Die quantitativen Aussagen hinter dem ungleichmäßigen Fähigkeitsprofil, die Messungen zu Aufgabendauer und zur Anpassung an unbekannte Aufgaben, referieren die Lecture Notes im Vorbeigehen; eine tragfähige Verankerung verlangt die zugrunde liegenden Publikationen als eigene Datensätze.
- Die Darstellung von Inferenzverfahren und stochastischer Variation bleibt hier qualitativ, weil die Quellen die Variation beschreiben, ohne die Sampling-Parameter zu benennen, die sie erzeugen.

[^1]: Grounded in [[30_assertions/llm-computes-next-token-probabilities]].
[^2]: Grounded in [[30_assertions/training-objective-differs-from-acquired-capability]].
[^3]: Grounded in [[30_assertions/tokenisation-fixes-the-unit-of-computation]].
[^4]: Grounded in [[30_assertions/representations-are-contextual-not-fixed]].
[^5]: Grounded in [[30_assertions/attention-relates-positions-across-layers]].
[^6]: Grounded in [[30_assertions/prompting-intervenes-in-the-current-computation]].
[^7]: Grounded in [[30_assertions/pretraining-and-posttraining-are-distinguishable-and-blurred]].
[^8]: Grounded in [[30_assertions/parametric-knowledge-carries-no-provenance]].
[^9]: Grounded in [[30_assertions/the-model-boundary-is-not-the-system-boundary]].
[^10]: Grounded in [[30_assertions/in-context-adaptation-changes-no-weights]].
[^11]: Grounded in [[30_assertions/model-output-stays-probabilistic]].
[^12]: Grounded in [[30_assertions/fluency-is-not-fidelity-to-the-source]].
[^13]: Grounded in [[30_assertions/model-output-is-a-candidate-representation]].
[^14]: Grounded in [[30_assertions/the-capability-profile-is-jagged]].
[^15]: Grounded in [[30_assertions/capability-evaluations-measure-different-things]].
[^16]: Grounded in [[30_assertions/the-assistant-is-a-stabilised-character]].
[^17]: Grounded in [[30_assertions/assistant-behaviour-has-three-shaping-layers]].
[^18]: Grounded in [[30_assertions/social-fluency-is-no-evidence-of-authority]].
[^19]: Grounded in [[30_assertions/the-latent-program-space-models-prompt-effects]].
[^20]: Grounded in [[30_assertions/prompt-engineering-is-an-external-search]].
[^21]: Grounded in [[30_assertions/interpretability-shows-structure-without-a-theory]].
[^22]: Posit: die Lückenliste hält fest, was dieses Kapitel aus seinen eigenen Quellen nicht tragen kann. Open evidence question: welche Publikationen die Referenzschicht führen muss, bevor die quantitativen Aussagen dieses Kapitels direkt verankert werden können.
