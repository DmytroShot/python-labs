from abc import ABC, abstractmethod
from typing import Dict, Type

class Document(ABC):
    """Інтерфейс Продукту: Базовий документ."""
    def __init__(self, doc_type: str):
        self._doc_type = doc_type

    @abstractmethod
    def render(self) -> str:
        """Повертає відрендерений рядок документу."""
        pass

class DocumentFactory(ABC):
    """Інтерфейс Фабрики: Створення документів."""
    @abstractmethod
    def create(self, doc_type: str) -> Document:
        """Створює екземпляр документу за типом."""
        pass

ALLOWED_TYPES = {"Report", "Invoice", "Contract"}

class CorpReport(Document):
    def render(self) -> str:
        return f"[{self._doc_type}] **Corp Document:** Standard, fully compliant report."

class CorpInvoice(Document):
    def render(self) -> str:
        return f"[{self._doc_type}] **Corp Document:** Standard, legal invoice format."

class CorpContract(Document):
    def render(self) -> str:
        return f"[{self._doc_type}] **Corp Document:** Official, detailed contract."

class ShadowReport(Document):
    def render(self) -> str:
        return f"[{self._doc_type}] **Shadow Document:** Test format. Service tag: <#4X-RPT-A>"

class ShadowInvoice(Document):
    def render(self) -> str:
        return f"[{self._doc_type}] **Shadow Document:** Simplified internal version. Internal ID: [9999]"

class ShadowContract(Document):
    def render(self) -> str:
        return f"[{self._doc_type}] **Shadow Document:** Draft/Test version. Status: DRAFT_ONLY"

class CorpDocumentFactory(DocumentFactory):
    """Фабрика для створення Corp документів."""
    _mapping: Dict[str, Type[Document]] = {
        "Report": CorpReport,
        "Invoice": CorpInvoice,
        "Contract": CorpContract
    }

    def create(self, doc_type: str) -> Document:
        if doc_type not in ALLOWED_TYPES:
            raise ValueError(f"SECURITY ERROR: Document type '{doc_type}' is not allowed in the whitelist.")
        
        doc_class = self._mapping.get(doc_type)
        if not doc_class:
            raise ValueError(f"Unknown document type '{doc_type}' for 'corp' mode.")
            
        return doc_class(doc_type)


class ShadowDocumentFactory(DocumentFactory):
    """Фабрика для створення Shadow документів."""
    _mapping: Dict[str, Type[Document]] = {
        "Report": ShadowReport,
        "Invoice": ShadowInvoice,
        "Contract": ShadowContract
    }

    def create(self, doc_type: str) -> Document:
        if doc_type not in ALLOWED_TYPES:
            raise ValueError(f"SECURITY ERROR: Document type '{doc_type}' is not allowed in the whitelist.")
            
        doc_class = self._mapping.get(doc_type)
        if not doc_class:
            raise ValueError(f"Unknown document type '{doc_type}' for 'shadow' mode.")
            
        return doc_class(doc_type)


def get_factory(mode: str) -> DocumentFactory:
    """Конфіг-перемикач: вибирає фабрику за режимом."""
    if mode == 'corp':
        return CorpDocumentFactory()
    elif mode == 'shadow':
        return ShadowDocumentFactory()
    else:
        raise ValueError(f"Invalid mode: '{mode}'. Must be 'corp' or 'shadow'.")

def client_code(factory: DocumentFactory, doc_type: str):
    """Клієнтський код: використовує фабрику без знання конкретних класів."""
    try:
        document = factory.create(doc_type)
        print(f"   ✅ Document created ({type(document).__name__}): {document.render()}")
    except ValueError as e:
        print(f"   ❌ {e}")
        
print("--- Abstract Factory Demonstration ---")
print("Дозволені типи: Report, Invoice, Contract")

document_requests = ["Report", "Invoice", "Contract", "SecretFile"]

print("\n## 1. Режим: 'corp' (Чесний)")
corp_factory = get_factory('corp')

for doc_type in document_requests:
    print(f"\n* Запит на документ: **{doc_type}**")
    client_code(corp_factory, doc_type)

print("\n" + "="*50 + "\n")
print("## 2. Режим: 'shadow' (Тіньовий)")
shadow_factory = get_factory('shadow') 

for doc_type in document_requests:
    print(f"\n* Запит на документ: **{doc_type}**")
    client_code(shadow_factory, doc_type)