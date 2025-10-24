# Git Workflow Documentation

## Branching Strategy

### Main Branches
- `main`: Production-ready code
- `dev`: Integration branch for features

### Supporting Branches
- `feature/*`: New features
- `hotfix/*`: Urgent production fixes
- `release/*`: Release preparation

## Workflow Steps

1. Create feature branch from `dev`
2. Develop and commit changes
3. Push feature branch
4. Create Pull Request to `dev`
5. Code review and testing
6. Merge to `dev`
7. Periodic merge from `dev` to `main`
8. Tag releases on `main`

## Commit Message Convention
- feat: New feature
- fix: Bug fix
- docs: Documentation
- style: Formatting
- refactor: Code restructuring
- test: Testing related
- chore: Maintenance tasks