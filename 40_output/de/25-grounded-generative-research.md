---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/a-research-artefact-is-a-project-specific-operational-form]]", "[[30_assertions/acceptance-rests-with-the-critical-expert]]", "[[30_assertions/agentic-engineering-organises-extended-model-mediated-work]]", "[[30_assertions/amplification-rather-than-transfer-of-authority]]", "[[30_assertions/capable-systems-widen-the-span-between-production-and-acceptance]]", "[[30_assertions/context-and-agentic-engineering-are-interdependent]]", "[[30_assertions/context-engineering-organises-the-informational-environment]]", "[[30_assertions/data-governance-bounds-what-may-be-processed]]", "[[30_assertions/distillation-is-not-summarisation-or-compression]]", "[[30_assertions/inspection-is-separated-from-the-authority-to-record]]", "[[30_assertions/models-shift-the-cost-of-project-specific-implementation]]", "[[30_assertions/promptotyping-is-a-knowledge-driven-method]]", "[[30_assertions/software-operationalises-only-encoded-distinctions]]", "[[30_assertions/technical-verification-and-scholarly-validation-differ-in-kind]]", "[[30_assertions/the-artefact-produces-no-knowledge-on-its-own]]", "[[30_assertions/the-critical-expert-examines-what-a-coherent-artefact-conceals]]", "[[30_assertions/the-knowledge-base-is-a-set-of-interrelated-documents]]", "[[30_assertions/the-method-was-consolidated-from-one-practice]]", "[[30_assertions/the-significance-is-modal-rather-than-economic]]", "[[30_assertions/write-back-makes-a-finding-durable]]"]
posits: 1
lang: de
part: Frame
chapter: 25
title: "Grounded Generative Research"
feeding-sources: ["all parts of the feeding map"]
working-title: true
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Grounded Generative Research

## Der Übergang ist nicht neutral

Generative Systeme verringern den Umfang manueller Formalisierung, der zwischen einer wissenschaftlichen Beschreibung und einer ausführbaren computationellen Form nötig ist. Analysen, Transformationen, Oberflächen und Forschungssoftware lassen sich aus natürlichsprachlichen Spezifikationen und strukturierten Daten ableiten, und Teile des Implementierungsaufwands, die projektspezifische Entwicklung für einzelne Forschende und kleine Projekte einmal unpraktikabel machten, sind erschwinglich geworden.[^1]

Diese Fähigkeit erzeugt keinen neutralen Übergang vom Forschungsmaterial zum computationellen Output. Forschungsdaten sind selektive Repräsentationen, in denen bestimmte Aspekte des Materials für einen definierten Zweck computationell explizit gemacht sind, und was als Forschungsdatum zählt, hängt vom Kontext ab, in dem das Material ausgewählt und interpretiert wurde.[^2] Kontext wird für bestimmte Zwecke konstruiert statt einmal zusammengestellt, denn dasselbe Material muss anders destilliert werden, sobald sich Zweck oder intendiertes Artefakt ändern.[^3] Spezifikationen bleiben unvollständig, denn natürlichsprachliche Beschreibungen behalten Mehrdeutigkeit, und verschiedene Durchläufe können dieselbe Anforderung sachlich verschieden umsetzen.[^4] Erzeugte Implementierung ist probabilistisch, wo eine Struktur erst erkannt oder interpretiert werden muss statt abgebildet.[^1] Und jedes Forschungsartefakt operationalisiert Entscheidungen darüber, was sichtbar, vergleichbar, veränderbar oder prüfbar wird, denn Software verarbeitet nur, was in Strukturen kodiert ist, die ihr Repräsentationsmodell trägt.[^5]

Die methodische Aufgabe, die daraus folgt, ist der Bau von Umgebungen, in denen wissenschaftliches Wissen agentische Arbeit anleitet und in denen erzeugte Outputs gegen ihre evidentiellen und begrifflichen Grundlagen prüfbar bleiben. Agents von der Wissenschaft unabhängig zu machen ist ein anderes Vorhaben, und dieses Buch hat es nicht verfolgt.[^20]

## Fünf verbundene Begriffe

Das Argument lief über fünf Praktiken, die zusammengehören statt zu konkurrieren.[^21]

