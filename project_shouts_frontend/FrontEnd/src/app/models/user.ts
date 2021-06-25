enum GENDER_STATUS {
  Male,
  Female,
}

export class User {
  toBeTruthy(): any {
    throw new Error('Method not implemented.');
  }

  UserId!: number;
  UserName!: string;
  FirstName!: string;
  LastName!: string;
  Email!: string;
  MobileNo!: number;
  Password!: string;
  Gender!: GENDER_STATUS;
  DateOfBirth!: string;
  ProfilePicURL!: string;
}
