---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/a-knowledge-base-is-tested-by-bounded-continuation-tasks]]", "[[30_assertions/a-wrong-output-is-diagnosed-by-document-type]]", "[[30_assertions/independent-transfer-is-evaluated-through-sustained-work]]", "[[30_assertions/teaching-cases-do-not-establish-independent-continuation]]", "[[30_assertions/technical-verification-and-scholarly-validation-differ-in-kind]]", "[[30_assertions/the-account-must-be-proportionate-to-what-is-delegated]]", "[[30_assertions/the-benefit-of-the-method-is-distributed-unevenly]]", "[[30_assertions/the-boundary-to-research-software-engineering]]", "[[30_assertions/the-method-cannot-supply-missing-competence]]", "[[30_assertions/the-method-redistributes-implementation-labour]]", "[[30_assertions/the-sufficiency-of-distillation-is-practical]]", "[[30_assertions/transfer-would-require-adaptation]]", "[[30_assertions/transferability-differs-from-exact-reproduction]]"]
posits: 3
lang: de
part: "V. Research Artefacts and Comparative Cases"
chapter: 20
title: "Lehre, Transfer und asymmetrische Verstärkung"
topic: "[[Research-Artefacts]]"
feeding-sources: ["paper chapters 2.3 and 3"]
working-title: true
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Lehre, Transfer und asymmetrische Verstärkung

## Was Lehrfälle zeigen können

Eine aus einer Praxis konsolidierte Methode wirft die Frage auf, ob sie sich überträgt, und die Lehre ist der Ort, an dem diese Frage zuerst gestellt wird. Die verfügbare Evidenz ist begrenzt. Lehrfälle zeigen, dass Teilnehmende unter angeleiteten Bedingungen mit strukturierten Dokumenten und erzeugten Implementierungen arbeiten können, und sie zeigen nicht, dass Teilnehmende solche Arbeit über ein längeres Projekt hinweg selbstständig fortsetzen.[^1] Die Unterscheidung zählt, weil das angeleitete Abschließen einer Übung und das unbegleitete Fortführen eines Projekts Verschiedenes prüfen und nur das Zweite über Transfer spricht.

Der stärkere Test ist in den Quellen formuliert und von ihnen nicht erfüllt. Neue fachliche Beteiligte sollten die Methodenspezifikation, das einschlägige Projektmaterial und Zugang zu einer geeigneten technischen Umgebung erhalten und danach einen begrenzten Promptotype entwickeln und beurteilen, ohne dass die ursprüngliche Praxis weiter eingreift, wobei erfolgreiche, gescheiterte und abgebrochene Wege erhalten bleiben, Änderungen an Projektwissen, Artefakten, menschlichem Eingriff, externer Hilfe und Abnahmegründen festgehalten werden und Modell und Harness als experimentelle Variablen statt als unsichtbare Hintergrundbedingungen behandelt werden.[^2] Eine begrenzte Fortsetzungsaufgabe ist die kleinere Fassung desselben Tests, in der unabhängige Beteiligte das Projekt erklären, eine ausgewählte Abweichung diagnostizieren oder eine abgegrenzte Implementierungsaufgabe aus den gepflegten Dokumenten fortsetzen und beobachtete Schwierigkeiten, soweit möglich, dokumentarischen, technischen, zugangsbezogenen oder kompetenzbezogenen Grenzen zugeordnet werden.[^3]

Transfer ist außerdem von Reproduktion zu unterscheiden. Eine andere Person kann die Methode anwenden und ein anderes Artefakt mit anderen Dokumenten, Modellen, Werkzeugen und Projektstrukturen herstellen, weshalb Transfer verlangt, dass die methodischen Kernrelationen ohne undokumentierten Eingriff der Urheberschaft hergestellt, angewandt und rekonstruiert werden.[^4] Und die Methode selbst bedürfte auf dem Weg aus ihrem Feld heraus einer Anpassung, denn die Relation von gepflegtem Wissen, begrenzter Implementierung, Prüfung, Write-back, differenzierter Kontrolle und verantwortlichem Urteil ist nicht von sich aus auf die Geisteswissenschaften beschränkt, während die Methode gegen ein spezifisch geisteswissenschaftliches Schwierigkeitsprofil aus heterogenen Quellen, interpretativer Modellierung, unvollständiger Evidenz und Angemessenheitsformen entwickelt wurde, die technische Konformität nicht entscheidet.[^5]