Prompt Engineering ist der systematische Entwurf und die Bewertung von Modelleingaben, also die iterative Entwicklung eines Prompts über Änderungen an seinem Inhalt oder an den auf ihn angewandten Techniken. Context Engineering erweitert das vom einzelnen Prompt auf die informationelle Umgebung, in der Prompts interpretiert werden, und umfasst Auswahl, Organisation, Pflege und Bereitstellung dessen, was ein modellbasiertes System braucht, ohne darin zu bestehen, alles verfügbare Material in ein Kontextfenster zu legen.[^6] Knowledge Engineering liefert die dauerhafte Repräsentation und Steuerung dessen, was ein Projekt für den Fall hält, und nimmt in dieser Methode die Form gepflegter Dokumente an, die Daten, Anforderungen und Repräsentationsentscheidungen festhalten.[^7] Agentic Engineering organisiert die ausgedehnte, werkzeuggestützte Arbeit eines Agents und regelt, wie Aufgaben zerlegt werden, wie Werkzeuge eingesetzt werden, wann menschliches Eingreifen nötig ist und wie die Arbeit geprüft und fortgesetzt wird.[^8] Promptotyping ordnet alle vier zu einer Methode, die strukturierte Forschungsdaten und wissenschaftliche Spezifikationen in prüfbare Forschungsartefakte übersetzt, mit einer versionierten Projektwissensbasis als organisierender Struktur und Write-back als dem Mechanismus, der Befunde dauerhaft macht.[^9]

Die Wissensumgebung, die diese Praktiken verbindet, ist die gepflegte Wissensbasis, deren Dokumente begrenzte Repräsentationen aus umfangreicherem Material sind, für menschliche Prüfung und Revision gepflegt und für die Arbeitskontexte von Agents verfügbar.[^7] Der Grounded Vault ist die Form, die dieses Buch dieser Umgebung gibt, und er ist Gegenstand eines früheren Teils.

Die wissenschaftliche Autorität liegt beim Critical Expert überall dort, wo die Abnahme von Interpretation, Kontextualisierung, Quellenkritik und fachlichem Urteil abhängt, verstanden als die Person oder Gruppe, die kompetent und verantwortlich beurteilt, ob das Projektwissen das Material angemessen repräsentiert und ob das Artefakt für seinen Zweck taugt.[^10] Die Linie, die die Anordnung arbeiten lässt, verläuft zwischen dem Prüfen eines Outputs und seiner Autorisierung, denn Agents dürfen Evidenz zusammentragen, Materialien vergleichen, Abweichungen untersuchen, Prüfungen ausführen und vorläufige Einschätzungen festhalten, und sie dürfen keinen autorisierten Verifikationsstatus, keine wissenschaftliche Validierung, keine Freigabe und keine Abnahme selbstständig vergeben.[^11]

## Was das Feld definiert

Applied Generative AI for Research ist über eine methodische Anordnung definiert und nicht über die Verwendung eines bestimmten Modells oder Werkzeugs. Was die Anordnung zusammenhält, ist eine Menge von Relationen, die explizit bleiben, also die Relation eines Outputs zu der Evidenz, die ihn stützt, einer Spezifikation zu dem Wissen, aus dem sie geschrieben wurde, einer Ausführung zu dem Kontext, den sie erhalten hat, eines Befunds zu dem Dokument, das er ändert, und eines abgenommenen Zustands zu der Person, die ihn abgenommen hat.[^12]

Zwei Unterscheidungen tragen davon das meiste. Technische Verifikation fragt, ob ein Output formalisierten Anforderungen entspricht, und wissenschaftliche Validierung fragt, ob die von diesen Anforderungen kodierte Repräsentation durch das Material gedeckt und für ihren Zweck angemessen ist, sodass eine Implementierung zugleich korrekt und unzureichend sein kann.[^13] Und eine Korrektur wird methodisch folgenreich, sobald sie in das gepflegte Projektwissen eingearbeitet wird, statt auf die aktuelle Implementierung beschränkt zu bleiben, was ein Projekt davon abhält, dieselbe Lehre erneut zu ziehen.[^14]

Generative Systeme können Forschungsarbeit unter Bedingungen verstärken, die sich benennen lassen. Outputs müssen in etwas verankert sein, das eine lesende Person erreichen kann. Handlungen müssen durch Berechtigungen und einen prüfbaren Umfang begrenzt sein, und die Zulässigkeit von Material und Arbeitsablauf wird außerhalb der Methode entschieden.[^15] Transformationen müssen prüfbar bleiben, und Grenzen müssen dokumentiert sein, statt entdeckt zu werden. Ansprüche müssen der kritischen wissenschaftlichen Prüfung zugänglich bleiben.[^10]

## Was das Buch gezeigt hat und was nicht

