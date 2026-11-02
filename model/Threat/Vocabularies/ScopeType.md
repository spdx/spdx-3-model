SPDX-License-Identifier: Community-Spec-1.0

# ScopeType

## Summary

The ScopeType enables to limit the scope of a ConceptRelationship.

## Description

A referenced concept may be a parent concept for various child concepts. This is in especially the case, when the
reference target is a taxonomy.

## Metadata

- name: ScopeType

## Entries

- node-only: only the object shall be referenced; it's children are not implied
- subtree: the object and its subtree are implied
- descendants-only: the object itself is not implied; yet all children are implied
