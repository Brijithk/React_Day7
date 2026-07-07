from person import Person
from database import Database

class Doctor(Person):

    def __init__(self, doctor_id, name):
        super().__init__(doctor_id, name)

    def doctor_dashboard(self):

        while True:

            print("\n========== DOCTOR PANEL ==========")
            # print("1. View Profile")
            print("1. View Appointments")
            print("2. Start Consultation")
            print("3. Logout")

            choice = input("\nEnter choice : ")

            # if choice == "1":
            #     self.display()

            if choice == "1":
                self.view_appointments()

            elif choice == "2":
                self.start_consultation()

            elif choice == "3":
                break

            else:
                print("Invalid choice")
    
    def view_appointments(self):

            con = Database.get_connection()
            cur = con.cursor()

            try:

                query = """
                SELECT a.appointment_id,
                    a.patient_id,
                    p.patient_name,
                    a.appointment_date,
                    a.appointment_time,
                    a.token_no,
                    a.appointment_status
                FROM appointment a
                JOIN patient p
                ON a.patient_id = p.patient_id
                WHERE a.doctor_id=%s
                ORDER BY a.appointment_date,
                        a.token_no
                """

                cur.execute(query, (self.user_id,))

                appointments = cur.fetchall()

                if not appointments:
                    print("\nNo appointments found.")
                    return

                print("\n=========== APPOINTMENTS ===========")

                print(
                    f"{'APPT ID':<10}"
                    f"{'PATIENT':<10}"
                    f"{'NAME':<20}"
                    f"{'DATE':<12}"
                    # f"{'TIME':<10}"
                    f"{'TOKEN':<8}"
                    f"{'STATUS'}"
                )

                print("-"*70)

                for a in appointments:

                    print(
                        f"{a[0]:<10}"
                        f"{a[1]:<10}"
                        f"{a[2]:<20}"
                        f"{str(a[3]):<12}"
                        # f"{str(a[4]):<10}"
                        f"{a[5]:<8}"
                        f"{a[6]}"
                    )

            except Exception as e:
                print("Error :", e)

            finally:
                cur.close()
                con.close()

    def start_consultation(self):

            # Show appointments first
            print("\n========== YOUR APPOINTMENTS ==========")
            self.view_appointments()

            con = Database.get_connection()
            cur = con.cursor()

            try:

                appointment_id = input(
                    "\nEnter Appointment ID to consult : "
                )

                cur.execute("""
                    SELECT patient_id,
                    appointment_status
                    FROM appointment
                    WHERE appointment_id=%s
                    AND doctor_id=%s
                """,
                (appointment_id, self.user_id))


                result = cur.fetchone()

                if not result:
                    print("Appointment not found")
                    return

                patient_id = result[0]
                status = result[1]

                if status == "Completed":
                    print("\nThis consultation is already completed.")
                    return

                if status == "Cancelled":
                    print("\nThis appointment was cancelled.")
                    return

                # Show patient details
                cur.execute("""
                    SELECT patient_name,
                        age,
                        gender,
                        blood_group,
                        phone
                    FROM patient
                    WHERE patient_id=%s
                """, (patient_id,))

                patient = cur.fetchone()

                print("\n========== PATIENT DETAILS ==========")
                print("Patient ID   :", patient_id)
                print("Name         :", patient[0])
                print("Age          :", patient[1])
                print("Gender       :", patient[2])
                print("Blood Group  :", patient[3])
                print("Phone        :", patient[4])

                print("\n========== CONSULTATION ==========")

                symptoms = input("Symptoms      : ")
                diagnosis = input("Diagnosis     : ")
                prescription = input("Prescription  : ")
                notes = input("Notes         : ")

                # Generate consultation id
                cur.execute("""
                    SELECT consultation_id
                    FROM consultation
                    ORDER BY id DESC
                    LIMIT 1
                """)

                row = cur.fetchone()

                if row:
                    number = int(row[0][1:]) + 1
                else:
                    number = 1

                consultation_id = f"C{number:03d}"

                cur.execute("""
                    INSERT INTO consultation
                    (
                        consultation_id,
                        appointment_id,
                        patient_id,
                        doctor_id,
                        symptoms,
                        diagnosis,
                        prescription,
                        notes
                    )
                    VALUES
                    (%s,%s,%s,%s,%s,%s,%s,%s)
                """,
                (
                    consultation_id,
                    appointment_id,
                    patient_id,
                    self.user_id,
                    symptoms,
                    diagnosis,
                    prescription,
                    notes
                ))

                # Update appointment status
                #
                cur.execute("""
                    UPDATE appointment
                    SET appointment_status='Completed'
                    WHERE appointment_id=%s
                """, (appointment_id,))

                con.commit()

                print("\nConsultation Completed Successfully")
                print("Consultation ID :", consultation_id)

            except Exception as e:
                con.rollback()
                print("Error :", e)

            finally:
                cur.close()
                con.close()