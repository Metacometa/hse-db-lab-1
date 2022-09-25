import io
import os
import random
from colorama import init, Fore

class Dmbs():
    def __init__(self, dir_name):
        os.makedirs(dir_name + "/backups")

    def fill_students(self, dir_name, names):
        print(Fore.LIGHTCYAN_EX + "@DATABASE '" + Fore.CYAN + dir_name + Fore.LIGHTCYAN_EX + "' students " + Fore.LIGHTBLUE_EX + "FILLED " + Fore.LIGHTCYAN_EX +"from '" + Fore.CYAN + names + Fore.LIGHTCYAN_EX + "':" + Fore.RESET)
        file_names = io.open(names, "r", encoding='utf-8')
        students_file = io.open(dir_name + "/students.txt", "w",encoding='utf-8')
        names = file_names.readlines()
        id = 0
        for i in names:
            student = i.split()
            students_file.write(str(id)+" "+student[1] + " " + student[0] + " " + student[2] +"\n")
            id+=1
        file_names.close()
        students_file.close()
    def fill_variants(self, dir_name, test_names):
        print(Fore.LIGHTCYAN_EX + "@DATABASE '" + Fore.CYAN + dir_name + Fore.LIGHTCYAN_EX + "' tests " + Fore.LIGHTBLUE_EX + "FILLED " + Fore.LIGHTCYAN_EX +"from '" + Fore.CYAN + test_names + Fore.LIGHTCYAN_EX + "':" + Fore.RESET)
        file_test_names = io.open(test_names, "r", encoding='utf-8')
        variants_file = io.open(dir_name + "/variants.txt", "w",encoding='utf-8')
        variants_names = file_test_names.readlines()
        for i in range(0,len(variants_names)):
            variants_file.write(str(i)+" "+variants_names[i].strip() + "\n")
        file_test_names.close()
        variants_file.close()
    def print_students_table(self, dir_name):
        print(Fore.LIGHTCYAN_EX + "@DATABASE '" + Fore.CYAN + dir_name + Fore.LIGHTCYAN_EX + "' file '" + Fore.CYAN + "students.txt" + Fore.LIGHTCYAN_EX + "':" + Fore.RESET)
        students_file = io.open(dir_name + "/students.txt", "r", encoding='utf-8')
        students = students_file.readlines()
        first_shift = 0
        second_shift = 0
        third_shift = 0
        for i in students:
            string = i.split()
            first_shift = max(first_shift, len(string[0]))
            second_shift = max(second_shift, len(string[1]))
            third_shift = max(third_shift, len(string[2]))
        for i in students:
            string = i.split()
            print(string[0] + (first_shift-len(string[0])+13)*" " + string[1] + (second_shift-len(string[1])+3)*" " + string[2] + (third_shift-len(string[2])+3)*" " + string[3])
        students_file.close()
    def print_tests(self, dir_name):
        print(Fore.LIGHTCYAN_EX + "@DATABASE '" + Fore.CYAN + dir_name + Fore.LIGHTCYAN_EX + "' file '" + Fore.CYAN + "variants.txt" + Fore.LIGHTCYAN_EX + "':" + Fore.RESET)
        tests_file = io.open(dir_name + "/variants.txt", "r", encoding='utf-8')
        variants = tests_file.readlines()
        for i in variants:
            string = i.split()
            print(string[0] + 10*" "+string[1])
        tests_file.close()
    def find_student_by_id(self, dir_name, id):
        students_file = io.open(dir_name + "/students.txt", "r", encoding='utf-8')
        students = students_file.readlines()
        for i in students:
            student_id = i.split()
            if str(id) == student_id[0]:
                print(Fore.LIGHTCYAN_EX + "@DATABASE '" + Fore.CYAN + dir_name + Fore.LIGHTCYAN_EX + "' " + Fore.LIGHTBLUE_EX + "FOUND " + Fore.LIGHTCYAN_EX + "student with id '" + Fore.LIGHTYELLOW_EX + str(id) + Fore.LIGHTCYAN_EX + "': '" + Fore.LIGHTYELLOW_EX + student_id[2] + " " + student_id[1] + " " + student_id[3] + Fore.LIGHTCYAN_EX + "'" + Fore.RESET)
                students_file.close()
                return 0
        print(Fore.LIGHTCYAN_EX + "@DATABASE '" + Fore.CYAN + dir_name + Fore.LIGHTCYAN_EX + "' student with id '" + Fore.LIGHTYELLOW_EX + str(id) + Fore.LIGHTCYAN_EX + "' is " + Fore.LIGHTBLUE_EX + "NOT FOUND" + Fore.RESET)
        students_file.close()
    def find_test_by_id(self, dir_name, id):
        tests_file = io.open(dir_name + "/variants.txt", "r", encoding='utf-8')
        variants = tests_file.readlines()
        for i in variants:
            variant_id = i.split()
            if str(id) == variant_id[0]:
                print(Fore.LIGHTCYAN_EX + "@DATABASE '" + Fore.CYAN + dir_name + Fore.LIGHTCYAN_EX + "' " + Fore.LIGHTBLUE_EX + "FOUND" + Fore.LIGHTCYAN_EX + " test with id '" + Fore.LIGHTYELLOW_EX + str(id) + Fore.LIGHTCYAN_EX + "': '" + Fore.LIGHTYELLOW_EX + variant_id[1] + Fore.LIGHTCYAN_EX + "'"+ Fore.RESET)
                tests_file.close()
                return 0
        print(Fore.LIGHTCYAN_EX + "@DATABASE '" + Fore.CYAN + dir_name + Fore.LIGHTCYAN_EX + "' test with id '" + Fore.LIGHTYELLOW_EX + str(id) + Fore.LIGHTCYAN_EX + "' IS " + Fore.LIGHTBLUE_EX + "NOT FOUND" + Fore.RESET)
        tests_file.close()
    def add_student(self, dir_name, name, surname, patronymic):
        students_file = io.open(dir_name + "/students.txt", "r", encoding='utf-8')
        students = students_file.readlines()
        new_student = str(len(students))+" "+name+" "+surname+" "+patronymic + "\n"
        for i in students:
            new_id = new_student.split()[0]
            old_id = i.split()[0]
            if i.strip() == new_student.strip() or (new_id == old_id):
                print(Fore.LIGHTCYAN_EX + "@DATABASE '" + Fore.CYAN + dir_name + Fore.LIGHTCYAN_EX + "student '" + Fore.LIGHTYELLOW_EX + new_student.strip() + Fore.LIGHTCYAN_EX + "' already " +Fore.LIGHTRED_EX + "EXISTS" + Fore.RESET)
                students_file.close()
                return 0
        students_file.close()
        students_file = io.open(dir_name + "/students.txt", "a", encoding='utf-8')
        students_file.write(new_student)
        print(Fore.LIGHTCYAN_EX + "@DATABASE '" + Fore.CYAN + dir_name + Fore.LIGHTCYAN_EX + "' student '" + Fore.LIGHTYELLOW_EX + name + " " + surname + " " + patronymic + Fore.LIGHTCYAN_EX + "' was " + Fore.LIGHTMAGENTA_EX + "ADDED" + Fore.RESET)
        students_file.close()
    def add_test(self, dir_name, test_name):
        tests_file = io.open(dir_name + "/variants.txt", "r", encoding='utf-8')
        variants = tests_file.readlines()
        new_test = str(len(variants)) + " " + test_name +'\n'
        for i in variants:
            old_id = i.split()[0]
            new_id = new_test.split()[0]
            old_name = i.split()[1]
            new_name = new_test.split()[1]
            if old_name.strip() == new_name.strip() or (new_id == old_id):
                print(Fore.LIGHTCYAN_EX + "@DATABASE '" + Fore.CYAN + dir_name + Fore.LIGHTCYAN_EX + "' test '" + Fore.LIGHTYELLOW_EX + new_test.strip().split()[1] + Fore.LIGHTCYAN_EX + "' already " + Fore.LIGHTRED_EX + "EXISTS" + Fore.RESET)
                tests_file.close()
                return 0
        tests_file.close()
        tests_file = io.open(dir_name + "/variants.txt", "a", encoding='utf-8')
        tests_file.write(new_test)
        print(Fore.LIGHTCYAN_EX + "@DATABASE '" + Fore.CYAN + dir_name + Fore.LIGHTCYAN_EX + "' test '" + Fore.LIGHTYELLOW_EX + test_name + Fore.LIGHTCYAN_EX + "' was " + Fore.LIGHTMAGENTA_EX + "ADDED" + Fore.RESET)
        tests_file.close()
    def delete_student(self, dir_name, student_name):
        students_file = io.open(dir_name + "/students.txt", "r", encoding='utf-8')
        students = students_file.readlines()
        students_file.close()

        students_file = io.open(dir_name + "/students.txt", "w", encoding='utf-8')
        deleted = 0
        for i in students:
            if i.strip() != student_name.strip():
                students_file.write(i)
            else:
                deleted = 1
        students_file.close()
        if deleted == 1:
            print(Fore.LIGHTCYAN_EX + "@DATABASE '" + Fore.CYAN + dir_name + Fore.LIGHTCYAN_EX + "' student '" + Fore.LIGHTYELLOW_EX + student_name + Fore.LIGHTCYAN_EX + "' was " + Fore.LIGHTRED_EX + "DELETED" + Fore.RESET)
        else:
            print(Fore.LIGHTCYAN_EX + "@DATABASE '" + Fore.CYAN + dir_name + Fore.LIGHTCYAN_EX + "' student '" + Fore.LIGHTYELLOW_EX + student_name + Fore.LIGHTCYAN_EX + "' was " + Fore.LIGHTRED_EX + "NOT FOUND " + Fore.LIGHTCYAN_EX + "and " + Fore.LIGHTRED_EX + "DELETED" + Fore.RESET)
    def delete_test(self, dir_name, test_name):
        tests_file = io.open(dir_name + "/variants.txt", "r", encoding='utf-8')
        variants = tests_file.readlines()
        tests_file.close()

        tests_file = io.open(dir_name + "/variants.txt", "w", encoding='utf-8')
        deleted = 0
        for i in variants:
            checked_name = i.split()[1]
            if checked_name.strip() != test_name:
                tests_file.write(i)
            else:
                deleted = 1
        tests_file.close()
        if deleted == 1:
            print(Fore.LIGHTCYAN_EX + "@DATABASE '" + Fore.CYAN + dir_name + Fore.LIGHTCYAN_EX + "' test '" + Fore.LIGHTYELLOW_EX + test_name + Fore.LIGHTCYAN_EX + "' was " + Fore.LIGHTRED_EX + "DELETED" + Fore.RESET)
        else:
            print(Fore.LIGHTCYAN_EX + "@DATABASE '" + Fore.CYAN + dir_name + Fore.LIGHTCYAN_EX + "' test '" + Fore.LIGHTYELLOW_EX + test_name + Fore.LIGHTCYAN_EX +"' was " + Fore.LIGHTRED_EX + "NOT FOUND " + Fore.LIGHTCYAN_EX + "and " + Fore.LIGHTRED_EX + "DELETED" + Fore.RESET)
    def form_testing_table(self, dir_name):
        print(Fore.LIGHTCYAN_EX + "@DATABASE '" + Fore.CYAN + dir_name + Fore.LIGHTCYAN_EX + "' file '" + Fore.CYAN + 'testing_table.txt' + Fore.LIGHTCYAN_EX + "' " + Fore.LIGHTBLUE_EX + "FORMED" + Fore.RESET)
        tests_file = io.open(dir_name + "/variants.txt", "r", encoding='utf-8')
        variants = tests_file.readlines()
        num_of_tests = len(variants)
        tests_file.close()

        testing_table_file = io.open(dir_name + "/testing_table.txt", "w", encoding='utf-8')

        students_file = io.open(dir_name + "/students.txt", "r", encoding='utf-8')
        students = students_file.readlines()
        students_file.close()

        for i in students:
            testing_table_file.write(i.split()[0] + " " + str(random.randint(0, num_of_tests-1)) + "\n")
        tests_file.close()
    def print_testing_table(self, dir_name):
        print(Fore.LIGHTCYAN_EX + "@DATABASE '" + Fore.CYAN + dir_name + Fore.LIGHTCYAN_EX + "' file '" + Fore.CYAN + "testing_table.txt" + Fore.LIGHTCYAN_EX + "':" + Fore.RESET)
        testing_table_file = io.open(dir_name + "/testing_table.txt", "r", encoding='utf-8')
        testing_table = testing_table_file.readlines()
        testing_table_file.close()

        for i in testing_table:
            student_id = i.split()[0]
            variant_id = i.split()[1]
            students_file = io.open(dir_name + "/students.txt", "r", encoding='utf-8')
            students = students_file.readlines()
            variants_file = io.open(dir_name + "/variants.txt", "r", encoding='utf-8')
            variants = variants_file.readlines()
            max_name_length = 0
            max_surname_length = 0
            max_patronymic_length = 0
            for j in students:
                student = j.split()
                max_name_length = max(max_name_length, len(student[1]))
                max_surname_length = max(max_surname_length, len(student[2]))
                max_patronymic_length = max(max_patronymic_length, len(student[3]))
            string = ""
            for j in students:
                student = j.split()
                if student[0] == student_id:
                    string += student[1] + (max_name_length-len(student[1])+3)*" " + student[2] + (max_surname_length-len(student[2])+3)*" " + student[3] + (max_patronymic_length-len(student[3])+3)*" "
            for j in variants:
                variant = j.split()
                if variant[0] == variant_id:
                    string+= variant[1]
                    print(string)
            students_file.close()
            variants_file.close()
    def edit_test(self, dir_name, test_name, new_test_name):
        tests_file = io.open(dir_name + "/variants.txt", "r", encoding='utf-8')
        variants = tests_file.readlines()
        tests_file.close()
        for i in variants:
            if i.strip().split()[1] == new_test_name.strip().split()[1]:
                print(Fore.LIGHTCYAN_EX + "@DATABASE '" + Fore.CYAN + dir_name + Fore.LIGHTCYAN_EX + "' test '" + Fore.LIGHTYELLOW_EX + test_name + Fore.LIGHTCYAN_EX + "' can't be " + Fore.LIGHTGREEN_EX + "EDITED " + Fore.LIGHTCYAN_EX + "with '" + Fore.LIGHTYELLOW_EX + new_test_name + Fore.LIGHTCYAN_EX + "': test '" + Fore.LIGHTYELLOW_EX + new_test_name.strip().split()[1] + Fore.LIGHTCYAN_EX + "' already " + Fore.LIGHTRED_EX + "EXISTS" + Fore.RESET)
                return 0
            if test_name.split()[0] != new_test_name.split()[0]:
                if i.strip().split()[0] == new_test_name.split()[0]:
                    print(Fore.LIGHTCYAN_EX + "@DATABASE '" + Fore.CYAN + dir_name + Fore.LIGHTCYAN_EX + "' test '" + Fore.LIGHTYELLOW_EX + test_name + Fore.LIGHTCYAN_EX + "' can't be " + Fore.LIGHTGREEN_EX + "EDITED " + Fore.LIGHTCYAN_EX + "with '" + Fore.LIGHTYELLOW_EX + new_test_name + Fore.LIGHTCYAN_EX + "': id '" + Fore.LIGHTYELLOW_EX + i.strip().split()[0] + Fore.LIGHTCYAN_EX + "' already " + Fore.LIGHTRED_EX + "EXISTS" + Fore.RESET)
                    return 0
        tests_file = io.open(dir_name + "/variants.txt", "w", encoding='utf-8')
        edited = 0
        for i in variants:
            if i.strip() == test_name:
                tests_file.write(new_test_name + '\n')
                edited = 1
            else:
                tests_file.write(i)
        tests_file.close()
        if edited == 1:
            print(Fore.LIGHTCYAN_EX + "@DATABASE '" + Fore.CYAN + dir_name + Fore.LIGHTCYAN_EX + "' test '" + Fore.LIGHTYELLOW_EX + test_name + Fore.LIGHTCYAN_EX + "' was " + Fore.LIGHTGREEN_EX + "EDITED" + Fore.LIGHTCYAN_EX + " with '"+ Fore.LIGHTYELLOW_EX + new_test_name + Fore.LIGHTCYAN_EX+"'"+ Fore.RESET)
        else:
            print(Fore.LIGHTCYAN_EX + "@DATABASE '" + Fore.CYAN + dir_name + Fore.LIGHTCYAN_EX + "' test '" + Fore.LIGHTYELLOW_EX + test_name + Fore.LIGHTCYAN_EX +"' was " + Fore.LIGHTGREEN_EX + "NOT FOUND" + Fore.LIGHTCYAN_EX + " and " + Fore.LIGHTGREEN_EX + "EDITED " + Fore.LIGHTCYAN_EX + "WITH '" + Fore.LIGHTYELLOW_EX + new_test_name + Fore.LIGHTCYAN_EX +"'" + Fore.RESET)
    def edit_student(self, dir_name, student_name, new_student_name):
        students_file = io.open(dir_name + "/students.txt", "r", encoding='utf-8')
        students = students_file.readlines()
        students_file.close()

        for i in students:
            if student_name.strip().split()[0] != new_student_name.strip().split()[0]:
                if i.strip().split()[0] == new_student_name.strip().split()[0]:
                    print(Fore.LIGHTCYAN_EX + "@DATABASE '" + Fore.CYAN + dir_name + Fore.LIGHTCYAN_EX + "' student '" + Fore.LIGHTYELLOW_EX + student_name + Fore.LIGHTCYAN_EX + "' can't be " + Fore.LIGHTGREEN_EX + "EDITED " + Fore.LIGHTCYAN_EX + "with: '" + Fore.LIGHTYELLOW_EX + new_student_name + Fore.LIGHTCYAN_EX + "': id '" + Fore.LIGHTYELLOW_EX + i.strip().split()[0] + Fore.LIGHTCYAN_EX +"' already " + Fore.LIGHTRED_EX + "EXISTS" + Fore.RESET)
                    return 0

        students_file = io.open(dir_name + "/students.txt", "w", encoding='utf-8')
        edited = 0
        for i in students:
            if i.strip() == student_name.strip():
                students_file.write(new_student_name + '\n')
                edited = 1
            else:
                students_file.write(i)

        students_file.close()
        if edited == 1:
            print(Fore.LIGHTCYAN_EX + "@DATABASE '" + Fore.CYAN + dir_name + Fore.LIGHTCYAN_EX + "' student '" + Fore.LIGHTYELLOW_EX + student_name + Fore.LIGHTCYAN_EX + "' was " + Fore.LIGHTGREEN_EX + "EDITED " + Fore.LIGHTCYAN_EX + "with '" + Fore.LIGHTYELLOW_EX + new_student_name + Fore.LIGHTCYAN_EX + "'" + Fore.RESET)
        else:
            print(Fore.LIGHTCYAN_EX + "@DATABASE '" + Fore.CYAN + dir_name + Fore.LIGHTCYAN_EX + "' student '" + Fore.LIGHTYELLOW_EX + student_name + Fore.LIGHTCYAN_EX +"' was " + Fore.LIGHTGREEN_EX + "NOT FOUND " + Fore.LIGHTCYAN_EX + "and " + Fore.LIGHTGREEN_EX + "EDITED " + Fore.LIGHTCYAN_EX + "with '" + Fore.LIGHTYELLOW_EX + new_student_name + Fore.LIGHTCYAN_EX + "'" + Fore.RESET)

    def create_backup(self, dir_name, backup_name):
        print(Fore.LIGHTCYAN_EX + "@DATABASE '" + Fore.CYAN + dir_name + Fore.LIGHTCYAN_EX + "' " + Fore.BLUE + "backup '" + Fore.LIGHTYELLOW_EX + backup_name + Fore.BLUE + "'" + Fore.LIGHTGREEN_EX + " CREATED" + Fore.RESET)
        os.chdir(dir_name)
        os.chdir("backups")
        os.mkdir(backup_name)

        os.chdir(r"D:\Universum\HSE\second course\data bases\Lab\Lab")


        students_file = io.open(dir_name + "/students.txt", "r", encoding='utf-8'
                                )
        students = students_file.readlines()
        students_file.close()
        students_backup_file = io.open(dir_name + "/backups/" + backup_name + "/students.txt", "w", encoding='utf-8')
        for i in students:
            students_backup_file.write(i)
        students_backup_file.close()

        variants_file = io.open(dir_name + "/variants.txt", "r", encoding='utf-8')
        variants = variants_file.readlines()
        variants_file.close()
        variants_backup_file = io.open(dir_name + "/backups/" + backup_name + "/variants.txt", "w", encoding='utf-8')
        for i in variants:
            variants_backup_file.write(i)
        variants_backup_file.close()

        testing_table_file = io.open(dir_name + "/testing_table.txt", "r", encoding='utf-8')
        testing_table = testing_table_file.readlines()
        testing_table_file.close()
        testing_table_file = io.open(dir_name + "/backups/" + backup_name + "/testing_table.txt", "w", encoding='utf-8')
        for i in variants:
            testing_table_file.write(i)
        testing_table_file.close()

    def restore_backup(selfdself, dir_name, backup_name):
        print(Fore.LIGHTCYAN_EX + "@DATABASE '" + Fore.CYAN + dir_name + Fore.LIGHTCYAN_EX + "' " + Fore.BLUE + "backup '" + Fore.LIGHTYELLOW_EX + backup_name + Fore.BLUE + "'" + Fore.LIGHTBLUE_EX + " RESTORED" + Fore.RESET)
        backup_students_file = io.open(dir_name + "/backups/" + backup_name + "/students.txt", 'r', encoding='utf-8')
        backup_variants_file = io.open(dir_name + "/backups/" + backup_name + "/variants.txt", 'r', encoding='utf-8')
        backup_testing_table_file = io.open(dir_name + "/backups/" + backup_name + "/testing_table.txt", 'r', encoding='utf-8')

        students = backup_students_file.readlines()
        variants = backup_variants_file.readlines()
        testing_table = backup_testing_table_file.readlines()

        backup_students_file.close()
        backup_variants_file.close()
        backup_testing_table_file.close()

        students_file = io.open(dir_name + "/students.txt", "w", encoding='utf-8')
        variants_file = io.open(dir_name + "/variants.txt", "w", encoding='utf-8')
        testing_table_file = io.open(dir_name + "/testing_table.txt", "w", encoding='utf-8')

        for i in students:
            students_file.write(i)
        students_file.close()
        for i in variants:
            variants_file.write(i)
        variants_file.close()
        for i in testing_table:
            testing_table_file.write(i)
        testing_table_file.close()

