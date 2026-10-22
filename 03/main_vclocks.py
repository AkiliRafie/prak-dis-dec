from vector_clock import VectorClock

def main():
    print("--- Memulai Simulasi Vector Clock ---")
    
    # Inisialisasi 3 proses (P0, P1, P2)
    vc0 = VectorClock(num_processes=3, process_id=0)
    vc1 = VectorClock(num_processes=3, process_id=1)
    vc2 = VectorClock(num_processes=3, process_id=2)

    print("Kondisi Awal:")
    print(vc0)
    print(vc1)
    print(vc2)
    print("-" * 30)

    # 1. Proses 0 melakukan local event
    vc0.increment()
    print("Setelah P0 Local Event:")
    print(vc0)

    # 2. Proses 0 mengirim pesan ke Proses 1
    msg_p0_to_p1 = vc0.send_message()
    vc1.receive_message(msg_p0_to_p1)
    print("\nSetelah P0 Kirim Pesan ke P1:")
    print(vc0)
    print(vc1)

    # 3. Proses 2 melakukan local event
    vc2.increment()
    print("\nSetelah P2 Local Event:")
    print(vc2)

    # 4. Proses 1 mengirim pesan ke Proses 2
    msg_p1_to_p2 = vc1.send_message()
    vc2.receive_message(msg_p1_to_p2)
    print("\nSetelah P1 Kirim Pesan ke P2:")
    print(vc1)
    print(vc2)

    print("-" * 30)
    print("Analisis Hubungan Kejadian (Causality):")
    print(f"Apakah VC0 happens before VC1? {vc0.happens_before(vc1)}")
    print(f"Apakah VC0 concurrent dengan VC2? {vc0.is_concurrent(vc2)}")

if __name__ == "__main__":
    main()