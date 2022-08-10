import gym

resultado = [2, 1, 1, 2, 2, 2, 2, 0, 1, 1, 1, 2, 1, 0, 2, 0, 2, 2, 2, 2, 2, 1, 2, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 0, 1, 2, 2, 0, 1, 1, 0, 1, 0, 1, 0, 2, 0, 0, 2, 0, 2, 2, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 1, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 0, 2, 1, 2, 1, 1, 2, 1, 2, 1, 0, 2, 1, 1, 0, 0, 0, 2, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 2, 0, 0, 1, 0, 1, 0, 2, 1, 2, 0, 0, 2, 1, 2, 2, 2, 1, 2, 
2, 2, 2, 1, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 1, 1, 2, 1]

envName = 'MountainCar-v0'
renderMode = 'human'

env = gym.make(envName, new_step_api=True, render_mode='human')
env.reset()
for i in range ((len(resultado))):
    state, reward, done,info, data = env.step(resultado[i])
    print(state, reward, done, info, data)