## Asymmetrische Verstärkung

Der Begriff, der dieses Kapitel ordnet, benennt eine Ungleichverteilung. Promptotyping kann die praktische Reichweite artikulierter wissenschaftlicher und technischer Kompetenz erweitern, während sein Nutzen von Datenqualität, verfügbarem Wissen, Zugang zu leistungsfähigen Systemen und der Fähigkeit abhängt, deren Outputs zu prüfen, sodass Forschende und Institutionen mit stärkerer Expertise, Infrastruktur und Prüfkapazität überproportional profitieren können.[^6] Dieselbe Ungleichverteilung tritt innerhalb eines Projekts auf, wo Fachwissenschaft zusätzliche Aufsichtsarbeit übernehmen kann, Research Software Engineers technische Schulden erben können und die für die Prüfung Verantwortlichen plausibleren Outputs ohne entsprechende Mittel oder Autorität gegenüberstehen.[^6]

Zwei Mechanismen dahinter sind in früheren Kapiteln bereits festgehalten. Die Methode verteilt Implementierungsarbeit um, statt sie zu beseitigen, weshalb eine Evaluation verringerten Aufwand von verlagertem, neu entstandenem und aufgeschobenem Aufwand unterscheiden muss, und die kombinierte Last aus Wissenspflege, Koordination agentischer Arbeit und Erhalt eines prüfbaren Zustands wurde in den dokumentierten Fällen nicht gemessen.[^7] Und die Methode kann kein Domänenwissen liefern, das die Beteiligten nicht besitzen oder nicht als einschlägig erkennen, denn Vorlagen und gepflegte Dokumente machen Annahmen explizit und revidierbar, ohne sie bereitzustellen, während unzureichendes Projektwissen einen Agenten zu einer Implementierung führen kann, die kohärent, funktionsfähig und wissenschaftlich unzureichend ist.[^8]

Zusammengelesen geben diese beiden dem Begriff seine Schärfe. Die Fähigkeit, die den Nutzen am stärksten bestimmt, ist die Fähigkeit zu bemerken, dass etwas nicht stimmt, und genau diese Fähigkeit ist ungleich verteilt.[^9]

## Was die Lehre deshalb abdecken muss

Lehre kann sich nicht auf die Formulierung von Prompts beschränken. Sie muss Modellkompetenz abdecken, also was generative Systeme tun und wie sie versagen; Forschungsdatenkompetenz, also was ein Datenbestand repräsentiert und wo er aufhört zu tragen; die Organisation von Kontext und Wissen, also was in ein gepflegtes Dokument gehört und was in einen Arbeitskontext; Spezifikation, also die Übersetzung wissenschaftlicher Praxis in Aussagen, die eine Implementierung anleiten; Fehlerdiagnose; Prüfung; und das Bewusstsein für die Grenze zum Research Software Engineering.[^10]

Drei dieser Punkte haben in der Methode selbst eine prüfbare Form. Die Fehlerdiagnose hat ein Raster, denn ein formal falscher Output, ein Stilbruch oder ein ignoriertes Verbot wird im Action Document diagnostiziert, während ein inhaltlich falscher Output in den Wissensdokumenten diagnostiziert wird.[^11] Die Prüfung hat eine Unterscheidung, denn technische Verifikation fragt nach der Konformität zu formalisierten Anforderungen, während wissenschaftliche Validierung fragt, ob die repräsentierte Anordnung durch das Material gedeckt und für ihren Zweck angemessen ist.[^12] Und die Grenze zum professionellen Software Engineering hat ein Kriterium, denn sie ist überschritten, sobald ein Artefakt Pflichten aus Dauerhaftigkeit, Wartung, Sicherheit, Barrierefreiheit, institutionellem Betrieb, geteilter Nutzung, persistentem Zustand, Integration oder Unterstützung Dritter übernimmt.[^13]

