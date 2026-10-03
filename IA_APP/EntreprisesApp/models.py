import uuid

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class TimeStampedModel(models.Model):
    """Classe abstraite : created_at et updated_at pour tous les modèles."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UtilisateurManager(BaseUserManager):
    use_in_migrations = True

    def _generate_user_id(self):
        """Génère un identifiant unique de 8 caractères : 'U' + 7 hex."""
        while True:
            candidate = "U" + uuid.uuid4().hex[:7].upper()
            if not self.model.objects.filter(pk=candidate).exists():
                return candidate

    def create_user(self, email, password=None, role=None, **extra_fields):
        if not email:
            raise ValueError("L'adresse email est obligatoire.")
        if role is None:
            raise ValueError(
                "Le rôle doit être fourni selon le contexte d'inscription."
            )
        email = self.normalize_email(email)
        user = self.model(
            user_id=self._generate_user_id(),
            email=email,
            role=role,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields["role"] = Utilisateur.Role.ADMIN
        return self.create_user(email, password, **extra_fields)


class Utilisateur(AbstractUser, TimeStampedModel):
    class Role(models.TextChoices):
        CHARGEUR = "chargeur", "Chargeur"
        TRANSPORTEUR = "transporteur", "Transporteur"
        ADMIN = "admin", "Administrateur"

    user_id = models.CharField(max_length=8, primary_key=True, editable=False)
    username = None  # l'email sert d'identifiant de connexion
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20, blank=True)
    role = models.CharField(max_length=20, choices=Role.choices)
    # first_name = prénom, last_name = nom (hérités d'AbstractUser)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UtilisateurManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"


class Entreprise(TimeStampedModel):
    class TypeEntreprise(models.TextChoices):
        CHARGEUR = "chargeur", "Chargeur"
        TRANSPORTEUR = "transporteur", "Transporteur"

    raison_sociale = models.CharField(max_length=150)
    matricule_fiscal = models.CharField(max_length=17, unique=True)
    type_entreprise = models.CharField(
        max_length=20, choices=TypeEntreprise.choices
    )
    adresse = models.TextField()
    utilisateur = models.OneToOneField(
        Utilisateur,
        on_delete=models.CASCADE,
        related_name="entreprise",
    )

    def __str__(self):
        return f"{self.raison_sociale} ({self.get_type_entreprise_display()})"
