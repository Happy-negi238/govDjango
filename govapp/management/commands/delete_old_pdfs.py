from django.core.management.base import BaseCommand
from django.utils import timezone
from govapp.models import Pdf_Detail  # apne model ka naam use karo
import os

class Command(BaseCommand):
    help = 'Delete PDFs older than X seconds (for testing)'

    def handle(self, *args, **kwargs):
        cutoff_date = timezone.now() - timezone.timedelta(seconds=60)
        old_pdfs = Pdf_Detail.objects.filter(created_at__lt=cutoff_date, pdf__isnull=False).exclude(pdf='')

        for pdf in old_pdfs:
            pdf_path = pdf.pdf.path if hasattr(pdf.pdf, 'path') else None
            if pdf_path and os.path.exists(pdf_path):
                os.remove(pdf_path)  # file delete hogi
            pdf.pdf = ''  # DB me PDF field empty kar denge
            pdf.save()         
        self.stdout.write(self.style.SUCCESS("Old PDFs deleted successfully"))