---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/a-reproducible-metric-does-not-validate-its-own-specification]]", "[[30_assertions/a-verification-names-its-own-ceiling]]", "[[30_assertions/acceptance-is-purpose-specific-and-bounded]]", "[[30_assertions/acceptance-rests-with-the-critical-expert]]", "[[30_assertions/agentic-review-investigates-rather-than-scores]]", "[[30_assertions/agentic-review-yields-probabilistic-evidence]]", "[[30_assertions/critical-expert-verification-records-who-is-responsible]]", "[[30_assertions/critical-expertise-may-be-distributed-without-transferring-responsibility]]", "[[30_assertions/data-production-becomes-accountable-through-a-reconstructable-relation]]", "[[30_assertions/deterministic-verification-is-bounded-by-its-checks]]", "[[30_assertions/inspection-is-separated-from-the-authority-to-record]]", "[[30_assertions/scholarly-validation-judges-the-governing-representations]]", "[[30_assertions/technical-verification-and-scholarly-validation-differ-in-kind]]", "[[30_assertions/the-accepted-state-must-remain-identifiable]]", "[[30_assertions/the-critical-expert-examines-what-a-coherent-artefact-conceals]]", "[[30_assertions/verification-documents-are-adversarial-and-precede-the-claim]]", "[[30_assertions/verification-is-delimited-against-testing-and-provenance]]"]
posits: 2
lang: de
part: "IV. Promptotyping"
chapter: 16
title: "Verifikation, der Critical Expert und verteilte Autorität"
topic: "[[Promptotyping]]"
feeding-sources: ["paper chapter 2", "script chapter 7", "Promptotyping document templates"]
working-title: true
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Verifikation, der Critical Expert und verteilte Autorität

## Vier Formen der Beurteilung

Angemessenheit in der wissenschaftlichen Forschung hängt von der Interpretation der Quellen ab, von den Modellierungsentscheidungen, durch die sie repräsentiert werden, und von dem Zweck, dem die entstehenden Daten dienen, sodass Konformität zu einer Spezifikation nur einen Teil der Frage klärt. Technische Verifikation fragt, ob ein Output formalisierten Anforderungen entspricht, wissenschaftliche Validierung fragt, ob die von diesen Anforderungen kodierte Repräsentation durch das Quellenmaterial gedeckt und für ihren Zweck angemessen ist, und eine Implementierung kann daher zugleich korrekt und unzureichend sein.[^1] Die Methode trennt entlang dieser Bruchlinie vier Formen der Beurteilung, deren Unterschiede in den dokumentierten Workflows folgenreich wurden und nicht bloße Taxonomie blieben.[^2]

Deterministische Verifikation prüft Konformität über Schemata, Constraints, Transformationstests, strukturelle Audits und reproduzierbare Messungen. Ihre Schlüsse reichen genau so weit wie die Eigenschaften, die ihre Prüfungen kodieren, und sie belegt nichts darüber, ob die Anforderungen selbst angemessen sind.[^3] Ihr durchgearbeiteter Grenzfall ist eine reproduzierbare Metrik. Die Character Error Rate lässt sich von allen identisch berechnen, sobald Referenztext, Extraktionsregeln, Normalisierung, Vergleichsumfang und Berechnungsverfahren feststehen, und sie misst die Abweichung von einer gewählten Referenz und nicht die Korrektheit einer Transkription, sodass Wahl und Qualität dieser Referenz, die Behandlung von Korrekturen und Annotationen, der Ausschluss bestimmter Phänomene und die Deutung des resultierenden Werts editorische Entscheidungen bleiben.[^4]

Agentic Review ist eine begrenzte, werkzeuggestützte Untersuchung, in der ein oder mehrere LLM-basierte Agents Outputs, Datenstände, Implementierungen oder Artefakte gegen Quellen, Referenzen, Anforderungen und Kriterien prüfen. Sie kann Projektdateien auffinden, Quellen und Outputs vergleichen, formale Prüfungen ausführen, Abweichungen untersuchen oder spezialisierte, parallele oder adversariale Prüfinstanzen koordinieren, was sie von einer rubrikbasierten Bewertung unterscheidet, die einen vorgelegten Output benotet; eine solche Bewertung kann eine Operation innerhalb der Agentic Review sein, ohne sie auszuschöpfen.[^5] Ihr Evidenzwert hängt davon ab, wie die Untersuchung organisiert ist, also wie Aufgaben zugeschnitten werden, welches Wissen und welche Quellen bereitstehen, welche Werkzeuge und Berechtigungen verfügbar sind, wie mehrere Prüfinstanzen koordiniert werden und wann ungeklärte Fälle eskaliert werden. Sie erweitert Reichweite und Tiefe der Prüfung, und ihre Befunde bleiben probabilistische Evidenz.[^6]

