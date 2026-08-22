---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/acceptance-is-a-purpose-bound-decision]]", "[[30_assertions/agents-produce-evidence-without-authority]]", "[[30_assertions/fluency-is-not-fidelity-to-the-source]]", "[[30_assertions/formal-conformance-is-not-scholarly-adequacy]]", "[[30_assertions/independent-review-extends-coverage-not-authority]]", "[[30_assertions/model-output-is-a-candidate-representation]]", "[[30_assertions/model-output-stays-probabilistic]]", "[[30_assertions/parametric-knowledge-carries-no-provenance]]", "[[30_assertions/self-revision-is-no-independent-verification]]", "[[30_assertions/social-fluency-is-no-evidence-of-authority]]", "[[30_assertions/sycophancy-needs-a-procedural-countermeasure]]", "[[30_assertions/the-assessment-vocabulary-has-four-levels]]", "[[30_assertions/the-capability-profile-is-jagged]]", "[[30_assertions/the-critical-expert-designs-the-conditions]]", "[[30_assertions/the-epistemic-infrastructure-conditions-inspection]]", "[[30_assertions/the-model-boundary-is-not-the-system-boundary]]"]
posits: 2
lang: de
part: "I. Generative Modelle als Forschungssysteme"
chapter: 3
title: "Wissen, Evidenz und epistemische Autorität"
topic: "[[Generative-Models]]"
feeding-sources: ["script chapter 2", "slide section AI Agents"]
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Wissen, Evidenz und epistemische Autorität

## Was ein Modell wissen kann

Das Verb macht die meiste Mühe. Zu sagen, ein Modell wisse etwas, legt eine Beziehung zwischen einer Behauptung und ihren Gründen nahe, und die Beziehung, in der ein Modell tatsächlich steht, ist eine andere. Training verändert Parameter, sodass statistische Struktur aus den Daten die spätere Generierung beeinflusst, es bleibt keine adressierbare Fassung eines Trainingsdokuments zurück, und ein Modell kann deshalb einen Sachverhalt zutreffend beschreiben und zugleich die Quelle nicht benennen, aus der die Beschreibung stammt.[^1] Was in den Parametern liegt, ist als Evidenz unbrauchbar, wie zutreffend es auch sein mag.

Damit die Frage bearbeitbar wird, sind drei Informationsebenen auseinanderzuhalten, die gelernten Repräsentationen in den Parametern, die abrufbare Information in externen Ressourcen und die im aktuellen Kontext vorhandene Information. Die Grenze des Modells ist nicht die Grenze des Systems, sodass es von der Ebene abhängt, aus der eine Behauptung stammt, ob das System sie mit Evidenz stützen kann.[^2] Eine Behauptung aus der dritten Ebene lässt sich bis zu ihrer Stelle verfolgen, eine aus der zweiten bis zu ihrem Abruf, eine aus der ersten bis nirgendwohin.

An diesem letzten Fall bildet sich das Material dieses Buches. Ein gut lesbarer erzeugter Text ist kein Bericht darüber, was die Quellen sagen. Sprachliche Flüssigkeit, Grammatikalität und innere Kohärenz sagen nichts über Quellentreue, und eine Transkription kann überzeugend zu lesen sein, während einzelne Lesungen falsch sind.[^3] Die praktische Folge ist eine Regel über den Status. Jede Ausgabe gilt als Kandidatenrepräsentation, deren nächster Schritt der Vergleich mit dem Material ist, das sie zu repräsentieren beansprucht, denn Plausibilität ist keine Validierung.[^4]

## Die Risiken, die daraus folgen

Mehrere Risiken dieser Anordnung haben dieselbe Form. Die Ausgabe ist probabilistisch, sodass dieselbe Eingabe verschiedene Ergebnisse liefern kann und eine plausible Formulierung keine rekonstruierte Tatsache ist.[^5] Ausgaben können Behauptungen enthalten, die nichts stützt, Modelle können Bias reproduzieren, und ein System kann einer geäußerten Überzeugung zustimmen, während die interne Verarbeitung nur teilweise verstanden bleibt.[^6] Soziale Kompetenz macht jedes dieser Risiken schwerer bemerkbar. Sicherheit, Empathie und Gesprächsfluss sind Eigenschaften einer durch Training und Produktgestaltung stabilisierten Assistentenfigur, und keine davon sagt etwas darüber, ob die Behauptungen in einer Antwort zutreffen.[^7]

