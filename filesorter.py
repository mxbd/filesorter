import os
import shutil

print('Welcome to python filesorter')

run_1 = True
while run_1:

    answer = str(input('\nTo sort Downloads folder press [D], or to select another Folder press [A]: '))

    if answer == 'D':
        # directory to sort
        path_D = r'C:\Users\Max\Downloads'

        # list all filenames in chosen directory
        file_list = os.listdir(path_D)

        for file in file_list:
            name, ext = os.path.splitext(file)

            # removes first element of extension (dot)
            ext = ext[1:]

            # if directory exists move file
            if os.path.exists(path_D + '/' + ext):
                shutil.move(path_D + '/' + file, path_D + '/' + ext + '/' + file)

            # else create a new directory and move file
            else:
                os.makedirs(path_D + '/' + ext)
                shutil.move(path_D + '/' + file, path_D + '/' + ext + '/' + file)

        sort_1 = str(input('\nDownloads Folder has been sorted! - Sort another Folder? (y/n): '))

        if sort_1 == 'y':
            continue
        elif sort_1 == 'n':
            break
        else:
            print('\nINVALID INPUT - Please try again')
            continue

    elif answer == 'A':

        run_2 = True
        while run_2:

            # directory to sort
            path = str(input('\nEnter the path of the folder you would like to sort: '))

            try:

                # list all filenames in chosen directory
                file_list = os.listdir(path)

                for file in file_list:
                    name, ext = os.path.splitext(file)

                    ext = ext[1:]

                    if os.path.exists(path + '/' + ext):
                        shutil.move(path + '/' + file, path + '/' + ext + '/' + file)

                    else:
                        os.makedirs(path + '/' + ext)
                        shutil.move(path + '/' + file, path + '/' + ext + '/' + file)

                sort_2 = str(input('\n' + path + ' has been sorted! - Sort another Folder? (y/n): '))

                if sort_2 == 'y':
                    continue
                elif sort_2 == 'n':
                    run_2 = False
                    run_1 = False
                else:
                    print('\nINVALID INPUT - Please try again')
                    continue

            # catch error if directory does not exist
            except FileNotFoundError:
                print('\nThe system cannot find the path specified: ' + path)
                rerun_2 = str(input('\nRun again? (y/n): '))

                if rerun_2 == 'y':
                    continue
                elif rerun_2 == 'n':
                    run_2 = False
                    run_1 = False
                else:
                    print('\nINVALID INPUT - Try again')
                    continue

    else:
        print('\nINVALID INPUT')
        rerun_1 = str(input('\nRun again? (y/n): '))

        if rerun_1 == 'y':
            continue
        elif rerun_1 == 'n':
            run_1 = False
        else:
            print('INVALID INPUT - Please try again')
            continue