Auch die Wissensorganisation hat eine prüfbare Form, und es ist das Abschlusskriterium der Distillation. Eine neue mitarbeitende Person oder eine neue Agent-Instanz sollte mit den Dokumenten und Zugriff auf die Ressourcen die Logik des Projekts rekonstruieren und die Arbeit ohne undokumentierte Erklärung fortsetzen können.[^14] Weil dieses Kriterium eine Aufgabe ist und kein Urteil, lässt es sich in derselben Operation lehren und prüfen, was es zur nützlichsten Einzelübung eines Kurses über die Methode macht.[^15] Wie viel dokumentarische Arbeit ein Projekt braucht, folgt daraus, was delegiert wird, sodass die Übung mit dem Fall skaliert, statt einen festen Maßstab aufzuerlegen.[^16]

## Gaps
- Das Lehrmaterial des Skriptums und des Foliensatzes speist dieses Kapitel und gehört zur parallelen Schreiblane, sodass das Kapitel allein auf der knappen Darstellung der Lehrfälle im Paper ruht.
- Die Gliederung fragt, welche Konzepte sich zuverlässig lehren lassen, wo Teilnehmende technische Unterstützung brauchen, wie Vorlagen die Qualität von Spezifikationen beeinflussen, ob Nicht-Programmierende erzeugte Implementierungen prüfen können und welche Prüfformen schwierig bleiben. Die Quellen beantworten keine davon, und das Kapitel führt sie als offene Fragen der Lehrlinie, statt sie zu beantworten.
- Wie Grounded Vaults die Kontinuität über Sitzungen tragen, ist in der Gliederung genannt und wird in Teil II von der anderen Lane behandelt, weshalb dieses Kapitel stattdessen auf das Abschlusskriterium der Distillation verweist.
- Kein Lehrfall wird hier einzeln beschrieben, weil die Quellen die Lehrsituation nur als unzureichende Evidenz für unabhängigen Transfer berichten.

[^1]: Grounded in [[30_assertions/teaching-cases-do-not-establish-independent-continuation]].
[^2]: Grounded in [[30_assertions/independent-transfer-is-evaluated-through-sustained-work]].
[^3]: Grounded in [[30_assertions/a-knowledge-base-is-tested-by-bounded-continuation-tasks]].
[^4]: Grounded in [[30_assertions/transferability-differs-from-exact-reproduction]].
[^5]: Grounded in [[30_assertions/transfer-would-require-adaptation]].
[^6]: Grounded in [[30_assertions/the-benefit-of-the-method-is-distributed-unevenly]].
[^7]: Grounded in [[30_assertions/the-method-redistributes-implementation-labour]].
[^8]: Grounded in [[30_assertions/the-method-cannot-supply-missing-competence]].
[^9]: Posit: die Fähigkeit, Unzulänglichkeit zu bemerken, als die entscheidende zu benennen, folgt aus der Verbindung der Arbeitsumverteilung mit der Grenze dessen, was Dokumente ausgleichen können, denn beide lassen die Last des Bemerkens bei der lesenden Person. Open evidence question: eine Studie, die das Erkennen unzureichender generierter Outputs gegen die technische und fachliche Kompetenz der lesenden Person misst.
[^10]: Posit: die sieben Bestandteile eines Curriculums für die Methode sind die eigene Anordnung des Buches dessen, was die vorangegangenen Kapitel von einer praktizierenden Person verlangen, und die Quellen nennen kein Curriculum. Open evidence question: welche der sieben sich auf ein messbares Niveau lehren lassen, was die Lehrfälle nicht zu zeigen angelegt waren.
[^11]: Grounded in [[30_assertions/a-wrong-output-is-diagnosed-by-document-type]].
[^12]: Grounded in [[30_assertions/technical-verification-and-scholarly-validation-differ-in-kind]].
[^13]: Grounded in [[30_assertions/the-boundary-to-research-software-engineering]].
[^14]: Grounded in [[30_assertions/the-sufficiency-of-distillation-is-practical]].
[^15]: Posit: das Fortsetzungskriterium taugt zugleich als Lehrübung, weil es durch einen beobachtbaren Versuch bestanden oder verfehlt wird und nicht durch den Eindruck einer prüfenden Person. Open evidence question: ob Kurse, die es stellen, besser gepflegte Dokumente hervorgebracht haben als Kurse, die die Dokumenttypen beschreibend lehren.
[^16]: Grounded in [[30_assertions/the-account-must-be-proportionate-to-what-is-delegated]].