Gerade die Zustimmungsneigung lässt sich nicht durch besseres Fragen beantworten. Sie ist im Verfahren zu beantworten, indem Evidenz, Alternativen oder unabhängiges kritisches Review verlangt werden, wo Zustimmung zu einer geäußerten Position das Ergebnis prägen könnte, und indem unabhängige Kandidaten erzeugt, ihre Unterschiede geprüft und entschieden werden.[^8] Dieselbe Überlegung erklärt, warum ein Modell, das seine eigene Arbeit prüft, den Kreis nicht schließt. Self-Revision kann Fehler sichtbar machen und liefert keine unabhängige Verifikation, weil dasselbe System eigene Fehlannahmen übersehen oder nachträglich plausibel begründen kann, und was sie verlässlicher macht, sind explizite Kriterien, externe Tests und prüfbare Referenzen außerhalb des Modells.[^9]

Der Verlust der Provenienz verdient eine eigene Erwähnung, weil er das Risiko ist, das am leisesten Schaden anrichtet. Eine wohlgeformte Antwort, die eine unbelegte Behauptung aufgenommen hat, sieht genauso aus wie eine wohlgeformte Antwort, die das nicht getan hat, und der Unterschied wird erst sichtbar, wo die Behauptung zurückverfolgt wird. Das ist der Grund, weshalb der Vault hinter diesem Buch jeden tragenden Satz an eine Quellenstelle bindet, und der Grund, weshalb diese Bindung maschinell und nicht erinnert sein muss.[^10]

## Vier Arten der Prüfung

Sobald Ausgaben als Kandidaten gelten, muss die Prüfung organisiert werden. Vier Formen sind zu unterscheiden und werden häufig verwechselt. Evaluation misst Ausgaben, Modelle oder Workflows an expliziten Kriterien und kann quantitativ oder qualitativ sein. Technische Verifikation fragt nach Konformität mit formalisierten Anforderungen und lässt sich genau deshalb oft automatisieren. Fachliche Validierung fragt, ob eine Repräsentation der Quelle, dem Zweck und dem disziplinären Kontext angemessen ist. Acceptance ist die Entscheidung, einen identifizierten Zustand für einen benannten Zweck zu verwenden, und sie bleibt nötig, nachdem die anderen drei gelaufen sind.[^11]

Die zweite und die dritte Form gehen auf eine Weise auseinander, die trägt. Gültige Syntax beweist, dass die Syntax stimmt, und Schemakonformität beweist, dass die formalen Regeln eingehalten wurden, während die Fragen, ob eine Transkription ihrer Quelle entspricht, ob editorische Unsicherheit angemessen repräsentiert ist, ob ein Interface die vorgesehenen Interpretationshandlungen stützt und ob Modellierungsentscheidungen sichtbar bleiben oder naturalisiert werden, von anderer Art sind. Ein Artefakt kann jede formale Prüfung bestehen und an allen scheitern.[^12]

Acceptance muss deshalb ihren Zweck benennen. Ein technisch verifiziertes Artefakt kann fachlich ungeeignet sein und ein fachlich interessanter Demonstrator publikationsuntauglich, sodass eine Acceptance, die nicht sagt, wofür sie den Zustand annimmt, mehr behauptet, als die Evidenz trägt.[^13]

## Wo die Autorität liegt

Agents und Validatoren können Fehler lokalisieren, Kriterien anwenden, Unterschiede berichten und Evidenz zusammenstellen, und nichts davon überträgt die Entscheidung. Expertise wird durch diese Anordnung nicht überflüssig, sie verlagert sich auf das Bestimmen von Zwecken, das Explizieren des relevanten Wissens, das Festlegen von Modellierungsunterscheidungen, das Setzen von Einschränkungen, das Entwerfen von Bewertungskriterien und die Entscheidung darüber, wie ein Stück Evidenz den Status einer Ausgabe verändert.[^14]

Die Rolle, die das trägt, ist der Critical Expert. Sie hält das Urteil überall dort, wo Prüfung Quellenkenntnis, Interpretation oder eine Designentscheidung verlangt, und sie entscheidet, welche Lesung vertretbar ist, ob eine Modellierung der Quelle entspricht, ob eine Oberfläche fachliche Unterscheidungen erhält und ob ein Zustand für seinen Zweck angenommen wird. Sie ist eine verantwortliche Autorität im Projekt und nicht eine bestimmte Person, und zu ihrer Arbeit gehören Provenienz, Validierungsregeln, Akzeptanzkriterien und Verfahren im Umgang mit Unsicherheit.[^15] Die Rolle als menschlichen Endkontrollpunkt zu lesen verfehlt ihre Stellung im Ablauf, weil das meiste ihrer Arbeit geschieht, bevor etwas erzeugt wird.