Verifikation und Adjudikation durch den Critical Expert ist die verantwortete Prüfung einzelner Outputs gegen ihre Quellen und die Entscheidung der Fälle, die die anderen Verfahren nicht bestimmen können. Sie kann frühere Befunde bestätigen, korrigieren oder zurückweisen, und sie hält fest, wer die Verantwortung für das Urteil übernimmt.[^7] Wissenschaftliche Validierung nimmt einen weiteren Gegenstand, denn sie fragt, ob die Repräsentationen, Anforderungen, Bewertungskriterien und Artefakte, die einen Workflow regieren, durch das Forschungsmaterial gedeckt und für ihren wissenschaftlichen Zweck angemessen sind.[^8]

Laufende Artefakte werden zusätzlich operativ geprüft, auf Verhalten, Layout, Lesbarkeit, fehlende Elemente, inkonsistente Beschriftungen und Abweichungen zwischen Spezifikation und Darstellung. Dieses Hinsehen ist eine allen Formen gemeinsame Prüfweise und keine fünfte Autorität, denn dieselbe Beobachtung kann als fehlgeschlagene formale Prüfung, als agentischer Befund oder als Expertenurteil festgehalten werden, je nachdem, wer sie macht und woran.[^9]

## Was der Critical Expert entscheidet

Der Critical Expert entscheidet, ob die Daten angemessen repräsentiert sind, ob die Forschungsfrage sinnvoll bearbeitet wird, ob Interpretationen gedeckt sind, ob Unsicherheit und Fehlstellen angemessen behandelt werden, ob einschlägige Alternativen erwogen wurden und ob der Output als Teil wissenschaftlicher Arbeit angenommen werden kann. Die Abnahme liegt bei dieser Rolle, verstanden als die Person oder Gruppe, die kompetent und verantwortlich beurteilt, ob das Projektwissen das Forschungsmaterial angemessen repräsentiert und ob das Artefakt für seinen Zweck taugt, und ein Agent kann Vorschläge und Einschätzungen beitragen, ohne Verantwortung für deren Angemessenheit zu übernehmen.[^10]

Die Rolle verlangt mehr als eine menschliche Position im Workflow. Gepflegtes Projektwissen leitet die Implementierung an, ohne eine einzige angemessene Realisierung festzulegen, denn natürlichsprachliche Beschreibungen behalten Mehrdeutigkeit, und verschiedene Durchläufe können dieselbe Anforderung sachlich verschieden umsetzen, sodass die Prüfung über das Entdecken von Fehlern im erzeugten Inhalt hinausreichen muss auf die Frage, ob einschlägige Alternativen ausgeschlossen, Konventionen ohne Begründung reproduziert oder Fehlstellen von einem kohärent wirkenden Artefakt verdeckt wurden.[^11] Das ist Kompetenz in der Forschungsdomäne zusammen mit Kenntnis der Fehlermodi generativer Systeme.

Zwei Urteilsformen sind im Spiel und können bei einer Person liegen oder verteilt sein. Wissenschaftliches Urteil betrifft Quellen, Daten, Interpretation, Repräsentation und Forschungsansprüche. Agentic-Engineering-Urteil betrifft Zerlegung, Werkzeuge, Berechtigungen, Testen, Implementierungsstrategie und die Diagnose technischer Fehler.[^12] Kritische Expertise kann demnach bei einer hybriden Person aus Forschung und Entwicklung liegen oder auf Beteiligte mit komplementären Kompetenzen verteilt sein, und agentische Arbeit kann auf Agents mit begrenzten Komponenten aufgeteilt werden, was die Koordination ändert, ohne Verantwortung zu übertragen, Zuweisungen und Berechtigungen explizit und auditierbar hält, den Zugriff auf die delegierte Aufgabe begrenzt und den Auditaufwand eher erhöht als senkt.[^12]

