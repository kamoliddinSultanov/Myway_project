import { config } from '@vue/test-utils'

config.global.mocks = {
  $route: { path: '/login' },
  $router: { push: jest.fn() }
}