db = Dmbs('hse_students')

db.fill_students('hse_students', 'names.txt')
db.fill_variants('hse_students', 'test_names.txt')

db.print_students_table('hse_students')
db.print_tests('hse_students')

print("============")

db.find_student_by_id('hse_students', 90)
db.find_student_by_id('hse_students', 100)
db.find_test_by_id('hse_students', 3)
db.find_test_by_id('hse_students', 10)

print("============")

db.add_student('hse_students', 'Максим','Агеев','Александрович')
db.print_students_table('hse_students')
db.edit_student('hse_students', '6 Кирилл Бабин Иванович', '5 Кирилл Бабин Иванович')
db.edit_student('hse_students', '5 Игорь Васильев Андреевич', '228 Кек Лолов Лмаович')
db.edit_student('hse_students', '1 Андрей Акимов Николаевич', '1 Edited Edit Editing')
db.delete_student('hse_students', '0 Максим Агеев Александрович')
db.delete_student('hse_students', '0 Максим Агеев Александрович')
db.print_students_table('hse_students')

print("============")

db.add_test('hse_students', 'var6')
db.add_test('hse_students', 'var6')
db.edit_test('hse_students', '2 var3', '3 var10')
db.edit_test('hse_students', '4 var5', '4 var1')
db.edit_test('hse_students', '2 var3', '2 var15')
db.print_tests('hse_students')
db.delete_test('hse_students','var6')
db.delete_test('hse_students', 'var0')
db.print_tests('hse_students')


print("============")

db.form_testing_table('hse_students')
db.print_testing_table('hse_students')

print("============")
db.create_backup('hse_students', 'backup_1')

db.fill_students('hse_students', 'names_2.txt')
db.fill_variants('hse_students', 'test_names_2.txt')
db.form_testing_table('hse_students')
db.print_testing_table('hse_students')

print("============")
db.restore_backup('hse_students', 'backup_1')
db.form_testing_table('hse_students')
db.print_testing_table('hse_students')