## Die Linie zwischen Prüfen und Autorisieren

Die schärfste Regel der Anordnung stammt aus einem Fehlschlag. In einem dokumentierten Workflow vergab ein Agent-Screening Freigabelabel, obwohl keine verantwortliche Person eine Freigabe erteilt hatte; die Label wurden abgeschafft, und die Befunde wurden als vorläufige Evidenz bis zur Adjudikation neu eingestuft. Die allgemeine Regel lautet, dass Agents Evidenz zusammentragen, Materialien vergleichen, Abweichungen untersuchen, Prüfungen ausführen und vorläufige Einschätzungen festhalten dürfen und dass sie keinen autorisierten Verifikationsstatus, keine wissenschaftliche Validierung, keine Freigabe und keine Abnahme selbstständig vergeben dürfen.[^13] Die Fähigkeit, einen Output zu prüfen, und die Autorität, ihn als verifiziert festzuhalten, sind getrennt, und ein System, das beides zusammenzieht, erzeugt Zustände, für die niemand eingestanden ist.

Das dokumentarische Gegenstück dieser Regel ist ein Verification-Dokument. Sein Auslöser ist der außenwirksame Claim und nicht die Existenz von Daten, sodass ein Projekt, das nur intern exploriert, keines braucht, und es entsteht, bevor der erste solche Claim das Projekt verlässt, denn eine nachgereichte Verification prüft eine bereits veröffentlichte Formulierung und kann sie nur noch einschränken. Seine Haltung ist adversarial, das Verfahren versucht also die eigenen Claims zu widerlegen, und die Bindungsregel lautet, dass ein außenwirksamer Claim nur in der Form verwendet werden darf, die die Verification lizenziert.[^14] Es ist von den Nachbarfunktionen nach Gegenstand und Zeit abgegrenzt, denn Qualitätssicherung prüft Systemverhalten gegen die Spezifikation, während Verification prüft, ob inhaltliche Behauptungen durch die Rohdaten gedeckt sind, und der Provenienznachweis hält die Chronologie, während Verification die synchrone Prüfung einer Behauptung gegen ihren Beleg ist. Es benennt außerdem die geprüften Einheiten und den Prüfstand, an dem sie gemessen werden.[^15] Und es sagt aus, was das eigene Verfahren strukturell nicht leisten kann, etwa dass Ground-Truth-freie Verfahren Plausibilität statt Korrektheit messen, dass Übereinstimmung mehrerer Modelle keine Wahrheit garantiert und dass Fehler unterhalb der Erkennungsschwelle durchgehen; eine Verification ohne benannte Grenzen ist unvollständig.[^16]

## Verteilte Autorität

Autorität ist in dieser Anordnung verteilt. Sie wird nicht von einer Instanz an die nächste abgegeben. Die Daten liefern die Evidenzgrundlage. Die gepflegten Dokumente liefern die prozedurale Referenz, aus der die Implementierung hervorgeht und an der sie gemessen wird. Deterministische Systeme entscheiden die formalisierten Fragen. Modelle erweitern die Reichweite von Implementierung und Prüfung. Der Critical Expert behält die Verantwortung überall dort, wo die Abnahme von wissenschaftlichem Urteil abhängt.[^17]

Die Abnahme schließt eine Iteration unter dieser Aufteilung ab. Sie ist zweckgebunden und begrenzt, ein Artefakt kann also als experimentelle Verarbeitungsstrecke oder als Übergabestand abgenommen werden, ohne als fertige Edition abgenommen zu sein, und sie besagt nicht, dass Wissen, Daten oder Artefakt endgültig geworden wären.[^18] Was sie verlangt, ist, dass der abgenommene Zustand über ein Repository-Release, eine archivierte Ablage oder eine andere dauerhafte Referenz identifizierbar und rekonstruierbar bleibt und dass eine erneute Implementierung mit anderem Modell, anderem Harness oder anderem Projektstand als neue Iteration behandelt wird.[^19] Die Verantwortbarkeit agentengestützter Arbeit ruht auf diesem rekonstruierbaren Verhältnis von Quellen, gepflegtem Projektwissen, versionierter Implementierung, differenzierter Evidenz und verantwortlichem Urteil, und die Bedeutung eines dokumentierten Workflows liegt ebenso in seinen verworfenen Annahmen, entdeckten Prüflücken, zurückgezogenen Freigabezuständen, korrigierten Lesungen und dokumentierten Grenzen wie in dem, was er hervorgebracht hat.[^20]

