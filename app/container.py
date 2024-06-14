from dependency_injector import containers, providers

from app import user
from app.user.adapter.output.persistence.sqlalchemy.user import UserSQLAlchemyRepo
from app.user.adapter.output.repository_adapter import UserRepositoryAdapter
from app.user.application.service.user import UserService
from app.user.domain import repository


class Container(containers.DeclarativeContainer):
    user_repo = providers.Singleton(UserSQLAlchemyRepo)
    user_repo_adapter = providers.Factory(UserRepositoryAdapter, user_repo=user_repo)
    user_service = providers.Factory(UserService, repository=user_repo_adapter)
