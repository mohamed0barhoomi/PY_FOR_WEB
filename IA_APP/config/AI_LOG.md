* Outil IA utilisé : Claude

* Prompt utilisé :
  Give me the complete project folder.

* Sortie obtenue (résumé) :
  Génération d’une structure complète du projet avec les différents fichiers et éléments nécessaires à son fonctionnement.

* Écarts identifiés par rapport au cahier des charges :

  - Ajout d’une fonctionnalité de sauvegarde automatique, alors que le cahier des charges ne demande pas de demander à l’utilisateur d’enregistrer manuellement.
  - Ajout de l’option --str--, alors que le programme ne doit pas demander à l’utilisateur de saisir une chaîne de caractères (str).
  - Création d’un user_id personnalisé, alors que le cahier des charges demande d’utiliser un identifiant avec AbstractUser.
  - Ajout d’attributs qui ne sont pas prévus dans le cahier des charges, notamment password et d’autres champs supplémentaires.

* Correction apportée et justification :

  - Suppression de la fonctionnalité de sauvegarde automatique afin de respecter précisément les fonctionnalités demandées dans le cahier des charges.
  - Suppression de l’option --str-- afin d’éviter une saisie supplémentaire qui n’est pas demandée.
  - Modification de la gestion de l’identifiant utilisateur afin d’utiliser AbstractUser conformément aux exigences du cahier des charges.
  - Suppression des attributs supplémentaires non prévus dans le cahier des charges afin de conserver uniquement les champs nécessaires au projet.
  - Vérification et adaptation de la structure du projet afin qu’elle corresponde aux exigences fonctionnelles et techniques du cahier des charges.