Mehr Reviewer ersetzen sie nicht. Mehrere unabhängige Prüfinstanzen können Uneinigkeit sichtbar machen und verdächtige Fälle lokalisieren, und die Evidenz aus Schemata, Tests, Quellenvergleichen und Domänenwissen bleibt wichtiger als Übereinstimmung zwischen ihnen, sodass der Zweck der Orchestrierung mehrerer Instanzen eine strukturierte Trajektorie unabhängiger Arbeit ist und keine höhere Zahl von Modellaufrufen.[^16]

Möglich wird all das durch eine Anordnung und nicht durch eine Komponente. Dateien, Projektwissen, Schemata, Tests, Provenienzangaben, Modellausgaben und editorische Entscheidungen bilden gemeinsam die Bedingungen, unter denen eine erzeugte Repräsentation kritisiert, validiert und für einen Zweck angenommen werden kann, und die Frage, die ein Projekt beantworten muss, lautet, unter welchen technischen und epistemischen Bedingungen seine Ausgaben inspiziert und verwendet werden können.[^17] Teil II baut diese Anordnung, Teil III organisiert die Arbeit, die darin läuft.

## Lücken

Drei der Risiken, die die Gliederung diesem Kapitel zuweist, lassen sich nicht auf der Ebene behandeln, die sie unterstellt.[^18]
- Konfabulation erscheint in den Quellen als aufgezählte Eigenschaft ohne eine Definition, die sie vom gewöhnlichen Fehler trennt; das Kapitel nennt deshalb die probabilistische Eigenschaft und die ungestützte Behauptung und vermeidet den Begriff als Fachterminus.
- Unkalibrierte Konfidenz wird hier über die Assertion zur sozialen Flüssigkeit behandelt, die die Art einer Antwort betrifft; eine Aussage über Kalibrierung im strengen Sinn verlangt eine Quelle, die geäußerte Sicherheit gegen Trefferquote misst.
- Konventionelle, aber unangemessene Repräsentationen, von der Gliederung genannt, haben in diesen Quellen keinen Anker. Das Vault-Dokument behandelt die Struktur eines Bestandes als bedeutungstragend, ohne konventionelle Repräsentationen des Forschungsmaterials zu berühren, sodass das Thema bei den vergleichenden Fällen in Kapitel 17 bleibt.

[^1]: Grounded in [[30_assertions/parametric-knowledge-carries-no-provenance]].
[^2]: Grounded in [[30_assertions/the-model-boundary-is-not-the-system-boundary]].
[^3]: Grounded in [[30_assertions/fluency-is-not-fidelity-to-the-source]].
[^4]: Grounded in [[30_assertions/model-output-is-a-candidate-representation]].
[^5]: Grounded in [[30_assertions/model-output-stays-probabilistic]].
[^6]: Grounded in [[30_assertions/the-capability-profile-is-jagged]].
[^7]: Grounded in [[30_assertions/social-fluency-is-no-evidence-of-authority]].
[^8]: Grounded in [[30_assertions/sycophancy-needs-a-procedural-countermeasure]].
[^9]: Grounded in [[30_assertions/self-revision-is-no-independent-verification]].
[^10]: Posit: dass eine unbelegte Übernahme in einer wohlgeformten Antwort unsichtbar bleibt, folgt aus den Assertions zu Provenienz und Flüssigkeit und ist in keiner Quelle gemessen. Open evidence question: wie oft Lesende eine ungestützte Behauptung in einem flüssigen erzeugten Text bemerken, ohne sie zurückzuverfolgen.
[^11]: Grounded in [[30_assertions/the-assessment-vocabulary-has-four-levels]].
[^12]: Grounded in [[30_assertions/formal-conformance-is-not-scholarly-adequacy]].
[^13]: Grounded in [[30_assertions/acceptance-is-a-purpose-bound-decision]].
[^14]: Grounded in [[30_assertions/agents-produce-evidence-without-authority]].
[^15]: Grounded in [[30_assertions/the-critical-expert-designs-the-conditions]].
[^16]: Grounded in [[30_assertions/independent-review-extends-coverage-not-authority]].
[^17]: Grounded in [[30_assertions/the-epistemic-infrastructure-conditions-inspection]].
[^18]: Posit: die Lückenliste hält fest, was dieses Kapitel aus seinen eigenen Quellen nicht tragen kann. Open evidence question: welche Publikation zur Kalibrierung es dem Kapitel erlauben würde, ein gemessenes Verhältnis zwischen geäußerter Sicherheit und Trefferquote zu nennen.
