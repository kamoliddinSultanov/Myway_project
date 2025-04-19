import { config } from '@vue/test-utils'

// Mock переходов по маршрутам
config.global.mocks = {
  $route: { path: '/login' },
  $router: { push: jest.fn() }
}