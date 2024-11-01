from tanks.models import NameService

def find_service_by_name(service_name, related_field):
    """
    جستجوی سرویس مرتبط با مدل‌های مختلف بر اساس نام، ename یا pname
    """
    return (
        NameService.objects.filter(name=service_name, **{f"{related_field}__isnull": False}).first() or
        NameService.objects.filter(ename=service_name, **{f"{related_field}__isnull": False}).first() or
        NameService.objects.filter(pname=service_name, **{f"{related_field}__isnull": False}).first()
    )