Die Evidenz für diese Bedingungen stammt aus einer dokumentierten Praxis und nicht aus einem kontrollierten Vergleich. Sie wurde vor allem über Projekte konsolidiert, die eine hybride Person aus Forschung und Entwicklung geführt hat, die Fälle bilden keine repräsentative Stichprobe, ihre Dokumentation unterliegt Selektionseffekten, und beobachtete Verbesserungen lassen sich nicht sauber der Methode statt leistungsfähigeren Systemen, besseren Werkzeugen oder gewachsener Erfahrung zurechnen.[^16] Was die Praxis stützt, ist ein modaler Anspruch, denn Formen projektspezifischer Implementierung, die bislang außerhalb der praktischen Mittel einzelner Forschender und kleiner Projekte lagen, wurden machbar, und sie stützt keinen Anspruch darauf, dass die Methode schneller, billiger oder verlässlicher wäre als die Alternativen.[^17]

Das Argument für die Anordnung ruht daher nicht auf einem gemessenen Vorteil. Es ruht auf der Beobachtung, dass der Abstand zwischen dem, was Agents herstellen können, und dem, was Forschende verantwortbar annehmen können, mit der Leistungsfähigkeit der Systeme wächst, und dass gepflegtes Wissen, differenzierte Prüfung, Write-back und zweckgebundene Abnahme die Mittel sind, mit denen dieser Abstand steuerbar bleibt.[^18] Innerhalb des Geltungsbereichs, den dieses Buch erklärt hat, ist der Beitrag modellbasierter Agents zur wissenschaftlichen Arbeit Verstärkung, und die Kompetenz und das verantwortete Urteil, die sie voraussetzt, bleiben unverzichtbar.[^19]

## Gaps
- Prompt Engineering, Knowledge Engineering und der Grounded Vault sind Gegenstand der Teile I bis III, die die parallele Schreiblane aus Skriptum, Foliensatz und Vault-Dokument schreibt. Dieser Schluss formuliert sie aus den im Promptotyping-Topic verfügbaren Assertions und wird zu revidieren sein, sobald diese Teile und ihre Assertions vorliegen.
- Knowledge Engineering hat in den hier destillierten Quellen keinen definitorischen Anker, sodass seine Behandlung darauf ruht, was der Dokumentensatz der Methode tut, und nicht auf einer Definition.
- Die fünf Begriffe sind in der Gliederung als das verbundene Argument des Buches benannt. Ihre Anordnung folgt hier der Gliederung, und die Relation zwischen ihnen ist pro Begriff verankert und nicht als Ganzes.
- Der Schluss ist geschrieben, bevor die Teile I bis III existieren. Seine Aussagen darüber, was das Buch gezeigt hat, sind daher Aussagen über die Teile IV bis VI.

[^1]: Grounded in [[30_assertions/models-shift-the-cost-of-project-specific-implementation]].
[^2]: Grounded in [[30_assertions/a-research-artefact-is-a-project-specific-operational-form]].
[^3]: Grounded in [[30_assertions/distillation-is-not-summarisation-or-compression]].
[^4]: Grounded in [[30_assertions/the-critical-expert-examines-what-a-coherent-artefact-conceals]].
[^5]: Grounded in [[30_assertions/software-operationalises-only-encoded-distinctions]].
[^6]: Grounded in [[30_assertions/context-engineering-organises-the-informational-environment]].
[^7]: Grounded in [[30_assertions/the-knowledge-base-is-a-set-of-interrelated-documents]].
[^8]: Grounded in [[30_assertions/agentic-engineering-organises-extended-model-mediated-work]].
[^9]: Grounded in [[30_assertions/promptotyping-is-a-knowledge-driven-method]].
[^10]: Grounded in [[30_assertions/acceptance-rests-with-the-critical-expert]].
[^11]: Grounded in [[30_assertions/inspection-is-separated-from-the-authority-to-record]].
[^12]: Posit: fünf Relationen zu benennen, die explizit bleiben müssen, formuliert die Anordnung der vorangegangenen Teile in einem Satz, und keine Quelle setzt die Anordnung in dieser Form. Open evidence question: ob sich zeigen lässt, dass ein Projekt am Verlust genau einer dieser Relationen scheitert, während die übrigen halten.
[^13]: Grounded in [[30_assertions/technical-verification-and-scholarly-validation-differ-in-kind]].
[^14]: Grounded in [[30_assertions/write-back-makes-a-finding-durable]].
[^15]: Grounded in [[30_assertions/data-governance-bounds-what-may-be-processed]].
[^16]: Grounded in [[30_assertions/the-method-was-consolidated-from-one-practice]].
[^17]: Grounded in [[30_assertions/the-significance-is-modal-rather-than-economic]].
[^18]: Grounded in [[30_assertions/capable-systems-widen-the-span-between-production-and-acceptance]].
[^19]: Grounded in [[30_assertions/amplification-rather-than-transfer-of-authority]].
[^20]: Grounded in [[30_assertions/the-artefact-produces-no-knowledge-on-its-own]].
[^21]: Grounded in [[30_assertions/context-and-agentic-engineering-are-interdependent]].
