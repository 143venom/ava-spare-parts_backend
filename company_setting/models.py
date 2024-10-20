from django.db import models


# Logo Settings
class SiteLogo(models.Model):
    logo = models.ImageField(
        upload_to="company/logo/",
        default="default/favicon.ico",
        blank=True,
        null=True,
        verbose_name="Company Logo",
        help_text="Upload the logo of the company",
    )
    favicon = models.ImageField(
        upload_to="company/logo/",
        default="default/favicon.ico",
        blank=True,
        null=True,
        verbose_name="Favicon",
        help_text="Upload the favicon for the website",
    )

    def __str__(self):
        return "Site Logo Settings"

    class Meta:
        verbose_name_plural = "Site Logo"


# Contact Settings
class CompanyInfo(models.Model):
    company_name = models.CharField(
        max_length=255,
        verbose_name="Company Name",
        help_text="The full name of the company",
    )
    email = models.EmailField(
        verbose_name="Email Address", help_text="The main contact email for the company"
    )
    phone = models.CharField(
        max_length=15,
        verbose_name="Phone Number",
        help_text="The main contact phone number for the company",
    )
    address = models.CharField(
        max_length=700,
        verbose_name="Street Address",
        help_text="The street address of the company",
        default="Your Address",
        blank=True,
        null=True,
    )
    city = models.CharField(
        max_length=200,
        verbose_name="City",
        help_text="The city where the company is located",
        default="Your City",
        blank=True,
        null=True,
    )
    state = models.CharField(
        max_length=200,
        verbose_name="State/Province",
        help_text="The state or province where the company is located",
        default="Your State",
        blank=True,
        null=True,
    )
    postal = models.IntegerField(
        verbose_name="Postal Code",
        help_text="The postal code for the company's location",
        default=12345,
        blank=True,
        null=True,
    )
    country = models.CharField(
        max_length=300,
        verbose_name="Country",
        help_text="The country where the company is located",
        default="Your Country",
        blank=True,
        null=True,
    )
    day = models.CharField(
        max_length=9,
        default='Monday - Friday',
        verbose_name="Day of the Week",
        help_text="Day of the week for the opening hours"
    )
    opening_hours = models.CharField(
        max_length=100,
        default="10 am - 8 pm",
        verbose_name="Opening Hours",
        help_text="Company's regular opening hours",
    )

    def __str__(self):
        return f"{self.company_name} - {self.phone}"

    class Meta:
        verbose_name_plural = "Company Information"


# Social Media Setting
class SocialMedia(models.Model):
    facebook = models.URLField(
        max_length=255,
        verbose_name="Facebook URL",
        blank=True,
        null=True,
        help_text="URL to the company's Facebook page",
    )
    twitter = models.URLField(
        max_length=255,
        verbose_name="Twitter URL",
        blank=True,
        null=True,
        help_text="URL to the company's Twitter profile",
    )
    linkedin = models.URLField(
        max_length=255,
        verbose_name="LinkedIn URL",
        blank=True,
        null=True,
        help_text="URL to the company's LinkedIn profile",
    )
    instagram = models.URLField(
        max_length=255,
        verbose_name="Instagram URL",
        blank=True,
        null=True,
        help_text="URL to the company's Instagram profile",
    )
    youtube = models.URLField(
        max_length=255,
        verbose_name="YouTube Channel URL",
        blank=True,
        null=True,
        help_text="URL to the company's YouTube channel",
    )

    def __str__(self):
        return "Social Media Links"

    class Meta:
        verbose_name_plural = "Social Media"


# Footer Setting
class Footer(models.Model):
    copyright = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name="Copyright Text",
        help_text="The copyright notice to display in the footer",
    )

    def __str__(self):
        return "Footer Settings"

    class Meta:
        verbose_name_plural = "Footer"
