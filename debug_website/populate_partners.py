#!/usr/bin/env python
"""
Script to populate DEBUG IT SERVICE with partner data
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'debug_it.settings')
django.setup()

from home.models import Partner

PARTNERS_DATA = [
    {
        "name": "Claude (Anthropic)",
        "partner_type": "ai",
        "description": "Advanced AI assistant powered by Anthropic's Claude. We use Claude's capabilities for intelligent automation, natural language processing, and AI-powered features in our applications.",
        "website": "https://www.anthropic.com",
        "featured": True,
        "order": 1
    },
    {
        "name": "GitHub Copilot",
        "partner_type": "ai",
        "description": "AI-powered code completion and programming assistant. Integrated into our development workflow to accelerate coding, improve code quality, and enhance developer productivity.",
        "website": "https://github.com/features/copilot",
        "featured": True,
        "order": 2
    },
    {
        "name": "Espire Infolabs",
        "partner_type": "it",
        "description": "Leading IT solutions and consulting partner. Collaboration for enterprise-level software development, cloud solutions, and digital transformation initiatives.",
        "website": "https://espire.in",
        "featured": True,
        "order": 3
    },
    {
        "name": "Windserv",
        "partner_type": "cloud",
        "description": "Cloud infrastructure and platform services partner. Supporting our platform with reliable cloud hosting, scalability, and infrastructure management solutions.",
        "website": "https://windserv.com",
        "featured": True,
        "order": 4
    },
    {
        "name": "NEC Technologies",
        "partner_type": "infrastructure",
        "description": "Enterprise IT infrastructure and technology solutions. Partnership for enterprise-grade security, infrastructure support, and technology integration services.",
        "website": "https://www.nec.com",
        "featured": True,
        "order": 5
    },
]

def populate_partners():
    """Populate partners"""
    print("=" * 60)
    print("Adding IT and AI Partners")
    print("=" * 60 + "\n")
    
    for data in PARTNERS_DATA:
        partner, created = Partner.objects.get_or_create(
            name=data['name'],
            defaults={
                'partner_type': data['partner_type'],
                'description': data['description'],
                'website': data['website'],
                'featured': data['featured'],
                'order': data['order'],
            }
        )
        if created:
            print(f"✓ Added partner: {data['name']} ({data['partner_type']})")
        else:
            print(f"- Partner '{data['name']}' already exists")
    
    print("\n" + "=" * 60)
    print("✓ Partner population completed!")
    print("=" * 60)
    
    # Print summary
    print(f"\nTotal Partners: {Partner.objects.count()}")
    print("\nPartners by type:")
    for ptype_code, ptype_name in Partner.PARTNER_TYPES:
        count = Partner.objects.filter(partner_type=ptype_code).count()
        if count > 0:
            print(f"  {ptype_name}: {count}")

if __name__ == '__main__':
    populate_partners()