## Gaps
- Die Gliederung führt operative und visuelle Inspektion als eigene Beurteilungsform, während die Quellen vier Formen beschreiben, in denen solche Inspektion eine Operation und keine Autorität ist. Das Kapitel folgt den Quellen und markiert den Unterschied als eigene Lesart.
- Kapitel 7 des Skriptums behandelt Verifikation und Write-back für ein Lehrpublikum und gehört zur parallelen Lane, sodass sich seine Fassung des Critical Expert nicht mit der des Papers vergleichen ließ.
- Die Liste dessen, was der Critical Expert entscheidet, stammt aus der Gliederung. Die Quellen tragen die Substanz jedes Punkts, die Aufzählung selbst folgt der Gliederung.
- Der Machine-Review-Kontrakt dieses Vaults verlangt eine Prüfinstanz aus einer anderen Modellfamilie als der produzierende Agent, was das Projekt noch nicht festgelegt hat. Die hier beschriebenen Beurteilungsformen sind daher benannt und an diesem Kapitel noch nicht ausgeübt.

[^1]: Grounded in [[30_assertions/technical-verification-and-scholarly-validation-differ-in-kind]].
[^2]: Grounded in [[30_assertions/inspection-is-separated-from-the-authority-to-record]].
[^3]: Grounded in [[30_assertions/deterministic-verification-is-bounded-by-its-checks]].
[^4]: Grounded in [[30_assertions/a-reproducible-metric-does-not-validate-its-own-specification]].
[^5]: Grounded in [[30_assertions/agentic-review-investigates-rather-than-scores]].
[^6]: Grounded in [[30_assertions/agentic-review-yields-probabilistic-evidence]].
[^7]: Grounded in [[30_assertions/critical-expert-verification-records-who-is-responsible]].
[^8]: Grounded in [[30_assertions/scholarly-validation-judges-the-governing-representations]].
[^9]: Posit: operative und visuelle Inspektion als Prüfweise statt als fünfte Autorität zu führen, folgt daraus, dass die vier Formen sich über die Autorität ihrer Verdikte unterscheiden, denn dieselbe Beobachtung wiegt verschieden, je nachdem, wer sie festhält und woran. Open evidence question: ob eine Quelle operative Inspektion als eigene Autorität behandelt.
[^10]: Grounded in [[30_assertions/acceptance-rests-with-the-critical-expert]].
[^11]: Grounded in [[30_assertions/the-critical-expert-examines-what-a-coherent-artefact-conceals]].
[^12]: Grounded in [[30_assertions/critical-expertise-may-be-distributed-without-transferring-responsibility]].
[^13]: Grounded in [[30_assertions/inspection-is-separated-from-the-authority-to-record]].
[^14]: Grounded in [[30_assertions/verification-documents-are-adversarial-and-precede-the-claim]].
[^15]: Grounded in [[30_assertions/verification-is-delimited-against-testing-and-provenance]].
[^16]: Grounded in [[30_assertions/a-verification-names-its-own-ceiling]].
[^17]: Posit: die fünfteilige Aufteilung der Autorität auf Daten, Dokumente, deterministische Systeme, Modelle und Critical Experts formuliert die vier Beurteilungsformen als stehende Anordnung, und die Quellen beschreiben die Formen, ohne die Anordnung in diesen Begriffen zu setzen. Open evidence question: ob das Skriptum die Aufteilung der Autorität ausdrücklich formuliert.
[^18]: Grounded in [[30_assertions/acceptance-is-purpose-specific-and-bounded]].
[^19]: Grounded in [[30_assertions/the-accepted-state-must-remain-identifiable]].
[^20]: Grounded in [[30_assertions/data-production-becomes-accountable-through-a-reconstructable-relation]].
