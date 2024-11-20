def personal_trainer():
    print("Bem-vindo ao Assistente de Personal Trainer Virtual!")
    
    # Coleta de dados do usuário
    biotipo = input("Qual é seu biotipo corporal (Ectomorfo, Mesomorfo, Endomorfo)? ").capitalize()
    dias_semana = int(input("Quantos dias por semana você pode treinar? (Digite um número) "))
    minutos_dia = int(input("Quantos minutos por dia você pode treinar? "))
    preferencia = input("Qual tipo de exercício você prefere (Cardio, Musculação, Yoga, HIIT)? ").capitalize()
    objetivo = input("Qual é o seu objetivo (Perda de peso, Ganho de massa muscular, Resistência, Flexibilidade)? ").capitalize()
    experiencia = input("Qual é seu nível de experiência (Iniciante, Intermediário, Avançado)? ").capitalize()
    
    # Processamento e recomendação
    print("\nAnalisando seu perfil e criando seu plano de treino...\n")
    
    if preferencia == "HIIT" and objetivo == "Perda de peso":
        print("Plano de Treino Personalizado:")
        for i in range(dias_semana):
            print(f"\nDia {i+1}:")
            print(f"- Aquecimento (5 minutos): Polichinelos e alongamento dinâmico.")
            print(f"- HIIT (20 minutos):")
            print("  30 segundos de burpees + 30 segundos de descanso.")
            print("  30 segundos de mountain climbers + 30 segundos de descanso.")
            print("  30 segundos de agachamentos com salto + 30 segundos de descanso.")
            print("  Repita 3 vezes.")
            print("- Resfriamento (5 minutos): Alongamento estático.")
    else:
        print("Ainda estamos desenvolvendo planos detalhados para outras preferências!")

# Executar o protótipo
personal_trainer()
